# The tracking sheet

The sheet (`sheet_id`) follows the company's i1/i2 tracking template. Other people use it too, so write only the cells named here.

## Finding the week tab

Tabs are named `Week 1`, `Week 2` and so on. Week 1 is the week of `week1_monday`; each later week adds one.

## Finding the session's i1 block

- i1 blocks are stacked in columns A to F, 15 rows apart. Header rows are 2, 17, 32, 47 and so on.
- On a header row, column C holds the session date and time and column F holds the host's name.
- The session's block is the one whose header has this session's date and time in C and `coach_full_name` in F.
- The 12 name rows start two rows below the header.
- If no block matches, write nothing and put it on the "Needs you" list.

## What to write on each name row

| Column | Holds | Write |
|---|---|---|
| B | Name (filled by a formula) | Never write |
| C | Show? | TRUE or FALSE (a boolean, not text) |
| D | Conversion | 1, 2 or 3 (a number), only for people who showed |
| E | i2 Timeslot | The slot text exactly as the dropdown offers it, or `Find a time` |
| F | Notes | One or two words about the person (`notes_style: sentence` = one short sentence; `none` = blank). No personal characteristics. The call time goes here only when `call_time_location` is `notes`. |

The slot texts for the week are the dropdown options in column E. They match the i2 block headers, written like `Tues 5:00 PM`.

## Colours (columns B to F of the row)

Skip this section when `colour_rows` is `no`.

| Case | Colour (red, green, blue) |
|---|---|
| Showed | 0.851, 0.918, 0.827 |
| No-show | 0.85, 0.85, 0.85 |
| Position 3 | 0.957, 0.8, 0.8 |

Column B of the first name row in each block is protected. Colour only C to F on that row, and send it as its own request, or the whole write fails.

## The i2 blocks

- They sit in columns I to T, stacked down the page. Read I1:T70 first.
- Each block starts with a header row: `Date` in I and P, the day in J and Q, the start time in L and S.
- The next row holds the titles (Name, Qual.?, Show?, Appl.?, Deadline). The eight rows after it hold people.
- There are two groups. Left: I to M. Right: P (Name), Q (Qual.?), R (Show?), S (Appl.?), T (Deadline).
- Skip this when `add_to_i2_block` is `no`.
- Put each 1 and 2 in the **right-hand** group of their slot's block: name in column P at the next empty row, and `Call <Day> H:MM PM` in column T (leave T blank unless `call_time_location` is `deadline`, the default). No colour.
- If the block is full, do not write. Put it on the "Needs you" list.
- The coach ticks Qual.? after the qualification call. The i2 reminder text only goes to people with that box ticked.

## Never

- Never insert, delete, move, sort or clear rows.
- Never write in another host's block.
- Never touch tabs other than the week tab.
- If the layout is not as described here, stop, write nothing, and report that the layout is different.
