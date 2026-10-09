# Scheduled tasks to create

Fill every `{placeholder}` from the settings block before creating a task. Each task runs with no memory of this chat, so its prompt must be complete on its own. Paste the full `i1 settings` block where a template says `{settings_block}`.

Use the coach's timezone in every schedule. Avoid exact hours and half hours; the times below are already offset.

| # | Name | Kind | When |
|---|---|---|---|
| 1 | `i1: write tomorrow's texts` | Recurring cloud task | 9:05 PM on the evening before each day the coach hosts i1s |
| 2 | `i1: refresh today's texts` | Recurring cloud task | 8:15 AM on each day the coach hosts i1s (earlier if a session starts before 10:00 AM: 90 minutes before the earliest session hour) |
| 3 | `i1: write today's i2 reminder texts` | Recurring cloud task | 8:10 AM and 1:10 PM, Monday to Friday |
| 4 | `i1: weekly sheet setup` | Recurring cloud task, phone notification on | Sunday 2:45 PM |
| 5 | `i1: end-of-day check` | Recurring cloud task, phone notification on | Monday to Friday, 105 minutes after the coach's latest session start hour (5:45 PM for a latest start of 4:00 PM) |
| 6 | `i1: daily planner` | Check-in into the i1 chat; re-arms itself | Next weekday 8:22 AM |
| 7 | `i1: weekly i2 times` (optional) | Check-in into the i1 chat; re-arms itself | Next Sunday 8:00 PM |

Create tasks 1, 2 and 3 only if `permission_texts` is `granted`. Skip task 3 when `send_i2_reminder` is `no`, task 4 when `weekly_sheet_setup` is `no`, and task 7 when `i2_times_by` is `i2_coach`. Skip tasks 1 and 2 when both `send_1_hour_text` and `send_10_min_text` are `no`.

Tasks 6 and 7 are created as one-off reminders into the i1 chat, because only that chat can reach the coach's Chrome. A recurring task cannot be tied to a chat, so each run schedules the next one.

Task 7 follows `i2_times_by`. If that setting was never asked, ask the coach before creating it: "Does someone else fill in the week's i2 times on your sheet?" Create it only if the answer is no.

---

## 1. i1: write tomorrow's texts

```
Write TOMORROW's reminder-text entries for {coach_full_name}'s i1 information sessions. The coach hosts "i1" group Zoom sessions booked through Calendly. Their phone has timed automations, on the hour and at ten to the hour, that read a private Google calendar called "Texts" and send each line of one entry as a text from their own number. Your job is only to write tomorrow's entries on that calendar. You send nothing yourself. Nobody is watching this run: do not ask questions.

{settings_block}

0. PERMISSION. If the settings block above does not contain "permission_texts: granted", write nothing and report that.

1. FIND TOMORROW'S SESSIONS. Calendly: get the current user, then list ACTIVE scheduled events for that user for tomorrow (00:00 to 23:59 in the coach's timezone) named "{i1_event_name}". None: create nothing and report "no i1 sessions tomorrow". A session that does not start exactly on the hour cannot be served by the phone's timer: write nothing for it and report it.

2. WHO IS BOOKED. For each session, list invitees with status active only. For each person take the first word of their name as the first name, and the answer to the phone-number question. Normalise the number to +1 followed by ten digits. A number that cannot be made into that form: leave the person out and report it. The same number twice in one session: one line, not two.

3. HOLDS. List tomorrow's events on the Google calendar with ID {texts_calendar_id}. If one is titled "DO NOT TEXT", its description lists numbers, one per line: never write a line for a number on it. If one has a title starting "HELD" for a session, write nothing for that session and report it.

4. WRITE TWO ENTRIES PER SESSION on that calendar (availability free, no reminders, notification level none, no guests). <session time> is written like "11:00 AM".
   - Title "i1 <session time> - 1 hour text (<number of people>)". Starts 62 minutes before the session, ends 45 minutes before. One line per person: <number>|{text_1_hour}
   - Title "i1 <session time> - 10 minute text (<number of people>)". Starts 25 minutes before the session, ends at the session start. One line per person: <number>|{text_10_min}
   If the settings block says "send_1_hour_text: no", do not write the 1-hour entry. If it says "send_10_min_text: no", do not write the 10-minute entry.
   In each line replace every <...> token with the real value (first name, session time). If a token cannot be filled, leave that person out and report it; no line may contain "<". Lines are separated by a single newline. The only "|" on a line is the one after the number. Plain text.
   The 10-minute entry must start 25 minutes before, not later: an entry that starts within 20 minutes of the hour would be sent a second time by the on-the-hour run.

5. ONE ENTRY PER SEND TIME. An entry with the same title start already exists: update its i1 reminder lines and its title to match current bookings, and keep any other lines in it. A different entry already starts at the exact minute needed: append to the end of its description and keep every line there. Never add a line identical to one already in the entry. Never delete an entry. A session was cancelled and its entries exist: remove only its i1 reminder lines and report it.

6. PRIVACY. Do not write names or phone numbers into any file. Do not repeat phone numbers in the report.

7. REPORT, short: tomorrow's date; one line per session with the time, how many people and the two send times; anyone left out and why. Do not send, draft or post anything. Do not change any Calendly booking or any other calendar.
```

