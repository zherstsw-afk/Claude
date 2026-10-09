# Recruitee over its API (no browser)

Used when the settings block says `recruitee_mode: api`. Otherwise follow `browser.md`.

Claude runs a bundled script, `scripts/recruitee.py` in this skill's folder, with Python 3. It talks to Recruitee's API with the coach's own personal API token. The token is in a key file, `i1-recruitee.txt`, in the folder connected to the i1 chat (`recruitee_key_file` in the settings). The coach filled it in themselves.

- Never open, print, copy or quote the key file. Only pass its path to the script.
- Never ask the coach to paste the token into the chat.
- The script prints JSON. `"ok": true` means done (or nothing to do); `"ok": false` comes with an `error`, and the script changed nothing unless the output says `"changed": true`.

Every command starts the same way:

```
python3 "<this skill's folder>/scripts/recruitee.py" --key-file "<recruitee_key_file>" <command> ...
```

If the key file is not there (the Claude app is closed, or the folder is not connected), or the script says it cannot reach Recruitee: skip the Recruitee steps, finish everything else, and put every move, disqualification and note on the "Needs you" list with that reason. Do not fall back to the browser on your own.

## Find the person's profile

`find --email "<email from the Calendly i1 booking>"`

It returns every profile that holds that email, with each job (`offer_title`), current `stage_name`, `disqualified`, `tags` and `created_at`.

- One match: use its `candidate_id`.
- Two or more: "Two profiles for one person" below.
- None: Needs you ("no Recruitee profile with the booking's email").
- The profile is in several jobs: the write commands refuse and list the jobs. Pass `--offer <offer_id>` for the job whose title matches the program. If unclear, Needs you.

## Moving a no-show

Moving someone to the no-show stage runs the stage's automations, which email them "we missed you" straight away. Be sure before running it.

1. Find the profile as above. If `stage_name` already is `recruitee_no_show_stage`, stop: moved already.
2. `move --candidate <id> --email "<booking email>" --stage "<recruitee_no_show_stage>"`
3. Check the output says `"changed": true` and `stage_now` is the no-show stage.

The same "do not move" list applies as in `browser.md`: a cancelled person who holds another active i1 booking; the second row of a duplicate booking; anyone the coach said to skip.

## Disqualifying a 3

Only for a person who showed and whom the coach called a 3, and subject to `permission_disqualify` exactly as in `browser.md`.

1. Find the profile. If a placement already shows `"disqualified": true`, stop.
2. `disqualify --candidate <id> --email "<booking email>" --reason "<disqualify_reason>"`
3. If the reason is not on the list, the script refuses and lists the reasons: Needs you.

The API has no "send email" switch. Recruitee sends whatever email is tied to that reason, if any. That is why setup checks this on a test candidate; `disqualify_send_email` is not used in API mode.

## Adding a note for each 2

`note --candidate <id> --email "<booking email>" --text "<one or two sentences: what holds them back, their i2 slot, the call time>"`

No personal characteristics in notes. The script skips a note that is already on the profile.

## Unsure? Dry run

Add `--dry-run` to `move`, `disqualify` or `note` to see what would happen without changing anything. Use it whenever the case is not clear-cut, and for every step when the coach has said `ask` for that permission: show the dry-run result, ask once, then run it for real.

## Two profiles for one person

Use the profile whose email matches the booking. If both match, use the one whose `tags` include `recruitee_coach_tag`. If neither or both still fit, skip the person: Needs you. Never touch a profile created in an earlier year (`created_at`).

## The i2 stage after a booking

Booking usually moves the person's Recruitee stage to the i2 stage by itself, and it can lag. At the end of the run, `find` each person booked into the i2 and flag anyone whose stage has not moved. Do not move them by hand.
