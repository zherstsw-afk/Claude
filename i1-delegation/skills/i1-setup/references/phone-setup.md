# Phone setup (iPhone)

The coach's own iPhone auto-sends every text, from their own number. There are four parts, built in this order, and each depends on the one before. The coach does all of them on their own phone and computer; Claude cannot. Walk them through one part at a time and do not move on until that part's check passes.

Menu names differ a little between iPhone software versions. If a button is not called exactly what is written here, tell the coach to look for the closest match.

When explaining what the phone needs day to day, say "not shut down or out of battery", never "on": locked with the screen off is fine, and coaches read "on" as "screen lit".

## Part 1. Create the Texts calendar (computer)

1. Open calendar.google.com with the same Google account the coach's Claude is connected to.
2. On the left, find "Other calendars" and click the + beside it. Choose "Create new calendar".
3. Name it exactly `Texts` (capital T, nothing else). The Shortcut looks for a calendar with this name.
4. Click "Create calendar". It shows on the left under "My calendars".
5. Hover over Texts, click the three dots, choose "Settings and sharing".
6. Scroll to "Integrate calendar" and copy the "Calendar ID". It ends in `@group.calendar.google.com`. This is `texts_calendar_id`.

Keep the calendar private: not shared, not public. It holds candidates' phone numbers.

**Check:** the coach sees Texts in their list and gives Claude the Calendar ID. Confirm Claude can read that calendar.

## Part 2. Get the Texts calendar onto the iPhone

The Shortcut can only read calendars that show in the iPhone's built-in Apple Calendar app (the white app with the date on it, not Google Calendar). Say "Apple Calendar" to the coach every time; "Calendar" alone gets taken as Google Calendar.

1. Settings, Apps, Calendar, Calendar Accounts (older software: Settings, Calendar, Accounts).
2. The same Google account must be listed with Calendars switched on. If it is not listed: Add Account, Google, sign in, switch Calendars on, save.
3. "Fetch New Data" is on the same Calendar Accounts screen, listed under the accounts; do not tell the coach to go back a screen. Tap it, set the Google account to Fetch, and the schedule at the bottom to "Every 15 Minutes". Never Manually: the phone would only notice new texts when the coach opens the Apple Calendar app.
4. Open the Apple Calendar app, tap Calendars at the bottom, and make sure Texts is ticked under the Google account.
5. If Texts is not listed: pull down to refresh and wait a minute. Still missing: on the phone's browser open `calendar.google.com/calendar/syncselect`, tick Texts, save, refresh again.

**Check:** write a test entry on the Texts calendar a few minutes ahead, titled `sync test`, with an empty description. Ask the coach whether it shows on their phone within a minute or two.

## Part 3. Add the Shortcut

The coach copies the working one; they do not build it. First delete the `sync test` entry from Part 2 so it cannot be picked up by a test.

1. On the iPhone, open https://www.icloud.com/shortcuts/b46c7a72f38147829a97d65cbd0c9aa9 and tap "Add Shortcut". It is named `I1 Texts`.
2. Open it with the three dots on its tile (tapping the tile runs it).
3. The first action must read: Calendar is Texts, Start Date is in the last 20 minutes. If the calendar is blank or different, pick Texts. Never change the 20.
4. Tap Done.

If the link does not work, the Shortcut can be built by hand:

1. **Find Calendar Events.** Filters: Calendar is `Texts`; Start Date is in the last 20 minutes. Sort by Start Date, Latest First. Limit: 1.
2. **Get Details of Calendar Events.** Detail: Notes.
3. **Split Text.** Split the Notes by New Lines.
4. **Repeat with Each** item in the split text:
   1. **Split Text.** Split Repeat Item by Custom: `|`
   2. **Get Item from List.** First Item. This is the number.
   3. **Get Item from List.** Last Item (from the same split). This is the message.
   4. **Send Message.** Message: the last item. Recipient: the first item. Turn "Show When Run" (or "Show Compose Sheet") off.
5. **End Repeat.**

The 20 minutes is only how far back it looks. Entries for the on-the-hour run start at :58. Entries for the ten-to run start at :35, which is inside the ten-to run's look-back and outside the on-the-hour run's.

**Check (Test 1, by hand):** write an entry that started one minute ago with a single line to the coach's own number. Wait until they see it on their phone, then have them tap the Shortcut. The phone asks to use the calendar and to send a message: they must choose **Always Allow** both times. With "Allow Once", every automatic send stops and waits. If they chose wrong: three dots on the Shortcut, the info button, Privacy, set Calendar and Messages to Always Allow. The test passes when the text arrives and a second run asks nothing.

## Part 4. Add the automations

Automations cannot be shared. The coach adds each one.

To add one:

1. Shortcuts app, Automation tab, the + in the top corner.
2. Time of Day. Set the time. Repeat: Daily.
3. Choose "Run Immediately" and switch "Notify When Run" off. "Run After Confirmation" would hold every text until the coach taps.
4. Next, then pick `I1 Texts`. If a blank automation opens, add the action Run Shortcut and choose `I1 Texts`. Done.

Which times, worked out from `i1_start_hours`, `call_hours` and the latest i2 start hour:

- **On the hour:** every hour from one hour before the earliest i1 start to the later of (an hour before the latest call) and (an hour before the latest i2). For the default hours this is every hour from 9:00 AM to 8:00 PM, twelve in all.
- **Ten to the hour:** one for each hour an i1 can start. For the default hours: 9:50, 10:50, 11:50 AM, 12:50, 1:50, 2:50 PM, six in all.

Give the coach their exact list of times and have them confirm each as they add it. A run with nothing queued sends nothing, so daily including weekends is fine.

**Check the list with the coach:**

- every time is there;
- no time is there twice (two automations at the same time send every text twice);
- each says Daily, runs `I1 Texts`, and is set to Run Immediately with Notify When Run off;
- none is switched off.

**Test 2 (on the hour):** write an entry starting at the next :58 that is at least 15 minutes away, one line to the coach's own number. They confirm they can see it, lock the phone and wait. It must arrive on the hour by itself.

**Test 3 (ten to):** write an entry starting at the next :35 that is at least 15 minutes away. It must arrive at ten to the hour, once. A second copy on the hour means the 20 minutes in the Shortcut was changed.

Do not continue the setup until all three tests have arrived, each exactly once, with the phone locked for tests 2 and 3.

## If something is not working

| What the coach sees | What to check |
|---|---|
| Nothing sends | Texts ticked in the Apple Calendar app; the entry visible on the phone; an automation for that time, switched on; the Shortcut's calendar is Texts |
| Sends when tapped, not on the timer | The automation is missing, off, or set to Run After Confirmation |
| The phone asks permission every time | Allow Once was chosen; set Calendar and Messages to Always Allow |
| Works unlocked, not locked | In the Shortcut's info screen, under Privacy, look for a switch that allows running while locked |
| Every text twice | Two automations at the same time, or the 20 minutes was changed |
| A text never sent though the entry exists | The entry reached the phone too late: Fetch New Data on Every 15 Minutes, signal, and Low Power Mode off during session hours |
| Phone was shut down or out of battery at a send time | Those texts are skipped, not sent later; the coach sends them by hand from the entry |

## Stopping a text by hand

Open the entry in the Apple Calendar app (or Google Calendar on the computer) and delete that person's line from the notes before the send time. Do this after the morning refresh (8:15 AM) on the day: the overnight and morning tasks rebuild the lists from the bookings, so a line deleted earlier comes back. To keep someone off the lists, say "don't text" and their name in the i1 chat. To stop every text for a while, switch the automations off, or say "pause i1" in the i1 chat.
