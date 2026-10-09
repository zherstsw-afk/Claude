"""Offline tests for i1-delegation's recruitee.py against a fake Recruitee API.

The fake follows the request/response shapes of Recruitee's public API as used
by open-source clients. It proves the script's logic and safety rules, not
that the live API behaves the same: the coach's setup test does that.

Run: python3 -m unittest discover -s tests
"""

import contextlib
import io
import json
import os
import sys
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, HTTPServer

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "i1-delegation", "skills", "i1-after-session", "scripts"))

TOKEN = "test-token-123"
COMPANY = "777"


def fresh_state():
    return {
        "offers": {10: {"id": 10, "title": "Management Program", "pipeline_template": {"stages": [
            {"id": 1, "name": "Applied"}, {"id": 2, "name": "i1 Booked"},
            {"id": 3, "name": "i1 No Show"}, {"id": 4, "name": "i2 Booked"}]}},
            11: {"id": 11, "title": "Other job", "pipeline_template": {"stages": [{"id": 9, "name": "Applied"}]}}},
        "candidates": {
            100: {"id": 100, "name": "Test Candidate", "emails": ["test.cand@example.com"], "tags": [{"name": "i1 Coach"}],
                  "created_at": "2026-09-01", "placements": [{"id": 500, "offer_id": 10, "stage_id": 2, "disqualify_kind": None}]},
            101: {"id": 101, "name": "Two Jobs", "emails": ["two@example.com"], "tags": [], "created_at": "2026-09-01",
                  "placements": [{"id": 501, "offer_id": 10, "stage_id": 2}, {"id": 502, "offer_id": 11, "stage_id": 9}]},
        },
        "notes": {100: [], 101: []},
        "reasons": [{"id": 7, "name": "Not interested"}, {"id": 8, "name": "Not eligible"}],
        "writes": [],
    }


STATE = fresh_state()


