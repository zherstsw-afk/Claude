# i2 booking

Books the i1 coaches' qualified candidates into your i2 on your own Calendly, from the shared tracking sheet. Runs in the cloud, so the i1 coach's computer doesn't have to stay awake after the transcript.

## What it does

- Each hour, reads the handoff rows the i1 coaches' Claude wrote on the tracking sheet.
- Books each `ready` row into your i2 event type, if the slot is open.
- Writes back `booked` (and clears the candidate's email and phone) or `needs you` with a short reason.

## Setup

Say "set up i2 booking" in Claude. Setup is in `skills/i2-booking/references/setup.md`. Needs:

- Calendly connected to your own account;
- Google Sheets connected, with access to the shared tracking sheet (Editor).

## Version

0.1.0. Only the handoff route is included. The i1 coach's side is the handoff step in `i1-delegation` 0.7.0.