## 2. i1: refresh today's texts

The same prompt as task 1 with these changes: replace "TOMORROW" and "tomorrow" with "TODAY" and "today" throughout, and add this line after step 1:

```
Only touch an entry whose start time is at least 20 minutes from now. Leave any entry that has already started or starts sooner exactly as it is.
```

This picks up people who booked or cancelled after the evening run.

## 3. i1: write today's i2 reminder texts

```
Write TODAY's "one hour before the i2" reminder texts for {coach_full_name}. People the coach has qualified attend an "i2" session hosted by {i2_host_first_name}. The coach's phone has timed automations, on the hour, that read a private Google calendar called "Texts" and send each line of one entry as a text from their own number. Your job is only to write today's i2 entries on that calendar. You send nothing yourself. Nobody is watching this run: do not ask questions.

{settings_block}

0. PERMISSION. If the settings block above does not contain "permission_texts: granted", write nothing and report that.

1. FIND TODAY'S i2 SESSIONS on the tracking sheet (Google Sheets ID {sheet_id}). The tab is "Week N": Week 1 starts Monday {week1_monday} and each week adds one. Read I1:T70. It holds i2 blocks stacked down the page. Each block starts with a header row with "Date" in column I and in column P, the day in J and Q, and the start time in L and S. The next row is the titles (Name, Qual.?, Show?, Appl.?, Deadline). The eight rows after that hold people: a left group (name in I, Qual.? in J) and a right group (name in P, Qual.? in Q). Keep the blocks whose day is today. None: create nothing and report "no i2 today". An i2 that does not start exactly on the hour: write nothing for it and report it.

2. WHO GETS A TEXT: every named person in today's blocks, either group, whose Qual.? box is TRUE. Nobody qualified yet for a session: write nothing for it and say so (a later run today picks up people qualified since).

3. PHONE NUMBERS come from Calendly: get the current user, list that user's scheduled events named "{i1_event_name}" from 14 days ago through today, list their invitees, and match each qualified person by full name (ignore case; accept a one-letter spelling difference only if exactly one invitee fits). Use the phone-number answer, normalised to +1 and ten digits. No confident match: leave the person out and report the name.

4. HOLDS. List today's events on the Google calendar with ID {texts_calendar_id}. If one is titled "DO NOT TEXT", never write a line for a number listed in its description. If one has a title starting "HELD" for this i2, write nothing for that i2 and report it.

5. WRITE ONE ENTRY PER SESSION on that calendar. It starts 62 minutes before the i2 and ends 45 minutes before; availability free, no reminders, notification level none, no guests. Title "i2 <start time> - 1 hour text (<number of people>)". One line per person: <number>|{text_i2_reminder}
Replace every <...> token with the real value; no line may contain "<". Then one last line: {coach_mobile}|Sent: i2 reminder texts for <start time> (<number of people> people).

6. ONE ENTRY PER SEND TIME. An entry titled "i2 <start time> - 1 hour text" exists: update only its i2 reminder lines to match the current qualified list and keep every other line in it. A different entry starts at that exact minute: append to it and keep every line there. Never add a line identical to one already in the entry. Never delete an entry or a line someone else wrote. The send time has passed: write nothing for that session and say so.

7. PRIVACY: no names or phone numbers in any file; no phone numbers in the report.

8. REPORT, short: today's date; one line per i2 session with its time, how many get the text and the send time; anyone left out and why. Do not send, draft or post anything. Do not change the sheet, any Calendly booking or any other calendar.
```

