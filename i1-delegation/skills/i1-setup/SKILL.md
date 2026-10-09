---
name: i1-setup
description: Sets up i1 delegation for a Student Works coach - collects their settings, checks each connection, tests the phone texting, and creates the scheduled tasks. Use when the coach says "set up i1 delegation", "set up my i1 automation", "install the i1 workflow", "get me started with i1 delegation", or when another i1 skill reports that the settings are missing.
---

# i1 delegation setup

## How to talk to the coach

Assume the coach is new to Claude and busy. Long messages make people quit.

- **Language first.** If the coach has not already chosen, the first message is just: "English or français?" Then every message, the settings form's labels, the test texts to their own number and the certificate use that language. Settings keys and the text wordings the coach sends to candidates stay as the coach writes them. Some coaches are francophone; never assume English.

- **One instruction per message.** Then stop and wait for "done" (or a screenshot).
- **Three short lines at most.** No paragraphs, no background, no "why" unless they ask.
- **Say exactly what to tap or click**, in order: "Open Zoom. Tap Settings. Tap Recording."
- **Plain words.** No tool names, file paths, settings keys or jargon. Say "your Texts calendar", not `texts_calendar_id`. On the phone steps say "Apple Calendar" for the iPhone's built-in app, never just "Calendar": coaches hear that as Google Calendar.
- **Check it yourself when you can**, and say "Works." in one line. Only explain when something fails.
- **When something fails**, give the single most likely fix in one line, then ask for a screenshot.
- **Show progress** at the start of each step as a Part number that matches the coach's helper prompt (`references/helper-prompt.md`): settings = "Part 4 of 7", phone texting = "Part 5 of 7", go-ahead and scheduled tasks = "Part 6 of 7", dry run and hand over = "Part 7 of 7".
- Questions: one at a time, with the default offered ("Keep 'the Management Program'? Yes / change it").

First message after the language is known, if the coach has not said which Part they are at: "Hi! I'll set this up with you one small step at a time. About two hours in all, and you can stop and pick up later. If anything breaks later, you just do it by hand like now. Ready?" If they arrive saying "I'm at Part 4" (they came from the helper prompt), skip the greeting: check step 1 silently, mention only what is missing, and go straight to Part 4.

This must be a Cowork chat in the Claude desktop app. Before anything else, check that scheduled tasks can be created here. If not, tell the coach in one line to open the Cowork tab of the desktop app and start the chat there.

The steps below are for you. Never paste them to the coach as written; turn each into short single instructions.

Do every step in the one chat the coach will keep for i1 delegation (their "i1 chat"). The after-session check-ins arrive in this chat, so it must stay open in their account.

## Step 1. Check what is connected

Check, without asking, whether this chat can reach: Google Sheets, Google Calendar, Calendly and Zoom. Chrome is checked later, only if step 1b leaves a step in browser mode. Google Drive is not needed; do not ask the coach to connect it (it is also temporarily unavailable on Student Works accounts). Show one line per item: "Connected" or "Missing". Then fix the missing items one at a time: give the taps to connect it, wait for "done", check again. If a step stays in browser mode after step 1b: Chrome needs the Claude extension installed in the browser where the coach is signed in to Recruitee. The i2 booking page is public, so no Calendly sign-in is needed in Chrome.

Zoom needs one account setting the coach switches on themselves (Claude cannot change it): on zoom.us/profile/setting, the **AI Companion** tab, set **Meeting summary** to start automatically. That is what produces the transcript Claude reads. Cloud recording is optional; if the coach has it, turning on **Automatic recording, In the cloud** under the Recording tab is a backup, but it is not needed. Zoom recording to the computer or iCloud does not help, because Claude cannot read local files.

**Test:** read the coach's Calendly user and list today's calendar events. For Zoom, have the coach start a meeting alone, talk for about two minutes, and end it; after about 10 minutes, find that meeting and read a line of its transcript back to them (by meeting UUID, types "transcript"; do not look only in cloud recordings). Report pass or fail for each.

## Step 1b. No browser: Recruitee and the i2 bookings

Goal: `recruitee_mode: api` and `i2_booking_mode: api`, so nothing needs a Chrome window. Follow `references/no-browser-setup.md`. The coach's part takes under 10 minutes. The i2 bookings also need one thing from the i2 coach, which can happen later. Until it does, bookings stay in browser mode.

