#!/usr/bin/env python3
"""Recruitee steps of the i1 after-session routine, over Recruitee's API.

Replaces clicking in Recruitee in a Chrome tab: find a candidate by email,
move a no-show to a stage, disqualify a 3, add a note for a 2.
Standard library only; prints one JSON object; exit code 0 = ok, 1 = refused
or failed (nothing changed unless the output says so).

Credentials come from a key file the coach fills in on their own Mac:

    company: 12345
    token: <personal API token>

The token is never printed. Candidate data is never written to disk or logs.

Usage (paths quoted):
    recruitee.py --key-file F check
    recruitee.py --key-file F find --email E
    recruitee.py --key-file F move --candidate ID --email E --stage "i1 No Show" [--offer ID] [--dry-run]
    recruitee.py --key-file F disqualify --candidate ID --email E --reason "Not interested" [--offer ID] [--dry-run]
    recruitee.py --key-file F note --candidate ID --email E --text "..." [--dry-run]

Safety rules held here, not only in the skill:
- every write names the booking's email and is refused unless the profile holds it;
- never repeats an action: a move to the current stage, a second
  disqualification or an identical note is a no-op;
- a profile in several open jobs with no --offer is refused;
- --dry-run reads everything and writes nothing.
"""

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

# Overridable for the offline test suite only.
API = os.environ.get("I1_RECRUITEE_API", "https://api.recruitee.com")


class Refused(Exception):
    pass


def norm(s):
    return str(s or "").strip().lower()


def name_of(x):
    return x if isinstance(x, str) else (x or {}).get("name")


# ---------- key file ----------

def read_key_file(path):
    if not path:
        raise Refused("No key file given. Pass --key-file with the path to i1-recruitee.txt.")
    if not os.path.isfile(path):
        raise Refused("The Recruitee key file was not found. Ask the coach to check i1-recruitee.txt is in their i1 folder.")
    values = {}
    with open(path, encoding="utf-8-sig") as f:
        for line in f:
            if ":" in line:
                k, v = line.split(":", 1)
                values[norm(k)] = v.strip()
    company, token = values.get("company", ""), values.get("token", "")
    if not company or not token:
        raise Refused("The Recruitee key file is missing the company or the token line. Ask the coach to fill both in and save.")
    return company, token


# ---------- HTTP ----------

class Api:
    def __init__(self, company, token):
        self.root = f"{API}/c/{urllib.parse.quote(company.strip())}"
        self.token = token.strip()

    def call(self, method, path, body=None):
        data = json.dumps(body).encode() if body is not None else None
        for attempt in range(3):
            req = urllib.request.Request(self.root + path, data=data, method=method)
            req.add_header("Authorization", f"Bearer {self.token}")
            req.add_header("Accept", "application/json")
            req.add_header("User-Agent", "i1-delegation/0.6")
            if data is not None:
                req.add_header("Content-Type", "application/json")
            try:
                with urllib.request.urlopen(req, timeout=30) as res:
                    text = res.read().decode()
                    return json.loads(text) if text else {}
            except urllib.error.HTTPError as e:
                where = f"{method} {path.split('?')[0]}"  # no names or emails in messages
                if e.code == 429 and attempt < 2:
                    time.sleep(2 * (attempt + 1))
                    continue
                if e.code == 401:
                    raise Refused("Recruitee refused the token (401). It may be wrong or revoked: make a new one in Recruitee, Settings, Apps and plugins, Personal API tokens.")
                if e.code == 403:
                    raise Refused(f"Recruitee says this account may not do that (403) on {where}. The coach's hiring role may lack the permission.")
                if e.code == 404:
                    raise Refused(f"Not found (404) on {where}. Check the company number, or the record no longer exists.")
                raise Refused(f"Recruitee answered {e.code} on {where}.")
            except urllib.error.URLError as e:
                raise Refused(f"Could not reach Recruitee ({e.reason}). If this runs in Cowork, its network setting may block api.recruitee.com.")

    def get(self, path):
        return self.call("GET", path)

    def post(self, path, body):
        return self.call("POST", path, body)

    def patch(self, path, body):
        return self.call("PATCH", path, body)


# ---------- reading ----------

_offers = {}


def get_offer(api, offer_id):
    if offer_id not in _offers:
        _offers[offer_id] = api.get(f"/offers/{offer_id}").get("offer") or {}
    return _offers[offer_id]


