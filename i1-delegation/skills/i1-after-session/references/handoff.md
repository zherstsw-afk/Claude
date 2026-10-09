# The handoff: i2 bookings through the tracking sheet

Used when the settings block says `i2_booking_mode: handoff`. The i2 coach's own Claude (the `i2-booking` plugin) books the 1s and 2s on the i2 coach's own Calendly connector. This coach's Claude never touches the i2 coach's Calendly. The two Claudes pass work through the tracking sheet itself, in a block of columns to the right of everything else on each week tab.

## Where the block is

- Each week tab has a handoff block starting at the column `handoff_first_column` in the settings block (set during setup: the first column after the last column the sheet uses, found by setup and never guessed).
- Row 2 of the block is the header. Row 1 is protected on the sheet and is never written. Rows 3 onward hold one row per 1 or 2 for that week's sessions.
- Never write anywhere else on the tab for this step. The rest of the sheet is written by the routine as before.

## The columns (in order, starting at `handoff_first_column`)

| # | Column | Who writes it | What goes in |
|---|---|---|---|
| 0 | Name | this coach's Claude | The name exactly as on the sheet. Used to match rows. |
| 1 | Email | this coach's Claude | The i1 booking's email. Cleared by the i2 coach's Claude once booked. |
| 2 | Phone | this coach's Claude | The i1 booking's phone, +1 and ten digits. Cleared once booked. |
| 3 | i2 host | this coach's Claude | The i2 coach's first name (`i2_host_first_name`). |
| 4 | i2 date | this coach's Claude | The agreed i2 day, as a date. |
| 5 | i2 start | this coach's Claude | The agreed i2 start, e.g. `5:00 PM`, in the coach's `timezone`. |
| 6 | Call time | this coach's Claude | `H:MM PM` for the qualification call, or blank if not said. |
| 7 | Status | both | `ready`, `booked`, `needs you` or `cancelled`. |
| 8 | Booked at | the i2 coach's Claude | Time of the booking, e.g. `2026-10-14 17:42`. |
| 9 | Note | either | Short reason only, never contact details. e.g. `slot full`, `already booked`, `Calendly refused`. |

## This coach's side (the routine's step 7 in handoff mode)

For each 1 or 2 with an agreed slot and call time, after the routine's other steps:

1. Find the week tab for the session's date. Read the handoff block's header row. If it isn't there, stop the handoff step, tell the coach to run setup's handoff check, and put the people on "Needs you".
2. Look for an existing row with the same name and the same i2 date and start. If it exists with status `ready`, `booked` or `cancelled`, do nothing. Never add a second row for the same person and slot.
3. Otherwise add one row: name from the sheet, email and phone from the i1 Calendly invitee record, host, date, start, call time, status `ready`.
4. Never write a row for someone without a slot, a call time, an email or a phone. Put them on "Needs you" with the reason, and leave the row out.
5. Never change another row's status. Only the i2 coach's Claude sets `booked`.
6. A 3 or a no-show gets no row.

If the i2 slot is later changed or the person cancels, set the row's status to `cancelled` and add a note. Never delete a row.

## The i2 coach's side

Set up with the `i2-booking` plugin. Each run:

1. For each handoff block on the current and next week tabs, find rows with status `ready`.
2. For each, check the i2 coach's own Calendly first: if the person already holds that slot (matched by email), set `booked` and go on. This stops a repeat.
3. Otherwise book the slot on the i2 coach's own i2 event type, with the same rules as this coach's `calendly-api.md`: the start must be listed as available, required questions answered exactly. Then set `booked`, the time, and blank the email and phone cells.
4. If the slot is not available or the booking is refused, set `needs you` and a short note. Never pick another slot.

## Privacy

- The handoff block holds candidate contact details only until the booking is made. The i2 coach's Claude clears email and phone once booked; the name stays for matching and for the record.
- Student Works has allowed coaches to share the sheet for this purpose. The sheet is shared with the i2 coach only.
- Nothing from this block is written to a file on either Mac or the plugin. The sheet is the only copy outside the two Calendly accounts.
