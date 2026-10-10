# Recruitee (Tellent) in the built-in browser

Used when the settings block says `recruitee_mode: builtin`. This is the Claude desktop app's built-in browser, with its pane closed, so the coach doesn't watch it work. The coach signed in to Tellent once in that browser; it keeps that sign-in. Use this instead of `browser.md`'s Chrome steps for Recruitee.

Never sign in for the coach. Never type a password, a code or a token. If Tellent shows a sign-in, a code or a robot check, stop that person's step and put them on "Needs you" with the reason. Tell the coach to open the browser pane to finish it.

## Before the first Recruitee step

1. Get the browser tabs in this chat. Claude uses one tab for Tellent and reuses it, same as `browser.md`'s "one tab" rule. Never open a second one.
2. Open `recruitee_site` (the candidates list, `https://app.tellent.com/ats/` in the settings block). If it shows a sign-in page, stop all Recruitee steps, say "Tellent is signed out in the built-in browser", and put everyone left on "Needs you".
3. If the page is the dashboard rather than the candidates list, open the candidates list from the app's navigation. Reading only.

## Finding a candidate

1. Use the candidates page's search box, and search the booking's email address (the one from the Calendly i1 booking). Never search by name alone.
2. Open the one result whose email matches exactly. Confirm the email on the profile before doing anything.
3. No match: Needs you, "no Tellent profile with the booking's email".
4. More than one profile holds that email: follow `rules.md`'s "two profiles" rule.
5. Read the candidate's stage and whether they're disqualified before any change. If it's already the target stage, or already disqualified, stop: it was done already.

Stage names in Tellent (use these exact names; they come from the settings block, not from memory): `recruitee_no_show_stage` (default `i1 No Show`), `i1 Scheduled`, `Not Interested`, `Pending Application`.

## Moving a no-show

Moving someone to the no-show stage can email them "we missed you" straight away. Be sure before clicking.

1. On the profile, use the stage control and choose `recruitee_no_show_stage`.
2. If an automation box appears (it lists the email that will be sent), read it. If it matches the no-show email, confirm it. If it doesn't, cancel and put the person on Needs you.
3. Check the profile now shows `recruitee_no_show_stage`.

Do not move: a cancelled person who holds another active i1 booking; the second row of a duplicate booking; anyone the coach said to skip.

## Disqualifying a 3

Only for someone who showed and whom the coach called a 3. Follow `permission_disqualify` exactly as in `browser.md`.

1. Open the profile (matched by email, as above). If it already shows as disqualified, stop.
2. Use the disqualify action and choose the reason in `disqualify_reason`. If that reason isn't offered, Needs you.
3. If the box offers to send an email, leave it off unless the settings block says `disqualify_send_email: yes`.
4. Confirm, then check the profile shows disqualified.

## Adding a note for each 2

1. On the profile, open the notes area and add one or two sentences: what holds them back, their i2 slot, the call time. No personal characteristics.
2. Save, then check the note appears on the profile.

## Limits

- Never click anything on a profile other than the one matched by email.
- Never send an email, message or text from Tellent.
- Never delete a candidate, a note or a stage history entry.
- Candidate names and emails stay in the session. Never write them to a file.
