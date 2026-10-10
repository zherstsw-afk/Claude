---
name: i1-controls
description: Stops, pauses, resumes and checks i1 delegation for a coach. Use when the coach says "pause i1", "stop the i1 automation", "resume i1", "hold the texts", "release the texts", "don't text" plus a person's name, "text them again", "stop the texts for my 2:00 session", "i1 status", "is i1 running", "restart the i1 planner", "open my i1 tab", "set up my i1 window", "change my i1 text wording", or "change an i1 setting".
---

# i1 controls

Short commands the coach gives in their i1 chat. Do exactly what is asked, confirm in one or two lines what changed, and say how to undo it.

Texts live as lines in entries on the coach's Texts calendar (`texts_calendar_id` in the `i1 settings` block). The phone sends an entry only at a timed run shortly after the entry's start time, so an entry parked at a time with no run is never sent.

## Stop one text

"Don't text <name>" or "take <name> off the 1:00 texts".

1. List the Texts entries from now to the end of tomorrow.
2. Remove that person's line from each entry it appears in (match on first name and, if two share it, ask which). Note their number.
3. Make it stick, because the overnight tasks rebuild the lists from the bookings: on each day from today until the day the coach names (default: the next 7 days), add their number to that day's `DO NOT TEXT` entry. That entry starts 11:20 PM and ends 11:35 PM, availability free, no reminders; its description is numbers only, one per line, no `|`. Create it if the day has none. Every text-writing task skips numbers on it.
4. Reply with which entries changed, their send times, and until when the person is blocked. Entries whose send time has passed cannot be changed; say so.

To undo ("text them again"): remove the number from the `DO NOT TEXT` entries. The next text-writing run puts the person back.

## Hold the texts for one session or one send time

"Hold the texts for my 2:00 session."

1. Find the entries for that session (the 1-hour and 10-minute entries, plus any qualification entry).
2. Park each one: prefix its title with `HELD (was <original start time>) ` and move its start to 11:20 PM the same day, ending 11:35 PM. Phone runs happen on the hour and at ten-to and look back 20 minutes, so an entry starting at twenty past is never sent. Do not change the lines.
3. Reply with what was parked.

The text-writing tasks leave a session alone while a `HELD` entry exists for it.

To release: only if the original start time is still at least 10 minutes away. List that day's entries first. If no other entry starts at the original minute, move the entry back and remove the prefix. If another entry now starts there, append the held lines to that entry (skipping any identical line), and retitle the parked one `MERGED (was <original start time>)` so it is not released twice. If the original time has passed, say it was missed and leave it parked.

## Pause everything

"Pause i1" or "stop the i1 automation".

1. Disable every scheduled task whose name starts with `i1:` (disable, never delete).
2. Park every Texts entry from now on, as above.
3. Reply with a count of tasks disabled and entries parked, and the reminder: "Your phone automations still run, but they have nothing to send. Say 'resume i1' to turn it back on."

While paused, do not run the after-session routine from a check-in. If one arrives, reply "i1 is paused" and stop.

## Resume

"Resume i1."

1. Enable the `i1:` scheduled tasks.
2. Release parked entries whose original time is still ahead. List any that were missed.
3. If no `i1: daily planner` reminder is pending, create it again (see "Restart the planner").
4. Reply with what is back on and what was missed.

## Status

"i1 status" or "is i1 running?"

Reply with a short table:

- each `i1:` scheduled task: on or off, last run, next run;
- whether an `i1: daily planner` reminder is pending;
- today's and tomorrow's Texts entries: title, send time, number of lines, and any that are HELD;
- how bookings and Recruitee run (`i2_booking_mode`, `recruitee_mode`);
- if `recruitee_mode` is `api`: run the Recruitee script's `check` (the after-session skill's `references/recruitee.md`) and say whether it passed;
- if `recruitee_mode` is `builtin`: say whether Tellent is signed in in the built-in browser (`references/recruitee-builtin-browser.md`);
- only if either mode is `browser`: whether the browser can be reached and Claude's tab group holds the i1 tab.

No names or phone numbers in the reply.

## Open the i1 tab

"Open my i1 tab" or "set up my i1 window." If `recruitee_mode` is `api` or `builtin`, and `i2_booking_mode` is `api` or `handoff`, say no Chrome tab is needed and stop. Otherwise follow "The i1 tab" in the after-session skill's `references/browser.md`: reuse the tab in Claude's tab group or open one, navigate it to `i2_booking_url`, and tell the coach to drag it into its own window and leave it visible, not minimized. Never open a second tab.

## Restart the planner

"Restart the i1 planner." The daily planner re-arms itself each morning; if a run was missed, the chain stops.

Create a one-off reminder into this chat named `i1: daily planner` for the next weekday at 8:22 AM, with the planner message from the setup skill's `references/task-prompts.md` and the full settings block. If today still has i1 sessions ahead, also run the planner's steps now.

## Change a setting or the wording

1. The settings and their allowed values are listed in the setup skill's `references/builder-sheet.md`. Show the current value and the new one, and ask the coach to confirm. A change to a permission line needs the coach's clear yes in the chat.
2. Update the `i1 settings` block, then update every `i1:` scheduled task's instructions in place so they carry the new value, including the pending planner reminder. Update, never delete and recreate.
3. If text wording changed, rewrite the lines in entries already queued for today and tomorrow.
4. Reply with what was updated.

## Switch off the API path

"Use the browser for Recruitee" or "use the browser for bookings": set `recruitee_mode` or `i2_booking_mode` to `browser` as in "Change a setting", and tell the coach the i1 tab and visible window are needed again. To stop Recruitee access completely, the coach deletes the "i1 Claude" token in Recruitee (Settings, Apps and plugins, Personal API tokens) and deletes `i1-recruitee.txt`.

## Limits

- Never delete a scheduled task or a calendar entry. Remove a line only when the coach asked for that person's text to stop.
- Never send anything. Changing an entry only changes what the phone will send.
- The coach can always stop a text by hand: open the entry in their calendar and delete the line.
