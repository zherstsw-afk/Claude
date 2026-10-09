# Setting up the i2 booking (for the i2 coach)

About 15 minutes, once. Everything runs in the cloud, so no computer needs to stay awake.

Say "set up i2 booking" to the Claude where you want this to run. Claude will walk through these steps one at a time.

## 1. Connect the two things it needs

- **Calendly.** Your own account, the one whose i2 event type the candidates book. Settings → Connectors → Calendly → sign in as yourself.
- **Google Sheets.** Your Google account must be able to open the shared tracking sheet. Ask the i1 coach to share it with your Google account (Editor access). Settings → Connectors → Google Sheets.

## 2. Tell Claude your settings

Claude asks for each one, and you paste them in the chat. Nothing else is needed.

| Setting | What it is | Where to get it |
|---|---|---|
| `i2_event_type_uri` | Your i2 event type | Claude finds it from your Calendly event types; confirm the name. |
| `timezone` | Your timezone | From Calendly; confirm. |
| `i2_host_first_name` | Your first name, as on the sheet's i2 host | Ask. |
| `sheet_id` | The shared tracking sheet | The i1 coach gives you the link; take the ID from it. |
| `handoff_first_column` | Where the handoff block starts on each week tab | The i1 coach's setup finds it and tells you the letter. |
| `week1_monday` | The Monday that Week 1 tab starts on | The i1 coach's setup finds it and tells you the date. |

## 3. Test it on one row

1. Ask the i1 coach to add one test row with Status `ready`: a test name, a test email with `+i2test` before the @ (on an address you can read), and a phone of +15555550100.
2. Ask Claude to run the booking now: "run the i2 booking".
3. Check: the row shows `booked`, the Booked at time is filled, and Email and Phone are cleared. Calendly shows the test invitee on your i2 slot.
4. Cancel that test booking in Calendly yourself (the cancel link in the confirmation email). Ask the i1 coach to delete the test row.

If the row shows `needs you`, the Note says why. Fix that one thing and run again.

## 4. Switch on the check, on i1 days only

Ask Claude to create a scheduled task named **"i2: book handoff rows"**, with the prompt in `task-prompt.md` and your settings pasted in. It runs only on the i1 days and in the hours after each i1 starts:

- **Days:** the i1 coach's `i1_days`, Monday to Friday numbers (Mon 1, Tue 2, Wed 3, Thu 4, Fri 5).
- **Hours:** from one hour after the earliest i1 start, to three hours after the latest, in the coach's timezone. For an i1 that starts at 1:00 PM on Tuesday and Thursday, that's 2:00 PM to 4:00 PM.
- **Schedule:** `CRON_TZ=<timezone> 0 <first hour>-<last hour> * * <days>`. For the example above, `CRON_TZ=America/New_York 0 14-16 * * 2,4`.

Rows are written about 40 to 60 minutes after an i1 starts, so the first run catches them within the hour. If the i1 times change, update this task's schedule too; the i1 coach's Claude will remind them when they change `i1_days` or `i1_start_hours`.

Each run that finds nothing to book stops after one read, so these runs stay cheap.

## 5. What to watch

- Every hour the task runs, a short report. `needs you` rows are the ones that need you: a slot was full, a question was unanswered, or Calendly refused.
- If Calendly refuses the bookings, the task stops and reports it. That means your access changed.
- If a run says "no i2 handoffs" most times, that's normal: it's the early exit working.
