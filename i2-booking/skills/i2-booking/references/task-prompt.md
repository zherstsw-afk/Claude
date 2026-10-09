# Scheduled task prompt: "i2: book handoff rows"

Paste everything from the next line into the scheduled task, with your settings filled in. Hourly.

---

Book the i2 handoff rows for {i2_host_first_name}. Nobody is watching this run: do not ask questions; set rows that need a person to `needs you` and report.

i2 booking settings:
- i2_event_type_uri: {i2_event_type_uri}
- timezone: {timezone}
- i2_host_first_name: {i2_host_first_name}
- sheet_id: {sheet_id}
- handoff_first_column: {handoff_first_column}
- week1_monday: {week1_monday}

Follow the i2-booking skill in full: find the current and next week tabs, read the handoff block's `ready` rows, check each against this coach's Calendly first, book only a listed slot, record the result, and clear Email and Phone only after a confirmed booking. Never write outside the handoff block. Report briefly with no names, emails or phone numbers.
