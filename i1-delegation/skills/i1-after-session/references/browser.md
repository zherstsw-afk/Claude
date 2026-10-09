# Browser steps: Calendly and Recruitee

These run in the coach's own Chrome through the Claude extension. The coach is already signed in to both sites. Never sign in for them.

Use element references from a page search, not screen coordinates: the window size changes.

## Before the first browser step

Get the tab context. Claude's tab group should hold exactly one tab: the i1 tab, opened that morning (see "The i1 tab" below) and dragged by the coach into its own visible window. Use that one tab for everything, one site at a time: navigate it to Calendly for the bookings, then navigate the same tab to Recruitee for the moves, disqualifications and notes.

- Never open a second tab. Claude can only control tabs in one window, and a second tab that ends up in another window is lost.
- No tab in the group: open one (see "The i1 tab"), tell the coach in one line to drag it into its own window and leave it visible, and carry on in it.
- A Calendly page that stays blank after a reload and a 10 second wait means the window is hidden or minimized. Do not book. Put the bookings on the "Needs you" list with the line "i1 window was not visible".
- If the browser cannot be reached, skip steps 7 and 8, finish everything else, and put every booking and move on the "Needs you" list.

## The i1 tab

The daily setup, done before the coach's first i1 of the day. The daily planner starts it; the coach can also say "open my i1 tab".

1. Get the tab context. If the group already holds a tab, reuse it; do not open another.
2. Otherwise create one new tab and navigate it to `i2_booking_url`.
3. Tell the coach, in these words: "Your i1 tab is open in Chrome. Drag it into its own window and leave that window visible on screen, not minimized. Don't close it or add tabs to it."
4. Why one tab in its own window: the Calendly booking page only loads while its tab is the front tab of a window that is showing. A lone tab is always the front tab.

The coach may put other apps in front of that window. Tested 2026-10-09: the page loaded and a day's time slots opened with the tab alone in its own window. Minimized was not tested, so the rule is "not minimized".

## Booking a person into the i2 (Calendly)

Do one person at a time.

1. Go straight to the slot. The address is `i2_booking_url`, then `/<YYYY-MM-DD>T<HH:MM>:00<UTC offset>`, then `?month=<YYYY-MM>&date=<YYYY-MM-DD>`. Use the UTC offset that applies on that date in the coach's `timezone` (it changes when the clocks change). For a 5:00 PM slot on October 6 in Toronto: `.../2026-10-06T17:00:00-04:00?month=2026-10&date=2026-10-06`.
2. Before filling anything, confirm the page shows the agreed day and time. If it shows a different slot or no form, do not book. Needs you.
3. Find the form fields. On the usual form they are Name, Email, Phone Number and "Send text messages to".
4. The form can arrive filled in with the last person booked from this browser. For every field: click it, select all, type the new value.
5. Read all the fields back from the page and compare them with the Calendly i1 booking. Fix any that differ.
6. Click Schedule Event once.
7. Wait 9 seconds, then check the page says "You are scheduled". If it still shows the form, wait and check again before clicking anything. Never click Schedule Event twice.
8. Calendly may ask for a code texted to the candidate's phone. Skip it by leaving the page. That person will not get Calendly's own text reminders; the phone's i2 reminder covers it.
9. If a robot check appears, stop this booking. It cannot be completed. List who is left.
10. If the slot is full or not offered, do not pick another slot. Put it on the "Needs you" list.

Booking usually moves the person's Recruitee stage to the i2 stage by itself. It can lag. Do not move it by hand. Check it once more at the end of this run and flag it if it has still not moved.

## Moving a no-show (Recruitee)

Moving someone to the no-show stage emails them a "we missed you" message straight away. Be sure before clicking.

1. Open search with cmd+k (ctrl+k on Windows). If nothing opens, press it a second time.
2. Type the person's name.
3. Open the result whose email matches the Calendly booking.
4. If the stage already shows `recruitee_no_show_stage`, stop: this person was moved already.
5. Click the blue stage button and choose `recruitee_no_show_stage`.
6. An automations box lists the tag and the email it will send. Click Continue.
7. Confirm the stage now shows the no-show stage.

Do not move:
- anyone who cancelled and holds another active i1 booking (they rescheduled);
- the second row of a duplicate booking;
- anyone the coach said to skip.

## Disqualifying a 3 (Recruitee)

Only for a person who showed and whom the coach called a 3. Never for a no-show, a 1 or a 2. Follow `permission_disqualify`: `granted` = do it, `ask` = list them and ask first, `never` = leave them for the coach.

1. Open the person's profile as above. The email must match the Calendly booking.
2. If the profile already shows as disqualified, stop: it was done already.
3. Click Disqualify.
4. Read the box before confirming. Choose the reason named in `disqualify_reason` (default `Not interested`).
5. If the box offers to email the candidate, leave that off unless the settings block says `disqualify_send_email: yes`.
6. Confirm, then check the profile shows as disqualified.

Do not disqualify, and put the person on the "Needs you" list, when: that reason is not on the list; the box is not as described here; or it is unclear on the recording whether the person is a 3.

## Adding a note for each 2 (Recruitee)

1. Open the person's profile as above.
2. Click "Add a note...", type one or two sentences: what holds them back, their i2 slot, and the call time.
3. Click Save and check for "Note added". If unsure, reload the profile and look for the note.

No personal characteristics in notes.

## Two profiles for one person

Use the profile whose email matches the booking. If both match, use the one tagged `recruitee_coach_tag`. If neither or both still fit, skip the person and put them on the "Needs you" list. Never touch an older profile from an earlier year.
