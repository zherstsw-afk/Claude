# Sending your i2 coach the handoff: checklist for i1 coaches

Do this once, before your first session with the handoff on. It takes about 15 minutes.

1. **Find the handoff column.** On a week tab of the tracking sheet, find the first column to the right of everything the sheet uses (for the standard template, that's AF). Write it down.
2. **Write the headers on row 2 of each week tab.** Put these ten headers in row 2, starting at that column, in this order: Name, Email, Phone, i2 host, i2 date, i2 start, Call time, Status, Booked at, Note. Row 1 is protected on the sheet, so start at row 2. Do it on every week tab.
3. **Share the sheet** with your i2 coach's Google account as an Editor.
4. **Send your i2 coach** the kit: the guide, the plugin zip, and a copy of the prompt with these filled in: their first name (exactly how you'll write it in the i2 host column), the timezone, the sheet ID, the handoff column, the Week 1 Monday date, and your i1 days and start times.
5. **Set your i1 settings** in your Claude: `i2_booking_mode: handoff` and `handoff_first_column: <your column>`.
6. **Test.** Add one test row with status `ready` and a `+i2test` email on your own address, then tell your i2 coach the test is in. When they've booked it and cancelled the test, clear the test row.

From then on, your after-session run writes one `ready` row for each 1 or 2, and your i2 coach's Claude books it.
