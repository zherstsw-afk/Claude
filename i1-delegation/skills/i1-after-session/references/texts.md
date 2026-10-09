# Texts

Claude never sends a text. It writes lines into the coach's private "Texts" Google calendar (`texts_calendar_id`). The coach's phone auto-sends them on a timer.

## How the phone reads the calendar

- The phone runs **on the hour** and at **ten to the hour**. Each run sends ONE entry: the one that started most recently in the last 20 minutes.
- A run on the hour sends the entry that starts at **:58**.
- A run at ten-to sends the entry that starts at **:35**. It must not start later than :39, or the run on the hour would send it a second time.
- Each line of the entry's description is one text: `<number>|<message>`.
- This only works for sessions that start on the hour. For any other start time, write nothing and report it.

## Entry rules

1. List the day's entries on the Texts calendar before writing.
2. **Never two entries at the same start minute.** If an entry already starts at the minute needed, append the new lines to the end of its description and keep every line already there.
3. **Never add a line identical to one already in the entry.**
4. Create a new entry only when none starts at that minute: start :58, end :15 of the next hour, availability free, no reminders, no guests, notification level none.
5. Numbers are `+1` followed by ten digits, no spaces. A number that cannot be made into that form gets no text; flag it.
6. Lines are separated by a single newline. Plain text. The only `|` on a line is the one after the number.
7. Replace every `<...>` token in the wording with the real value. If a token cannot be filled, leave that person out and flag it. A line must never reach the calendar with a `<` in it.
8. Never delete an entry or a line that another run wrote.
9. End each batch with one line to the coach's own number (`coach_mobile`) saying what was sent, for example `<coach_mobile>|Sent: qualification call texts for your 1:00 session (3 people).`

## Holds and do-not-text

Before writing any line, look at the day's entries for these two markers. Both sit at 11:20 PM, where no run can send them.

- An entry titled `DO NOT TEXT`: its description lists numbers, one per line. Never write a line for a number on that list.
- An entry whose title starts with `HELD`: the coach is holding the texts for that session. Write nothing for that session and say so.

## Wording

Use the wording in the settings block. These are the defaults.

| Setting key | When it sends | Default wording |
|---|---|---|
| `text_1_hour` | 1 hour before the i1 | `Hey <first>, it's <coach_first_name> from <program_name>. Thrilled to see you coming to the info session at <session time> today!` |
| `text_10_min` | 10 minutes before the i1 | `Hey <first>, we're starting in 10. The Zoom link is in your confirmation email in case you missed it, see you soon.` |
| `text_qualification` | First run on the hour after the session | `Hey <first>, great having you on the call today! I'll give you a ring <today at H:MM / tomorrow at H:MM PM / <weekday> at H:MM PM> for a quick chat before your next session (<Day> at <time>). Timing can shift a bit so keep your phone close, and please have the questionnaire done before I call.` |
| `text_call_reminder` | Day of the call (later-day calls only) | `Hey <first>, it's <coach_first_name>. I'll be calling you at <H:MM> today for our quick chat, talk soon!` |
| `text_i2_reminder` | 1 hour before the i2 | `Hey <first>, it's <coach_first_name>! Just a friendly reminder your next session with <i2_host_first_name> is at <start time> today, about an hour from now. Make sure to join early, we'll see you then!` |

The first two and the last are written by scheduled tasks, not by this routine. This routine writes the qualification text and the call reminder.

## Where the qualification text goes

Default (`qualification_text_when: after_session`):

- In the entry that starts 58 minutes after the session start; it sends one hour after the session start.
- If it is already more than 48 minutes past the session start, use the entry one hour later and say so.
- If the call time is at or before the time the text would send, write no text for that person and flag it.

Set hour (`qualification_text_when` is a whole hour such as `18:00`):

- Use the entry that starts at :58 before the first occurrence of that hour after the session ends. If the hour has already passed today, that is the same hour tomorrow.
- Work this out per person. If that send time is not at least 20 minutes before the person's call, send theirs the default way (right after the session) instead.
- When the text sends on a later day than the session, reword the opening so it still reads true: "great having you on the call yesterday" in place of "today", and work out "today" or "tomorrow" for the call from the day the text sends.

How the call time is written (`call_time_style`):

- `exact` (default): "today at 4:35", "tomorrow at 6:00 PM", "Thursday at 12:30 PM".
- `part_of_day`: "this afternoon", "tomorrow evening", "Thursday morning". Morning is before noon, afternoon is noon to 5:00 PM, evening is after 5:00 PM.

## Where the call reminder goes

- `call_reminder: off`: write none.
- Only for a call on a later day than the i1.
- `call_reminder` is a whole hour such as `09:00`: it goes in the entry that starts at :58 before that hour on the day of the call. If that hour is not at least 20 minutes before the call, use the default below.
- Default (`hour_before`): it goes in the entry that starts at :58 before the last on-the-hour run that is at least 20 minutes before the call. A 4:35 call uses the 3:58 entry. A 4:00 call uses the 2:58 entry. A 12:30 call uses the 11:58 entry.
- Entry title when created: `Call reminder texts (<n>)`.
- If that send time has already passed, or the coach has no run that early in the day, skip it and say so.

## Wording rules

- Human, short, first name only.
- Never say "pop it in your calendar".
- Do not change the coach's wording. If a template is missing from the settings, use the default above and say so in the report.
