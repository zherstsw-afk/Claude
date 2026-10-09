# What the i2 coach does (for API bookings)

Give the coach this message to send to the i2 coach, with the names filled in. Take each route in order; go to the next only if setup's Part B test fails on the one before.

## Route 1: event type permission (the i2 coach, 2 minutes)

> Hi <i2 coach first name>, I'm automating my i2 bookings so Claude books my 1s and 2s straight into your i2, the same as when they book themselves. For that, Calendly needs to let me see your i2 event type. Could you:
> 1. Open Calendly and go to Scheduling.
> 2. On your i2 event type, click the three dots, then Edit permissions (it may just say Permissions).
> 3. Add me (<coach's Calendly email>) with "Can view".
> 4. Save, and tell me when it's done.
> It doesn't let me change or cancel anything of yours, and you can take it back any time the same way. Thanks!

Calendly offers event type permissions on Standard, Teams and Enterprise plans, for personal and shared event types. In Calendly's own app, "Can view" lets the person book meetings on the host's behalf. Calendly's documents do not say whether it also opens the event type to the coach's API connection; the Part B test settles it.

## Route 2: Calendly admin role (the Calendly owner)

Only if Route 1's test fails. The organisation's Calendly owner changes the booking coach's role to Admin in Calendly's user management (admin settings). Admin tokens can read every member's event types. Calendly does not say whether they can also book on them; the Part B test settles it. This gives the coach much wider rights (every member's events and settings), so the owner should decide. Many will rightly say no.

## Neither works

Keep `i2_booking_mode: browser`. Bookings still need the i1 tab, but Recruitee does not (Part A). A visible window is then needed only for the bookings.

## What this does not need

- No password and no token from the i2 coach. Never ask the i2 coach for their Calendly API token: it would give the coach full control of the i2 coach's account.
- No change to the i2 event type itself.
