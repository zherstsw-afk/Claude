# Step 1b: no browser

Two parts. Part A (Recruitee) is the coach's alone and takes about 8 minutes. Part B (the i2 bookings) needs the i2 coach first; do the coach's side when the i2 coach says it is done, even on a later day.

Same style as the rest of setup: one instruction per message, three short lines at most, say exactly what to click, and check it yourself when you can.

## Part A. Recruitee through its API

What it replaces: Claude clicking in Recruitee in a Chrome tab. What the coach gets: no-show moves, disqualifications and notes with no browser at all.

1. **A folder for the key.** The i1 chat needs a folder from the coach's Mac connected to it. If none is connected: "Make a folder called i1 in your Documents folder. Then click the + in this chat and choose that folder." The token stays in that folder on their Mac.
2. **The empty key file.** Create `i1-recruitee.txt` in that folder with exactly these two lines and nothing else:
   ```
   company:
   token:
   ```
   Note its full path: it becomes `recruitee_key_file`.
3. **Make the token.** "Open Recruitee. Click Settings, then Apps and plugins, then Personal API tokens." Then: "Click New token. Name it i1 Claude. Copy the token it shows." If there is no Personal API tokens page or no New token button, the coach's hiring role does not allow tokens: tell them to ask their Recruitee admin to switch on "Manage API tokens" for their role (Settings, Company, Hiring roles), keep `recruitee_mode: browser` for now, and go to Part B.
4. **Fill in the key file.** "Open the i1 folder. Open i1-recruitee.txt (it opens in TextEdit). After token: paste the token. After company: type your company number from that same Recruitee page. Save and close." The company number is shown on the Personal API tokens page. If they cannot find it, the number after `company=` in a Recruitee web address also works, and so does the company's Recruitee subdomain (the part before `.recruitee.com` in their careers site).
   Never ask them to paste the token in the chat. If they do anyway, tell them to delete that token in Recruitee, make a new one, and put only the new one in the file.
5. **Check it.** Run `python3 "<the after-session skill's folder>/scripts/recruitee.py" --key-file "<path>" check`. Never open the file yourself. Pass: show the open jobs and disqualify reasons it lists, and confirm `recruitee_no_show_stage` and `disqualify_reason` against them. Fail: give the one-line fix the error suggests:
   - "Could not reach Recruitee": Cowork's network setting blocks it. On a Pro or Max plan: Settings, Capabilities, turn on "Allow network egress", then start a new chat and test again. On a Team or Enterprise plan, the plan's owner adds `api.recruitee.com` under Organization settings, Capabilities, Code execution, Additional allowed domains. Until then keep `recruitee_mode: browser`.
   - "401": the token was pasted wrong. Make a new one.
6. **Test candidate.** "In Recruitee, add a candidate called i1 Test to the Management Program job, at the i1 booked stage. Give it an email you can read, like yours with +i1test before the @." Never use a real candidate, not even for a dry run.
   - `find --email <test email>`: it must return exactly that profile.
   - `move ... --stage "<recruitee_no_show_stage>" --dry-run`, then the same without `--dry-run`.
   - Ask: "Did the 'we missed you' email reach your +i1test inbox?" Wait up to 10 minutes.
     - Yes: API moves run the stage's automations like a click does. Good.
     - No: Recruitee did not run the email for an API move. Tell the coach, keep `recruitee_mode: browser`, and stop Part A here. Do not switch a coach to a mode that stops sending the no-show email.
   - `note ... --text "i1 delegation test note"`. Ask the coach to look for it on the profile.
   - If `permission_disqualify` is not `never`: `disqualify ... --reason "<disqualify_reason>"`, then ask whether any email reached the test inbox, and tell the coach what that means (a real 3 gets the same email).
   - Ask the coach to delete the i1 Test candidate themselves. Claude never deletes a record.
7. **Switch it on.** Set `recruitee_mode: api` and `recruitee_key_file: <path>` in the settings block.

## Part B. i2 bookings through the Calendly connector

Why the i2 coach is needed: the i2 event type belongs to them. The coach's Calendly connection may only book on event types it is allowed to see, and today it cannot see another coach's event types (tested 2026-10-09: "Permission denied").

1. **Send the request.** Give the coach the message in `setup-i2-coach.md`, filled in, to send to the i2 coach (or the Calendly owner, if the first route fails). Then wait for "done".
2. **Find the i2 event type.** Find the i2 coach in the organisation's members (their scheduling link is the start of `i2_booking_url`). List that user's event types; if that is refused, list the coach's own event types and look for one shared with them. The right one has a scheduling link equal to `i2_booking_url` (or `i2_booking_url` is that user's page and the event type is the i2). Read it, then list its available times for the next 7 days. Pass: both work. Refused: the grant did not give API access; tell the coach to try the next route in `setup-i2-coach.md`, keep `i2_booking_mode: browser`.
3. **One test booking.** Ask the coach to agree with the i2 coach on one open slot at least two days away for a test. Book it through the connector exactly as the after-session skill's `references/calendly-api.md` says, with the invitee "i1 Test" and the coach's +i1test email, and no text-reminder number. Pass: the booking is made and Calendly's confirmation email reaches the +i1test inbox.
4. **Cancel it straight away.** Ask the coach to open that confirmation email and click Cancel. Then check the slot is open again. If it is not, tell the i2 coach which test booking to cancel.
5. **Switch it on.** Set `i2_booking_mode: api` and `i2_event_type_uri: <the event type's API reference>`.

If a robot check, a verification code or a refusal appears anywhere in Part B, stop and keep browser mode. Never try another way around it.

## After step 1b

- Both `api`: no Chrome extension, no i1 tab, no visible window. The daily planner skips the tab.
- Either still `browser`: do the Chrome check and the i1 tab test from step 1.
