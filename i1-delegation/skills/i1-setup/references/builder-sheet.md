# The builder sheet

The builder sheet is a page the coach fills in before their trial. Each row is one question, with a "Zander's way" column (the default) and a "Your way" column (older copies call these "Default" and "Your choice"). A filled sheet becomes the `i1 settings` block.

## Reading a filled sheet

1. The coach pastes the sheet (or its text) into the chat. Read every row.
2. A blank "Your way" cell means the default. The coach may answer in their own words; map each answer to the allowed value it clearly means.
3. The sheet writes the blanks in texts as `[square brackets]`. Convert them to the tokens the routine uses: `[first name]` to `<first>`, `[your first name]` to the coach's actual first name, `[program]` to the program name, `[session time]` to `<session time>`, `[call day and time]` to `<call day and time>`, `[i2 day and time]` to `<i2 day and time>`, `[call time]` to `<H:MM>`, `[i2 coach]` to the i2 coach's first name, `[i2 time]` to `<start time>`.
4. If a choice is unclear or is not one of the allowed values, ask about that row only.
5. Repeat the choices back as a short table of the rows that differ from the default, then the full settings block, and ask the coach to confirm.
6. If the coach has no sheet, ask the same rows in the chat, a section at a time, offering the default for each.

Tell the coach once: only the default setup has run on live sessions. Each changed choice is new, so they should watch it on their first session.

## Rows, keys and allowed values

A key that is missing from a settings block always means its default.

### About you

| Row | Key | Default | Allowed |
|---|---|---|---|
| Full name as Host on the sheet | `coach_full_name` | none | text |
| First name in texts | `coach_first_name` | none | text |
| Mobile number | `coach_mobile` | none | +1 and ten digits |
| Program name | `program_name` | `the Management Program` | text |

### Sessions and links

| Row | Key | Default | Allowed |
|---|---|---|---|
| i1 days | `i1_days` | none, FILL IN | weekdays |
| i1 start hours | `i1_start_hours` | none, FILL IN | whole hours only. Ask as two questions: "What is the earliest time any of your i1s starts?" and "What is the latest time any of your i1s starts?" Across the whole week, not per day. Example to give: earliest 10:00 AM (a Wednesday), latest 3:00 PM (a Tuesday) gives `10:00-15:00`. |
| i1 event name in Calendly | `i1_event_name` | `Management Program i1 Information Session` | text; confirm against the coach's Calendly event types |
| Call hours | `call_hours` | `12:00-21:00` | earliest and latest hour |
| Tracking sheet link | `sheet_id` | none | take the ID from the link |
| (not on the form) | `week1_monday` | read from the sheet | the Monday of the first date on the "Week 1" tab; Claude fills this in, the coach is not asked |
| i2 booking link | `i2_booking_url` | none | a Calendly link |
| i2 coach's first name | `i2_host_first_name` | none | text |
| Who enters the i2 times | `i2_times_by` | `claude` | `claude` or `i2_coach` |

### Texts

| Row | Key | Default | Allowed |
|---|---|---|---|
| 1 hour before the i1 | `send_1_hour_text` | `yes` | `yes`, `no` |
| Its wording | `text_1_hour` | see the after-session skill's `references/texts.md` | text |
| 10 minutes before the i1 | `send_10_min_text` | `yes` | `yes`, `no` |
| Its wording | `text_10_min` | as above | text |
| When the qualification call text sends | `qualification_text_when` | `after_session` | `after_session`, or a whole hour such as `18:00` |
| How the call time is written | `call_time_style` | `exact` | `exact`, `part_of_day` |
| Its wording | `text_qualification` | as above | text |
| Reminder on the day of the call | `call_reminder` | `hour_before` | `off`, `hour_before`, or a whole hour such as `09:00` |
| Its wording | `text_call_reminder` | as above | text |
| 1 hour before the i2 | `send_i2_reminder` | `yes` | `yes`, `no` |
| Its wording | `text_i2_reminder` | as above | text |

A coach who says "morning", "afternoon" or "evening" without an hour: ask which hour. Texts only send on the hour.

### How the sheet gets filled

| Row | Key | Default | Allowed |
|---|---|---|---|
| Notes | `notes_style` | `words` | `words` (one or two), `sentence`, `none` |
| Where the call time is written | `call_time_location` | `deadline` | `deadline`, `notes`, `nowhere` |
| Colour the rows | `colour_rows` | `yes` | `yes`, `no` |
| Add 1s and 2s to the i2 block | `add_to_i2_block` | `yes` | `yes`, `no` |
| Enter next week's sessions each Sunday | `weekly_sheet_setup` | `yes` | `yes`, `no` |

### After the session

| Row | Key | Default | Allowed |
|---|---|---|---|
| Qualification call day | `call_day_rule` | `day_before_i2` | `day_before_i2`, `as_said` |
| Calls on the calendar | `calendar_events` | `yes` | `yes`, `no` |
| Book 1s and 2s into the i2 | `permission_bookings` | see step 4 of setup | `granted <date>`, `ask`, `never` |
| Move no-shows in Recruitee | `permission_no_show_moves` | see step 4 of setup | `granted <date>`, `ask`, `never` |
| Queue texts to candidates | `permission_texts` | see step 4 of setup | `granted <date>`, `never` |
| Disqualify 3s in Recruitee | `permission_disqualify` | see step 4 of setup | `granted <date>`, `ask`, `never` |
| Reason chosen when disqualifying a 3 | `disqualify_reason` | `Not interested` | a reason on the coach's Recruitee list |
| Email a 3 when disqualifying | `disqualify_send_email` | `no` | `yes`, `no` |
| Cancelled booking | `cancelled_booking` | `no_show` | `no_show`, `leave` |
| Recruitee note for each 2 | `recruitee_notes_for_2s` | `yes` | `yes`, `no` |

### Without a browser (not on the form; setup fills these in)

| Row | Key | Default | Allowed |
|---|---|---|---|
| How Recruitee steps run | `recruitee_mode` | `browser` | `builtin` once setup's Part A2 passes (Tellent, built-in browser, pane closed); `api` once setup's Recruitee key test passes; else `browser` |
| Recruitee site (builtin mode) | `recruitee_site` | `https://app.tellent.com/ats/` | the candidates page; set during Part A2 |
| Where the Recruitee key file is | `recruitee_key_file` | none | the path of `i1-recruitee.txt` in the folder connected to the i1 chat |
| How i2 bookings run | `i2_booking_mode` | `browser` | `handoff` (the i2 coach's Claude books from the sheet, preferred), `api` once setup's Calendly test passes, else `browser` |
| Where the handoff block starts | `handoff_first_column` | none | the column letter found in setup, Part B; needed for `handoff` only |
| The i2 event type | `i2_event_type_uri` | none | the event type's API reference, found in setup |

The four permission rows are never taken from the sheet alone. "Without asking" on the sheet becomes `granted` only after the coach confirms it in the chat, in step 4 of setup.

## What each choice changes

- `send_1_hour_text`, `send_10_min_text`: the text-writing tasks skip that entry.
- `send_i2_reminder: no`: do not create the i2 reminder task.
- `weekly_sheet_setup: no`: do not create the weekly sheet setup task.
- `i2_times_by: i2_coach`: do not create the weekly i2 times check-in.
- `i1_days`, `i1_start_hours`, `call_hours`: decide which evenings and mornings the text-writing tasks run, which phone automations the coach needs, and when the end-of-day check runs.
- `recruitee_mode` and `i2_booking_mode`: when both are `api`, the daily planner opens no browser tab and the coach has no window to keep visible.
- Everything else is read by the after-session routine each time it runs.
