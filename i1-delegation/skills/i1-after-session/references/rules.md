# Rules for messy cases

When unsure, do nothing that reaches the candidate and put the case on the "Needs you" list.

| Situation | What to do |
|---|---|
| Booked, and named on the recording | Showed. Fill the row. |
| Booked, not named on the recording | No-show: Show? FALSE, gray, move to the no-show stage in Recruitee. This holds even if the coach told the group the person rescheduled. |
| Nobody booked is named on the recording | The recording is wrong or incomplete. Move nobody, text nobody, fill nothing. Needs you. |
| Everybody was a no-show (the coach says so, or the recording is a full session with no names) | Fill the rows as no-shows and write `No-show` in the Notes of the first row, so the block reads as processed. |
| Booking cancelled | No-show: Show? FALSE, gray, note `Cancelled`, move to the no-show stage in Recruitee. (When `cancelled_booking` is `leave`: note `Cancelled`, no colour, no Recruitee move.) |
| Cancelled, and holds another active i1 booking | Row gray, note `Moved to <day time>`. Do NOT move them in Recruitee: the move emails "we missed you" to someone who is still booked. List them in the report. |
| Same person booked twice | Treat as one person: one text, one filled row. Note `Duplicate booking` on the other row and leave it uncoloured. No Recruitee move for the duplicate. |
| Two booked people share a first name | Match on the full name the coach says. If the coach said only the first name and it is unclear which person, fill neither. Needs you. |
| On the recording but not booked | Write nothing. Needs you. |
| Two Recruitee profiles for one person | Use the one whose email matches the booking, then the one with the coach's tag. Still unclear: skip. Needs you. |
| Name spelled differently across systems | Match on email, then phone. Correct the first name in texts only when the email confirms the spelling. Otherwise leave it and flag it. |
| Phone number cannot be read | No text. Needs you. |
| Coach did not say 1, 2 or 3 | Mark Show? TRUE and green. Leave Conversion blank. No booking, no text. Needs you. |
| i2 slot not said | Write `Find a time` only if the coach said they would follow up; otherwise leave it blank. No booking, no call, no text. Needs you. |
| i2 slot full or not offered | No booking. Never pick another slot. Needs you. |
| Call time not said | Book the i2. No qualification text, no calendar event, no Deadline entry. Needs you. |
| Call time is at or before the time the text would send | Book the i2 and add the calendar event. No qualification text. Needs you. |
| Position 3 | Red row. No booking, no text. Disqualify them in Recruitee with the reason in `disqualify_reason` (`references/browser.md`), subject to `permission_disqualify`. A 3 who showed is never moved to the no-show stage. |
| Recruitee stage did not move after a booking | Leave it. Check once more at the end of this run. Flag it if still unchanged. |
| Coach named someone to skip | Leave every system alone for that person. |
| The i2 is later today | The qualification call is today, before the i2. |
| The session did not start on the hour | The texting timer cannot serve it. Do every step except texts, and flag it. |
