---
name: i2-booking
description: Books the i1 coaches' qualified candidates into the i2 on the i2 coach's own Calendly, reading ready rows from the shared tracking sheet's handoff block. Use when a scheduled check says to book handoff rows, or when the i2 coach says "book the i2 handoffs", "check my i2 bookings", "run the i2 booking", or "set up i2 booking".
---

# i2 booking (handoff rows)

Runs for the i2 coach. Each run reads the **handoff block** on the shared tracking sheet (the columns to the right of the i1 coach's sheet, on each week tab) and books every `ready` row into the i2 event type on this coach's own Calendly. It writes back the result. It never books anything it hasn't been told to, and never a second time.

One principle sits behind every rule: **when unsure, don't book; set the row to `needs you` and say why.** Never pick another slot.

## Keep each run small

- **One read first.** Read the handoff block on the current and next week tabs in one call. If no row is `ready`, stop now and report one line: "no i2 handoffs". Do nothing else.
- **Batch.** Check Calendly once per date (not once per person), and write all the result cells for the run in one sheet update, not one per row.
- **Only on i1 days.** This task is scheduled only in the hours after an i1 starts (`references/setup.md`, step 4), so a run that finds nothing should be cheap.

## Before starting

1. **Settings.** Find the block headed `i2 booking settings` in the scheduled task or earlier in this chat. If it is missing or a value is blank, stop and tell the coach to say "set up i2 booking".
2. **Paused?** If the coach has said "pause i2 booking" and not "resume i2 booking" since, reply "i2 booking is paused" and stop.
3. **Connections.** Calendly (this coach's own account) and Google Sheets (with access to the shared sheet) must both be reachable. If either is not, stop and say which one.

## Steps

1. **Find the week tabs.** The sheet's tabs are named "Week N", where Week 1 starts on `week1_monday` and each week adds one. Read the current week's tab and the next week's.
2. **Read the handoff block.** On each tab, the block starts at column `handoff_first_column` on row 2 (the header). Data rows start at row 3. The columns, in order: Name, Email, Phone, i2 host, i2 date, i2 start, Call time, Status, Booked at, Note. Read rows with Status `ready` **and i2 host equal to `i2_host_first_name`** (not case-sensitive). Several i2 coaches can share one sheet, so rows for another i2 coach are not yours: leave them exactly as they are, not even to read the email or phone into your run.
3. **For each `ready` row:**
   a. **Already booked?** Look at this coach's Calendly i2 event for that date and start: if an invitee with the row's email is already there and active, set Status `booked`, Booked at to now, and clear Email and Phone. Do not book again.
   b. **Slot available?** List this coach's i2 event type's available times for that day. The row's i2 start, in the coach's `timezone`, must be in the list. If not, set Status `needs you` and Note `slot not open`. Do not pick another slot.
   c. **Book.** Create the invitee on `i2_event_type_uri`:
      - `start_time`: the available slot's UTC start time, exactly as listed;
      - invitee name and email from the row, `timezone` the coach's `timezone`;
      - `text_reminder_number` from the row's phone, only if it is present;
      - `location` only the kind the event type uses (Zoom), and none for a round-robin event type;
      - `questions_and_answers`: every required question with its exact text. Use the row's phone for "Phone Number" and the other answers from the i1 booking's record in the row if present, otherwise `Booked by i1 coach handoff` for free text. If a required question can't be answered, set `needs you` and Note `required question unanswered`.
   d. **Record.** After a successful booking: Status `booked`, Booked at the current time, Email and Phone cleared. If the call errors or times out, check step (a) once more before anything else. If the person is not there, set `needs you` and Note `booking call failed`. Never retry on your own.
   e. **Refused.** If Calendly refuses the booking (permission or plan), set `needs you` and Note `Calendly refused`, and stop booking for the run.
4. **Never change a row you didn't read as `ready`**, except setting `booked` / `needs you` on rows you processed in this run.
5. **Report**, short: the week tabs read; one line per row processed with its result (`booked`, `already booked`, `needs you` and why). No names, emails or phone numbers in the report.

## Limits

- Never delete a row or a cell's text except clearing Email and Phone after a booking is confirmed.
- Never write anywhere on the sheet outside the handoff block. Never touch the i1 coach's columns.
- Never book a person without a row, with a different slot, or with a different name from the row.
- Never sign in anywhere and never ask for a Calendly token. If a connection is signed out, stop and say so.
- Calendly sends the candidate its normal confirmation and reminders, as it does for any booking.
- Candidate details are used in the run only. Never write them to a file or into a note.