## 4. i1: weekly sheet setup

```
Set up {coach_full_name}'s i1 session blocks for the coming week in the recruiting tracking sheet. Nobody is watching this run: do not ask questions, make the safe choice and report.

{settings_block}

THE SHEET. Google Sheet ID {sheet_id}. Other people use it, so write only the cells named below. One tab per week, "Week N": Week 1 is the week of Monday {week1_monday}, +7 days each. Work out the tab for the COMING Monday. If it does not exist, write nothing and report it. On a week tab, i1 blocks are stacked in columns A to F, 15 rows apart; header rows are 2, 17, 32, 47 and so on. On a header row, column B reads "Meeting Timeslot" or "Date", column C holds the session date and time, column E reads "Host", column F holds the host name. Column C must be a NUMBER (a date serial: whole days since 1899-12-30, plus hour/24, plus minute/1440, in the coach's local time), not text. Column F must be exactly: {coach_full_name}

STEP 1. FIND THE SESSIONS for the coming Monday 00:00 to Sunday 23:59. Calendly: get the current user and list active scheduled events named "{i1_event_name}" in that range. Some coaches also block planned slots on their main Google calendar with events titled exactly "I1": include those too, since a slot with no bookings yet has no Calendly event. The session list is the union, one entry per distinct start time. Nothing found: write nothing and report "no i1 sessions found".

STEP 2. READ THE TAB FIRST (A1:F320). A session is ALREADY IN if a header row has the coach's name and the same date and time: skip it. A block is FREE only if its header C and F are both empty and nothing is filled in beneath it. Never write into, clear or change a block that is not free. If the header rows are not where described, stop, write nothing and report that the layout is different.

STEP 3. WRITE. For each session not already in, in time order, take the next free block from the top and write its header row only: range "<tab>!C<row>:F<row>", values [[<serial number>, null, null, "{coach_full_name}"]]. Write nothing else. Never insert, delete, move, clear, colour or sort. Not enough free blocks: write what fits and report the rest.

STEP 4. CHECK. Read the blocks back and confirm each header shows the right date, time and host.

REPORT (short, no candidate names): tab used; one line per session with day, time and header row, or "already in"; anything skipped or unexpected. Do not send, draft or post anything. Do not change any calendar or Calendly event.
```

## 5. i1: end-of-day check

```
End-of-day check on {coach_full_name}'s i1 delegation. Nobody is watching this run: do not ask questions. This run only reads, except for the one alert entry described in step 4.

{settings_block}

1. TODAY'S SESSIONS. Calendly: get the current user and list ACTIVE scheduled events for today named "{i1_event_name}" that started at least 70 minutes ago. Any that started more recently: name them in the report as "too recent to check". None at all: go to step 3.

2. WAS EACH ONE PROCESSED? Open Google Sheet {sheet_id}, tab "Week N" (Week 1 is the week of Monday {week1_monday}). Find each session's block: the header row (rows 2, 17, 32 and so on) with the session's date and time in column C and "{coach_full_name}" in column F; 12 name rows start two rows below. A session is PROCESSED if any name row has Show? TRUE, a Conversion, or a Note. If a block has names but none of those, it is NOT PROCESSED. If no block matches the session, it is MISSING.

3. IS THE PLANNER ARMED? List the scheduled tasks. There should be a pending task named "i1: daily planner" for a later date. If not, the chain has stopped.

4. ALERT only if something is wrong (a session NOT PROCESSED or MISSING, or the planner not armed). Start the report with "ALERT:" and one line per problem, each with what the coach should do: for a session, "open your i1 chat and say: run the i1 routine for my <time> session"; for the planner, "open your i1 chat and say: restart the i1 planner". Also queue ONE text to the coach's own phone on the Google calendar {texts_calendar_id}: take the next time ending in :58 that is at least 10 minutes from now; list today's entries; if one already starts at that minute, append the line below to the end of its description and keep every line there; otherwise create "i1 alert" starting at that minute and ending 17 minutes later (availability free, no reminders, notification level none). The line: {coach_mobile}|i1 alert: <the problems in under 120 characters, no candidate names>

5. Nothing wrong: report "All clear" and one line per session. No candidate names and no phone numbers in the report.
```

