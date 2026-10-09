# i2 booking: setup guide for i2 coaches

This takes about 5 minutes, and it runs by itself after that. Your computer doesn't need to be on.

**What it does:** when an i1 coach's students qualify, their i2 spot is booked on your Calendly automatically. Each student gets Calendly's normal confirmation.

**What you need:**
- Claude (the Cowork tab in the Claude app, or claude.ai on the web)
- Your Calendly account connected to Claude
- Your Google account connected to Claude
- Editor access to the tracking sheet (the i1 coach shares it with your Google email)

---

## Step 1. Connect Calendly and Google Sheets

1. Open Claude and click **Customize**, then **Connectors**.
2. Click **Calendly**, then **Connect**. Sign in with **your own** Calendly login.
3. Click **Google Sheets**, then **Connect**. Sign in with your Google account.

## Step 2. Add the plugin

1. Click **Customize**, then **Plugins**.
2. Click **Add** and choose **i2-booking-plugin.zip**.
3. Check that **i2-booking** shows in your list.

## Step 3. Paste the setup prompt

1. Open a new chat in Claude.
2. Paste the prompt your i1 coach sent you (it's filled in with your details) and send it.

Claude checks your connections, asks about your i2 event type if you have more than one, sets up the plugin, and runs a test on the test row your i1 coach has already added to the sheet.

## Step 4. Check the test

1. Check the row: it should say **booked**, with a booked time, and the email and phone cleared.
2. Cancel the test booking in Calendly (open the confirmation email and click Cancel).

Once the test works, the hourly check turns on by itself, and it only runs on the i1 days.

## If something goes wrong

- A row says **needs you**: the note says why. Fix that one thing and type "run the i2 booking" again.
- Calendly says no: your access changed. Stop and tell your i1 coach.
- To pause: type "pause i2 booking" in any Claude chat. To turn it back on: "resume i2 booking".
