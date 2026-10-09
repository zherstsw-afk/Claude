# i1 delegation

Runs the work around a Student Works coach's i1 information sessions, so the coach only hosts the session and makes the calls.

## What it does

- Writes the reminder texts for each session; the coach's phone auto-sends them.
- After each session, reads the recording and fills the tracking sheet.
- Books each 1 and 2 into the i2 on Calendly.
- Moves no-shows in Recruitee, disqualifies 3s, and adds a note for each 2.
- Puts qualification calls on the coach's calendar.
- Checks each evening that every session was handled and alerts the coach's phone if not.

## Skills

| Skill | Say | What it does |
|---|---|---|
| i1-setup | "set up i1 delegation" | Walks through setup with a test after each step |
| i1-after-session | "I ended my meet" (or it runs by itself 40 minutes after a session starts) | The after-session routine |
| i1-controls | "pause i1", "i1 status", "don't text" plus a name | Stop, pause, resume, check, change settings |

## Before setup

Each coach fills in a builder sheet first: one page of their own rules (which texts send and when, the wording, how the sheet is filled, what happens after a session). The setup skill reads it and turns it into their settings.

## What a coach needs

- A paid Claude plan, used in the Cowork tab of the Claude desktop app, with Google Sheets, Google Calendar, Calendly and Zoom connected. The Claude app on their iPhone with notifications on, for alerts.
- For Recruitee without a browser: a Recruitee personal API token, kept in a file (`i1-recruitee.txt`) in a folder on the coach's Mac connected to the i1 chat. The coach's Recruitee hiring role must allow API tokens.
- For i2 bookings without a browser: the i2 coach gives the coach "Can view" permission on the i2 event type in Calendly (`skills/i1-setup/references/setup-i2-coach.md`).
- Only for a step still in browser mode: the Claude extension in the Chrome browser where they are signed in to Recruitee. (The i2 booking page is public; no Calendly sign-in is needed in Chrome.)
- A Zoom account with AI Companion, with Meeting summary set to start automatically, and i1s hosted on that account. Claude reads the AI Companion transcript; cloud recording is optional.
- An iPhone, for the texting Shortcut.
- The standard i1/i2 tracking sheet.
- A computer left awake with the Claude app open from about 40 to 80 minutes after each i1 starts. With both steps on the API, nothing needs to be on screen. With either still in browser mode, the i1 tab must also be in its own visible window: each i1 morning Claude opens one Chrome tab, the coach drags it into its own window and leaves it visible, and Claude uses that one tab for whatever is still in browser mode.
- Sessions that start on the hour.

## What stays with the coach

Host the session. Say each person's name, their 1, 2 or 3, their i2 slot and their call time aloud. Make the qualification calls. Tick Qual.? on the sheet after each call.

## If it breaks

Do the step by hand, as before. Nothing in this plugin replaces access the coach already has.

Version 0.6.0. Recruitee moves, disqualifications and notes can run over Recruitee's API through a bundled script (`skills/i1-after-session/scripts/recruitee.py`), and i2 bookings through the Calendly connector once the i2 coach grants access; with both on, no Chrome window is needed. Setup step 1b tests both on a test candidate and a test booking. Browser mode stays as the fallback.

Version 0.5.7. Certificate signed Student Works. Setup asks English or français first and keeps that language; French certificate. Setup ends with a certificate PDF made by a bundled script (same look for every coach). Setup hands the coach a prefilled settings form in the chat instead of asking for a builder sheet. Transcripts come from Zoom AI Companion (cloud recording optional). Each i1 morning Claude opens one Chrome tab (the i1 tab) for the bookings and Recruitee. Setup talks in short, one-step messages; a copy-paste helper prompt (skills/i1-setup/references/helper-prompt.md) gets new coaches through installing the plugin. Recordings come from Zoom cloud recording. First run on a live week: October 2026.