def stages_of(api, offer):
    stages = (offer.get("pipeline_template") or {}).get("stages")
    if not stages and offer.get("pipeline_template_id"):
        t = api.get(f"/pipeline_templates/{offer['pipeline_template_id']}")
        stages = (t.get("pipeline_template") or {}).get("stages")
    return [{"id": s.get("id"), "name": s.get("name")} for s in (stages or [])]


def describe_placement(api, p, references):
    offer_id = p.get("offer_id") or (p.get("offer") or {}).get("id")
    stage_id = p.get("stage_id") or (p.get("stage") or {}).get("id")
    offer_title = (p.get("offer") or {}).get("title")
    stage_name = (p.get("stage") or {}).get("name")
    for r in references or []:
        if r.get("type") == "Stage" and r.get("id") == stage_id:
            stage_name = stage_name or r.get("name")
        if r.get("type") == "Offer" and r.get("id") == offer_id:
            offer_title = offer_title or r.get("title")
    if offer_id and (not stage_name or not offer_title):
        offer = get_offer(api, offer_id)
        offer_title = offer_title or offer.get("title")
        if not stage_name:
            stage_name = next((s["name"] for s in stages_of(api, offer) if s["id"] == stage_id), None)
    return {
        "placement_id": p.get("id"),
        "offer_id": offer_id,
        "offer_title": offer_title,
        "stage_id": stage_id,
        "stage_name": stage_name,
        "disqualified": bool(p.get("disqualified") or p.get("disqualify_kind") or p.get("disqualified_at") or p.get("disqualify_reason")),
        "hired": bool(p.get("hired_at")),
    }


def profile(api, candidate_id):
    data = api.get(f"/candidates/{urllib.parse.quote(str(candidate_id))}")
    c = data.get("candidate")
    if not c:
        raise Refused("Recruitee returned no candidate for that ID.")
    refs = data.get("references")
    return {
        "candidate_id": c.get("id"),
        "name": c.get("name"),
        "emails": [e for e in (name_of(x) for x in c.get("emails") or []) if e],
        "tags": [t for t in (name_of(x) for x in c.get("tags") or []) if t],
        "created_at": c.get("created_at"),
        "placements": [describe_placement(api, p, refs) for p in c.get("placements") or []],
    }


def check_email(prof, email):
    if norm(email) not in [norm(e) for e in prof["emails"]]:
        raise Refused("This profile does not hold the booking's email. Nothing was changed. Run find with the email to get the right profile.")


def pick_placement(prof, offer_id):
    if offer_id is not None:
        hit = next((p for p in prof["placements"] if str(p["offer_id"]) == str(offer_id)), None)
        if not hit:
            raise Refused("The profile is not in that job (--offer). Nothing was changed.")
        return hit
    open_ = [p for p in prof["placements"] if not p["hired"]]
    if len(open_) == 1:
        return open_[0]
    if not open_:
        raise Refused("The profile is in no open job. Nothing was changed.")
    jobs = ", ".join(f"{p['offer_id']} ({p['offer_title']})" for p in open_)
    raise Refused(f"The profile is in {len(open_)} jobs. Run again with --offer set to one of: {jobs}. Nothing was changed.")


def placement_after(api, candidate_id, placement_id):
    return next((p for p in profile(api, candidate_id)["placements"] if p["placement_id"] == placement_id), {})


# ---------- commands ----------

def cmd_check(api, a):
    offers = api.get("/offers?scope=active&view_mode=brief").get("offers") or []
    try:
        reasons = api.get("/disqualify_reasons").get("disqualify_reasons") or []
    except Refused:
        reasons = []
    return {
        "ok": True,
        "open_jobs": [{"offer_id": o.get("id"), "title": o.get("title")} for o in offers],
        "disqualify_reasons": [r.get("name") for r in reasons],
    }


def cmd_find(api, a):
    want = norm(a.email)
    if "@" not in want:
        raise Refused("Give an email address.")
    found = api.get(f"/candidates?query={urllib.parse.quote(a.email.strip())}&limit=20").get("candidates") or []
    ids = [c["id"] for c in found if want in [norm(name_of(e)) for e in c.get("emails") or []]]
    matches = [profile(api, i) for i in ids]
    return {"ok": True, "matches_count": len(matches), "matches": matches}