## 6. i1: daily planner (check-in into the i1 chat)

Create with a one-off reminder into this chat for the next weekday at 8:22 AM. Message:

```
i1: daily planner (runs each weekday morning and re-arms itself). Do this without asking the coach.

{settings_block}

0. RE-ARM FIRST, before anything else, so one bad day does not stop the chain: list the scheduled tasks. If no task named "i1: daily planner" is pending for a later date, create a one-off reminder into this chat, name "i1: daily planner", for the next weekday at 8:22 AM in the coach's timezone, with this whole message unchanged, settings block included.

1. If the coach has said "pause i1" and not "resume i1" since, reply "i1 is paused" and stop.

2. Calendly: get the current user and list ACTIVE scheduled events for today named "{i1_event_name}". None: reply "No i1 sessions today." and stop.

3. For each of today's sessions that does not already have a pending task named "i1: after-session <start time>" due today, create a one-off reminder into this chat for 40 minutes after the session start, with that name and this message: "Scheduled check-in: the <start time> i1 session on <date> should be over. Run the i1-after-session routine for it, end to end. Calendly event: <event URI>. Session start: <date and time>." followed by the full i1 settings block.

4. OPEN THE i1 TAB. Get the Chrome tab context. If Claude's tab group already holds a tab, reuse it and navigate it to {i2_booking_url}; never open a second one. If it holds none, create ONE new tab and navigate it to {i2_booking_url}. Then tell the coach, as the first line of the reply: "Your i1 tab is open in Chrome. Drag it into its own window and leave that window visible on screen, not minimized. Don't close it or add tabs to it." Claude uses that one tab for both Calendly and Recruitee, one at a time. If the browser cannot be reached, say so in the reply and, if a phone-notification tool is available, send ONE notification: "i1: Chrome link is down. Bookings and Recruitee moves will not run until it is back."

5. Reply with at most one line per session: start time, people booked, when its check-in runs. No names, no phone numbers.
```

A session booked after 8:22 AM on the day has no check-in. The end-of-day check reports it; the coach says "run the i1 routine for my <time> session".

## 7. i1: weekly i2 times (optional; check-in into the i1 chat)

Only create this if nobody else fills in the week's i2 times on the coach's sheet. Create with a one-off reminder into this chat for the next Sunday at 8:00 PM. Message:

```
i1: weekly i2 times (runs each Sunday evening and re-arms itself). Set up the coming week's i2 times on the sheet without asking the coach.

{settings_block}

0. RE-ARM FIRST: if no task named "i1: weekly i2 times" is pending for a later date, create a one-off reminder into this chat, same name, for the following Sunday at 8:00 PM in the coach's timezone, with this whole message unchanged.

1. READ THE i2 TIMES in Chrome, in ONE tab: reuse the tab in Claude's tab group if there is one, otherwise create one; never open a second. For each weekday of the coming week, navigate that tab to {i2_booking_url}?month=<YYYY-MM>&date=<YYYY-MM-DD>, wait 3 seconds, read the page text, and take the times listed under that day. The page only loads while its tab is visible. If the browser cannot be reached, or no day shows a time, create ONE retry of this check-in for Monday 8:30 AM, tell the coach in one line, and stop.

2. SHEET {sheet_id}, the coming week's tab. Read I1:T70. SAFETY FIRST: if any person's name is already entered under any i2 block in that tab, or any block header already has a day and time, someone else has set the week up: write nothing in the i2 area and report what is there. Otherwise match the format of last week's i2 block header rows exactly (day as text such as "Tues", time as a time value) and write one block per i2 session in date order, the same day and time in both the left group (J, L) and the right group (Q, S). Never touch name rows. Never clear a cell. Never insert or delete rows.

3. DROPDOWN: on each of the coach's i1 blocks in that tab (header rows where column F is "{coach_full_name}"; 12 name rows start two rows below), set column E to a non-strict list of the week's slots written like "Tues 5:00 PM", plus "Find a time". Use the slots that are on the sheet after step 2, whoever wrote them.

4. Report in a few lines: the i2 slots found, what was written, anything missing.
```
