# Booking the i2 through the Calendly connector (no browser)

Used when the settings block says `i2_booking_mode: api`. Otherwise follow `browser.md`.

This only works after the i2 coach has given this coach access to the i2 event type (`setup-i2-coach.md` in the setup skill) and setup's Calendly test passed. The settings block then holds `i2_event_type_uri`.

Do one person at a time.

1. **Check the slot is open.** List the available times of `i2_event_type_uri` for the agreed day. The agreed slot must be in the list, with the same start time once converted to the coach's `timezone`. If it is not there (full, past or not offered), do not book and do not pick another slot. Needs you.
2. **Read the event type** (once per run): its custom questions, which are required, and its location kind.
3. **Book.** Create the invitee on `i2_event_type_uri`:
   - `start_time`: the slot's UTC start time exactly as the availability list returned it;
   - invitee `name` and `email` from the person's Calendly i1 booking, `timezone` the coach's `timezone`;
   - `text_reminder_number`: their phone in +1 and ten digits, only if the i1 booking has one;
   - `location`: only the kind the event type uses (for Zoom, `{"kind": "zoom_conference"}`); none for a round-robin event type;
   - `questions_and_answers`: every required question, with the question text copied exactly and the answer from the i1 booking (the phone number for "Phone Number"). If a required question cannot be answered from the i1 booking, do not book. Needs you.
4. **Check the result** once: the response names the new event. Never send the same booking twice. If the call errors or times out, list the i2 event's invitees for that slot and look for the person's email before doing anything else. If they are not there, Needs you; do not retry on your own.
5. **Permission denied** means the i2 coach's grant was removed or never worked. Stop booking for this run, put everyone left on the "Needs you" list with "Calendly access to the i2 was refused", and do not fall back to the browser.

Calendly sends the candidate its normal confirmation email and reminders, exactly as when they book themselves. There is no robot check on this path.

Booking usually moves the person's Recruitee stage to the i2 stage by itself; see the end of `recruitee.md` (or `browser.md`).