def cmd_move(api, a):
    prof = profile(api, a.candidate)
    check_email(prof, a.email)
    pl = pick_placement(prof, a.offer)
    if pl["disqualified"]:
        raise Refused("That placement is disqualified. Nothing was changed.")
    stages = stages_of(api, get_offer(api, pl["offer_id"]))
    target = next((s for s in stages if norm(s["name"]) == norm(a.stage)), None)
    if not target:
        raise Refused(f"No stage named '{a.stage}' in this job. Stages: {', '.join(s['name'] for s in stages)}. Nothing was changed.")
    if pl["stage_id"] == target["id"]:
        return {"ok": True, "changed": False, "reason": "already in that stage", "stage": target["name"]}
    plan = {"job": pl["offer_title"], "from_stage": pl["stage_name"], "to_stage": target["name"]}
    if a.dry_run:
        return {"ok": True, "dry_run": True, "would_move": plan}
    api.patch(f"/placements/{pl['placement_id']}/change_stage", {"stage_id": target["id"]})
    after = placement_after(api, a.candidate, pl["placement_id"])
    moved = after.get("stage_id") == target["id"]
    return {"ok": moved, "changed": moved, **plan, "stage_now": after.get("stage_name")}


def cmd_disqualify(api, a):
    prof = profile(api, a.candidate)
    check_email(prof, a.email)
    pl = pick_placement(prof, a.offer)
    if pl["disqualified"]:
        return {"ok": True, "changed": False, "reason": "already disqualified"}
    reasons = api.get("/disqualify_reasons").get("disqualify_reasons") or []
    reason = next((r for r in reasons if norm(r.get("name")) == norm(a.reason)), None)
    if not reason:
        raise Refused(f"No disqualify reason named '{a.reason}'. Reasons: {', '.join(r.get('name', '') for r in reasons)}. Nothing was changed.")
    plan = {"job": pl["offer_title"], "stage": pl["stage_name"], "reason": reason["name"]}
    if a.dry_run:
        return {"ok": True, "dry_run": True, "would_disqualify": plan}
    api.patch(f"/placements/{pl['placement_id']}/disqualify", {"disqualify_reason_id": reason["id"]})
    done = bool(placement_after(api, a.candidate, pl["placement_id"]).get("disqualified"))
    return {"ok": done, "changed": done, **plan}


def cmd_note(api, a):
    prof = profile(api, a.candidate)
    check_email(prof, a.email)
    text = (a.text or "").strip()
    if not text:
        raise Refused("The note is empty.")
    cid = urllib.parse.quote(str(a.candidate))
    try:
        notes = api.get(f"/candidates/{cid}/notes").get("notes") or []
    except Refused:
        notes = []
    if any(norm(text) in norm(n.get("body")) for n in notes):
        return {"ok": True, "changed": False, "reason": "the same note is already on the profile"}
    if a.dry_run:
        return {"ok": True, "dry_run": True, "would_add_note": text}
    note = api.post(f"/candidates/{cid}/notes", {"note": {"body": text}}).get("note") or {}
    return {"ok": bool(note.get("id")), "changed": bool(note.get("id"))}


def parser():
    p = argparse.ArgumentParser(description="i1 delegation: Recruitee over its API")
    p.add_argument("--key-file", default=os.environ.get("I1_RECRUITEE_KEY_FILE"))
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("check")
    f = sub.add_parser("find")
    f.add_argument("--email", required=True)
    for name in ("move", "disqualify", "note"):
        s = sub.add_parser(name)
        s.add_argument("--candidate", required=True)
        s.add_argument("--email", required=True)
        s.add_argument("--dry-run", action="store_true")
        if name != "note":
            s.add_argument("--offer")
        if name == "move":
            s.add_argument("--stage", required=True)
        if name == "disqualify":
            s.add_argument("--reason", required=True)
        if name == "note":
            s.add_argument("--text", required=True)
    return p


COMMANDS = {"check": cmd_check, "find": cmd_find, "move": cmd_move, "disqualify": cmd_disqualify, "note": cmd_note}


def main(argv=None):
    a = parser().parse_args(argv)
    try:
        api = Api(*read_key_file(a.key_file))
        out = COMMANDS[a.cmd](api, a)
    except Refused as e:
        out = {"ok": False, "error": str(e)}
    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0 if out.get("ok") else 1


if __name__ == "__main__":
    sys.exit(main())