Whatever is still in browser mode at the end of this step needs the Chrome check from step 1 and the i1 tab test: open the i1 tab (the after-session skill's `references/browser.md`, "The i1 tab"), have the coach drag it into its own window, then check the Calendly page shows days and times.

## Step 2. Collect the settings

Do not ask whether the coach has a builder sheet. Give them one to fill in, right in the chat, in one message:

1. Say: "Here's your settings form. Copy it, change anything you want, leave the rest, and paste it back. Lines marked FILL IN are the only ones you must do." Then post the form as a plain code block so it copies cleanly: one `key: value` line per row of `references/builder-sheet.md`, in that order, with the default already filled in and a short plain-English label after a `#` (for example `program_name: the Management Program   # what you call the program in texts`). Rows with no default show `FILL IN`: full name, first name, mobile, tracking sheet link, i1 days, earliest i1 start time, latest i1 start time, call hours, latest i2 hour, i2 booking link, i2 coach's first name. These are never prefilled, not even as an example, so nobody ends up with Zander's number or sheet. The earliest and latest i1 start are two separate lines, with the note "across your whole week, e.g. earliest 10:00 AM on Wednesday, latest 3:00 PM on Tuesday". Text wordings show the full default text so the coach can reword it.
2. When they paste it back, read it as `references/builder-sheet.md` describes. Ask only about a line that is still `FILL IN`, blank, or not an allowed value, one question per message.
3. If they paste a filled builder sheet from the page instead, read that the same way.

The table below is the core every setup needs. `references/builder-sheet.md` holds the full list of options. Ask for what cannot be found, one question per message with the default offered. Find the rest and ask the coach to confirm it.

| Setting | How to get it |
|---|---|
| `coach_full_name` | Ask. It must match the Host name used on the tracking sheet. |
| `coach_first_name` | From the full name; confirm. |
| `coach_mobile` | Ask. Store as +1 and ten digits. Used for the "Sent:" copy line and alerts. |
| `timezone` | From Calendly; confirm. |
| `program_name` | Default `the Management Program`; confirm. |
| `i1_event_name` | List the coach's Calendly event types and ask which one is the i1. |
| `sheet_id` | Ask for the tracking sheet link. |
| `week1_monday` | Never ask. Open the sheet's "Week 1" tab, read the first session date in its header rows (column C of rows 2, 17, 32 and so on), and take the Monday of that week. If the tab names start higher than 1, count back. Show it in the settings block as found. |
| `i2_host_first_name` and `i2_booking_url` | Ask for the i2 host's Calendly booking link. |
| `recruitee_no_show_stage` | Default `i1 No Show`; confirm. |
| `recruitee_coach_tag` | Default `i1 <coach_full_name>`; confirm. |
| `texts_calendar_id` | Set in step 3. |
| `text_1_hour`, `text_10_min`, `text_qualification`, `text_call_reminder`, `text_i2_reminder` | Show the defaults from the after-session skill's `references/texts.md`. The coach may reword them. Keep the `<...>` tokens; they are filled in for each person. |
| Session hours | Ask which days their i1s run, the earliest time any i1 starts and the latest time any i1 starts across the week (whole hours only; example: earliest 10:00 AM on Wednesday, latest 3:00 PM on Tuesday), the earliest and latest hours they make qualification calls, and the latest hour an i2 can start. Used in steps 3 and 6. |
| `permission_texts`, `permission_bookings`, `permission_no_show_moves` | Set in step 4. |
| `recruitee_mode`, `recruitee_key_file`, `i2_booking_mode`, `i2_event_type_uri` | Set in step 1b. Never shown on the form. |

**Test:** read the sheet layout without writing (week tab found, i1 header rows where expected, i2 blocks found). If the layout differs from the after-session skill's `references/sheet.md`, stop and tell the coach: this version only works with the standard tracking template.

## Step 3. Phone texting

Follow `references/phone-setup.md`, one part at a time: create the Texts calendar, get it onto the iPhone, add the Shortcut, add the automations. Each part has a check; do not move on until it passes. The coach does these on their own phone and computer; Claude cannot. If the coach has the "i1 delegation: phone setup" page, it is the same steps with tick boxes.

**Test 1 (Shortcut):** write one test entry on the Texts calendar that started one minute ago, with a single line to the coach's own number: `<coach_mobile>|i1 delegation test 1: your Shortcut works.` Wait until the coach sees the entry on their phone, then ask them to run the Shortcut by hand and choose Always Allow on both prompts. They should receive the text, and a second run should ask nothing.

**Test 2 (on the hour):** write an entry starting at the next :58 that is at least 15 minutes away, with a line to the coach's own number: `<coach_mobile>|i1 delegation test 2: your on-the-hour automation works.` Ask the coach to lock the phone and wait for the top of that hour.

**Test 3 (ten-to):** write an entry starting at the next :35 that is at least 15 minutes away: `<coach_mobile>|i1 delegation test 3: your ten-to automation works.` It should arrive at ten to the hour, once. If it arrives a second time on the hour, the Shortcut's look-back is longer than 20 minutes: fix it before going on.

Then go through the automation list with the coach (`references/phone-setup.md`, Part 4): every time present, none twice, each Daily, Run Immediately, switched on.

Do not continue until all three arrive, each exactly once.

## Step 4. Standing permission

Ask about each of these separately, one per message, in a line or two each:

1. Texts to candidates are queued on the Texts calendar and auto-sent by the coach's phone.
2. People who are 1s and 2s are booked into the i2 on Calendly.
3. No-shows are moved in Recruitee, which emails them "we missed you" straight away.
4. People the coach calls a 3 are disqualified in Recruitee.

If the builder sheet already gives a choice for a row, read it back and ask the coach to confirm it here in the chat; the sheet alone is not enough. Otherwise ask about each one separately. Record four lines: `permission_texts`, `permission_bookings`, `permission_no_show_moves`, `permission_disqualify`. Write `granted <date>` only on a clear yes in the coach's own words. Write `ask` if they want to be asked each time, and `never` if they do not want that step done at all (texts can only be `granted` or `never`).

If `permission_texts` is not `granted`, tell the coach plainly: the reminder texts are written overnight when nobody is there to ask, so they will not be written at all. Skip the three text-writing tasks in step 6.

## Step 5. Write the settings block

Show the full block, headed `i1 settings`, one `key: value` per line, and ask the coach to check it. This block is copied into every scheduled task. It contains the coach's own number and no candidate data.

## Step 6. Create the scheduled tasks

Create the tasks in `references/task-prompts.md`, filling every `{placeholder}` from the settings block. There are two kinds:

- **Recurring cloud tasks** (create as scheduled tasks; they run in a fresh session and do not need the computer): `i1: write tomorrow's texts`, `i1: refresh today's texts`, `i1: write today's i2 reminder texts`, `i1: weekly sheet setup`, `i1: end-of-day check`. Turn on phone notifications for the last two.
- **Check-ins into this chat** (create as a one-off reminder into this chat; each one re-arms the next): `i1: daily planner` and, only if the coach says nobody else fills in the i2 times on their sheet, `i1: weekly i2 times`. These need the coach's Chrome, which only a chat like this one can reach.

Use exactly these names. The other skills find the tasks by name.

Some tasks depend on the coach's choices (`references/builder-sheet.md`, "What each choice changes"): skip the i2 reminder task when `send_i2_reminder` is `no`, the weekly sheet setup when `weekly_sheet_setup` is `no`, and the weekly i2 times check-in when `i2_times_by` is `i2_coach`. Set each task's days and hours from `i1_days`, `i1_start_hours` and `call_hours`.

Before creating anything, list the coach's existing scheduled tasks and skip any that already exist with the same name. After creating, list them again and show the coach a table: name, when it runs, what it does.

**Test:** if `permission_texts` is granted, run `i1: write tomorrow's texts` once now. Show the coach which entries it wrote and ask them to open one in their calendar and read it.

## Step 7. Dry run on a past session

Pick the coach's most recent cloud-recorded i1. A brand-new coach usually has none yet (recording was only switched on in setup): then say so in one line, skip this step, and tell them their first live session is the dry run; stay near the chat for it. Otherwise run the after-session routine in read-only mode: build the table of who showed, position, slot and call time, and show what would have been texted, booked and moved. Write nothing. Ask the coach whether the table is right. Differences usually mean the coach did not say a name, a position or a slot aloud; explain that the routine only knows what is said.

## Step 8. Hand over

Tell the coach in four short bullets, then say "You're set up.":

- What they still do: host the session; say each name, their 1, 2 or 3, their i2 slot and their call time aloud; make the calls; tick Qual.? on the sheet after each call.
- What must stay on. If both `recruitee_mode` and `i2_booking_mode` are `api`: the computer awake with the Claude app open (nothing needs to be on screen) from about 40 to 80 minutes after each i1 starts, so Claude can read the Recruitee key file. If either is still `browser`: the same hours, plus the i1 tab in its own visible window (and Sunday evening if Claude fills the i2 times from the browser); each i1 morning Claude opens that one tab and says so; the coach drags it into its own window, leaves it visible and not minimized, and does not close it or add tabs to it. In both cases: the phone not shut down or out of battery, with signal (locked with the screen off is fine).
- How to stop it: "pause i1" or "don't text" plus a name in this chat, or delete a line from a Texts calendar entry before it sends.
- How they will know if something failed: the end-of-day check sends a phone alert.

## Step 9. Certificate

Right after "You're set up.", make the certificate and send it as a file in the chat. Do not draw it yourself; run the bundled script so it looks the same for every coach:

`python3 <this skill's folder>/scripts/certificate.py "<coach_full_name>" "<today, like October 9, 2026 or 9 octobre 2026>" i1-delegation-certificate.pdf [fr]`

Add `fr` as the last argument for a francophone coach; the certificate's wording is then in French.

If reportlab is missing, install it first (`pip install reportlab`). Send the PDF with one line: "Your certificate. Welcome aboard." If the script fails twice, say so in one line and move on; the certificate is a nice-to-have, never a blocker.

## Limits

- Never ask for or type a password. Never sign in for the coach.
- Never ask the coach to paste a token into the chat, and never open, print or quote the Recruitee key file.
- Never create an account.
- Never write candidate names, emails or phone numbers to a file.
- Setup changes nothing in the tracking sheet, Calendly or Recruitee, except on the coach's own test candidate and one test booking that is cancelled straight away (step 1b). Otherwise only the Texts calendar test entries, the empty key file and the scheduled tasks are created.