class Fake(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def reply(self, code, body):
        data = json.dumps(body).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def route(self, method):
        if self.headers.get("Authorization") != f"Bearer {TOKEN}":
            return self.reply(401, {"error": "unauthorized"})
        path, _, query = self.path.partition("?")
        parts = path.strip("/").split("/")
        if parts[:2] != ["c", COMPANY]:
            return self.reply(404, {})
        rest = parts[2:]
        length = int(self.headers.get("Content-Length") or 0)
        body = json.loads(self.rfile.read(length)) if length else None
        s = STATE
        if method == "GET" and rest == ["offers"]:
            return self.reply(200, {"offers": list(s["offers"].values())})
        if method == "GET" and rest[0] == "offers":
            return self.reply(200, {"offer": s["offers"][int(rest[1])]})
        if method == "GET" and rest == ["disqualify_reasons"]:
            return self.reply(200, {"disqualify_reasons": s["reasons"]})
        if method == "GET" and rest == ["candidates"]:
            from urllib.parse import parse_qs
            q = parse_qs(query).get("query", [""])[0].lower()
            hits = [c for c in s["candidates"].values() if any(q in e for e in c["emails"]) or q in c["name"].lower()]
            return self.reply(200, {"candidates": hits})
        if rest[0] == "candidates" and len(rest) >= 2:
            cid = int(rest[1])
            if cid not in s["candidates"]:
                return self.reply(404, {})
            if len(rest) == 2 and method == "GET":
                return self.reply(200, {"candidate": s["candidates"][cid], "references": []})
            if rest[2:] == ["notes"] and method == "GET":
                return self.reply(200, {"notes": s["notes"][cid]})
            if rest[2:] == ["notes"] and method == "POST":
                note = {"id": len(s["notes"][cid]) + 1, "body": body["note"]["body"]}
                s["notes"][cid].append(note)
                s["writes"].append(("note", cid))
                return self.reply(201, {"note": note})
        if method == "PATCH" and rest[0] == "placements":
            pid = int(rest[1])
            pl = next(p for c in s["candidates"].values() for p in c["placements"] if p["id"] == pid)
            if rest[2] == "change_stage":
                pl["stage_id"] = body["stage_id"]
                s["writes"].append(("stage", pid, body["stage_id"]))
            elif rest[2] == "disqualify":
                pl["disqualify_kind"] = "admin"
                s["writes"].append(("disqualify", pid, body["disqualify_reason_id"]))
            return self.reply(200, {"placement": pl})
        return self.reply(404, {})

    def do_GET(self):
        self.route("GET")

    def do_POST(self):
        self.route("POST")

    def do_PATCH(self):
        self.route("PATCH")


class RecruiteeScriptTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = HTTPServer(("127.0.0.1", 0), Fake)
        threading.Thread(target=cls.server.serve_forever, daemon=True).start()
        os.environ["I1_RECRUITEE_API"] = f"http://127.0.0.1:{cls.server.server_port}"
        for k in ("HTTP_PROXY", "http_proxy"):
            os.environ.pop(k, None)
        os.environ["NO_PROXY"] = os.environ["no_proxy"] = "127.0.0.1,localhost"
        global recruitee
        import recruitee
        recruitee.API = os.environ["I1_RECRUITEE_API"]
        cls.dir = tempfile.mkdtemp()
        cls.key = os.path.join(cls.dir, "i1-recruitee.txt")
        with open(cls.key, "w") as f:
            f.write(f"company: {COMPANY}\ntoken: {TOKEN}\n")

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()

    def setUp(self):
        STATE.clear()
        STATE.update(fresh_state())
        recruitee._offers.clear()

    def run_cli(self, *args, key=None):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = recruitee.main(["--key-file", key or self.key, *args])
        text = out.getvalue()
        return code, json.loads(text), text

    def test_check(self):
        code, out, _ = self.run_cli("check")
        self.assertEqual(code, 0)
        self.assertIn("Not interested", out["disqualify_reasons"])

    def test_token_never_printed(self):
        for args in (["check"], ["find", "--email", "test.cand@example.com"]):
            _, _, text = self.run_cli(*args)
            self.assertNotIn(TOKEN, text)

    def test_bad_token(self):
        bad = os.path.join(self.dir, "bad.txt")
        with open(bad, "w") as f:
            f.write(f"company: {COMPANY}\ntoken: nope\n")
        code, out, text = self.run_cli("check", key=bad)
        self.assertEqual(code, 1)
        self.assertIn("401", out["error"])
        self.assertNotIn("nope", text)

    def test_missing_key_file(self):
        code, out, _ = self.run_cli("check", key=os.path.join(self.dir, "none.txt"))
        self.assertEqual(code, 1)
        self.assertIn("not found", out["error"])

    def test_incomplete_key_file(self):
        half = os.path.join(self.dir, "half.txt")
        with open(half, "w") as f:
            f.write("company: 777\ntoken:\n")
        code, out, _ = self.run_cli("check", key=half)
        self.assertEqual(code, 1)

    def test_find_matches_email_exactly(self):
        code, out, _ = self.run_cli("find", "--email", "TEST.cand@example.com")
        self.assertEqual(code, 0)
        self.assertEqual(out["matches_count"], 1)
        m = out["matches"][0]
        self.assertEqual(m["placements"][0]["stage_name"], "i1 Booked")
        self.assertEqual(m["tags"], ["i1 Coach"])
        code, out, _ = self.run_cli("find", "--email", "cand@example.com")
        self.assertEqual(out["matches_count"], 0)

    def test_move_dry_run_writes_nothing(self):
        code, out, _ = self.run_cli("move", "--candidate", "100", "--email", "test.cand@example.com", "--stage", "i1 No Show", "--dry-run")
        self.assertEqual(code, 0)
        self.assertEqual(out["would_move"]["to_stage"], "i1 No Show")
        self.assertEqual(STATE["writes"], [])

    def test_move_then_never_repeat(self):
        code, out, _ = self.run_cli("move", "--candidate", "100", "--email", "test.cand@example.com", "--stage", "i1 no show")
        self.assertEqual((code, out["changed"], out["stage_now"]), (0, True, "i1 No Show"))
        code, out, _ = self.run_cli("move", "--candidate", "100", "--email", "test.cand@example.com", "--stage", "i1 No Show")
        self.assertEqual((code, out["changed"]), (0, False))
        self.assertEqual(STATE["writes"], [("stage", 500, 3)])

    def test_move_refuses_wrong_email(self):
        code, out, _ = self.run_cli("move", "--candidate", "100", "--email", "someone@else.com", "--stage", "i1 No Show")
        self.assertEqual(code, 1)
        self.assertEqual(STATE["writes"], [])

    def test_move_refuses_unknown_stage(self):
        code, out, _ = self.run_cli("move", "--candidate", "100", "--email", "test.cand@example.com", "--stage", "No Show")
        self.assertEqual(code, 1)
        self.assertIn("i1 No Show", out["error"])
        self.assertEqual(STATE["writes"], [])

    def test_move_needs_offer_when_two_jobs(self):
        code, out, _ = self.run_cli("move", "--candidate", "101", "--email", "two@example.com", "--stage", "i1 No Show")
        self.assertEqual(code, 1)
        self.assertIn("--offer", out["error"])
        code, out, _ = self.run_cli("move", "--candidate", "101", "--email", "two@example.com", "--stage", "i1 No Show", "--offer", "10")
        self.assertEqual(code, 0)
        self.assertEqual(STATE["writes"], [("stage", 501, 3)])

    def test_disqualify_once(self):
        code, out, _ = self.run_cli("disqualify", "--candidate", "100", "--email", "test.cand@example.com", "--reason", "Not interested")
        self.assertEqual((code, out["changed"]), (0, True))
        code, out, _ = self.run_cli("disqualify", "--candidate", "100", "--email", "test.cand@example.com", "--reason", "Not interested")
        self.assertEqual(out["changed"], False)
        self.assertEqual(STATE["writes"], [("disqualify", 500, 7)])
        code, out, _ = self.run_cli("move", "--candidate", "100", "--email", "test.cand@example.com", "--stage", "i1 No Show")
        self.assertEqual(code, 1)  # never move a disqualified placement

    def test_disqualify_unknown_reason(self):
        code, out, _ = self.run_cli("disqualify", "--candidate", "100", "--email", "test.cand@example.com", "--reason", "Nope")
        self.assertEqual(code, 1)
        self.assertEqual(STATE["writes"], [])

    def test_note_once(self):
        text = "Unsure about summer hours. i2 Tue 5:00 PM, call Mon 6:00 PM."
        code, out, _ = self.run_cli("note", "--candidate", "100", "--email", "test.cand@example.com", "--text", text)
        self.assertEqual((code, out["changed"]), (0, True))
        code, out, _ = self.run_cli("note", "--candidate", "100", "--email", "test.cand@example.com", "--text", text)
        self.assertEqual(out["changed"], False)
        self.assertEqual(STATE["writes"], [("note", 100)])

    def test_no_candidate_data_on_disk(self):
        before = set(os.listdir(self.dir))
        self.run_cli("find", "--email", "test.cand@example.com")
        self.run_cli("note", "--candidate", "100", "--email", "test.cand@example.com", "--text", "x")
        self.assertEqual(set(os.listdir(self.dir)), before)


if __name__ == "__main__":
    unittest.main()
