# Chess.com Behavioral Analysis
### Does six years of data reveal a compulsive playing pattern?

---

## Background

This project analyzes my own complete Chess.com game history, covering **21,007
games** played between **November 2020 and May 2026**. I am referred to throughout
as "the user" — a deliberate choice to practice writing objective, third-person
analytical reports, the same way a professional analyst would write about a client.

Rather than asking *"how well did I play?"*, this analysis asks a harder question:
**do my behavioral patterns — volume, timing, session structure, and requeue habits
— show signs of compulsive use?**

All data was collected via the Chess.com Public API. No authentication was required.

---

## The Data

| Field | Value |
|---|---|
| Total games | 21,007 |
| Date range | 2020-11-10 → 2026-05-08 |
| Unique opponents | 20,242 |
| Opponent countries | 223 |
| Most played format | Blitz (94% of all games) |
| Overall win rate | 50.1% |

---

## Five Behavioral Signals

### 1 — Daily Volume: Binge Days Are Frequent

A "binge day" was defined as any day with games at or above the **95th percentile**
of daily volume, which came out to **38 games per day**.

| Metric | Value |
|---|---|
| Binge threshold (95th percentile) | 38 games/day |
| Number of binge days | 93 |
| Most games in a single day | **93 games** |

93 binge days over roughly 5 full years means the user averaged a binge **once
every three weeks**. The peak of 93 games in a single day represents approximately
5 hours of continuous 3-minute blitz chess.

The 30-day rolling average also reveals that volume was not randomly distributed —
binge days tend to cluster, suggesting multi-day escalation periods rather than
isolated incidents.

---

### 2 — Requeue Speed: Both Wins and Draws Drive the Loop

The time between consecutive games was measured for all games within a 2-hour
window. The original hypothesis was that the user would requeue faster after
losses — the classic "tilt" pattern. The data told a more nuanced story.

| Result of previous game | Median time to next game |
|---|---|
| Draw | **6.0 minutes** |
| Win | **6.3 minutes** |
| Loss | 8.2 minutes |

The user requeues **slowest after losses** and fastest after draws and wins.
This is the opposite of tilt. Rather than chasing losses out of frustration,
the user slows down when they lose — and accelerates when the result feels
unresolved (draw) or rewarding (win).

Draws producing the fastest requeue is particularly interesting: a draw in blitz
often feels like a near-win, and the data suggests the user immediately seeks
to resolve that tension with another game.

This is a **reward and tension loop**, not a frustration loop. It is arguably
more entrenched because it is being driven by positive and ambiguous outcomes
rather than negative ones.

---

### 3 — Late Night Play: 1 in 5 Games After 22:00

**21.0% of all games** — more than 4,400 games — were played after 22:00.

| Time block | Notes |
|---|---|
| Morning (5–12) | Lowest volume |
| Afternoon (12–18) | Peak performance window (Lunch Break - Train Commute Back)|
| Evening (18–22) | High volume |
| Late night (22–5) | **21% of all games (~4,400 games)** |

Playing chess after 10pm is not inherently problematic. Playing over four thousand
games after 10pm across six years is a different matter. This is the clearest
signal that the habit was regularly competing with sleep and rest.

---

### 4 — Session Length: Up to 16 Hours in a Single Sitting

A session was defined as a continuous block of games where no gap between
consecutive games exceeded 2 hours.

| Metric | Value |
|---|---|
| Total sessions identified | 3,689 |
| Median session length | 3 games |
| Mean session length | 5.7 games |
| Longest session | **92 games over 14 hours** |

The median of 3 games sounds healthy. The extremes do not.

**Top 5 longest sessions:**

| Date | Games | Duration | Win rate |
|---|---|---|---|
| 2024-12-28 | 92 | 14.0 hours | 49.5% |
| 2025-03-14 | 85 | 16.7 hours | 54.7% |
| 2024-07-21 | 65 | 12.7 hours | 53.8% |
| 2025-08-03 | 63 | 10.8 hours | 52.4% |
| 2024-05-04 | 59 | 11.3 hours | 45.8% |

A 16-hour session of anything is remarkable. A 16-hour session of a mobile game
that can be started with a single tap is the kind of behavior the user themselves
described as: *"I found myself playing when I didn't even remember opening the app."*

Notably, win rates in the longest sessions hover around 50% — the user is not
playing noticeably worse in marathons, which removes a natural self-correction
mechanism. If long sessions produced bad results, the feedback loop might
discourage them. It doesn't.

---

### 5 — Yearly Trend: The Habit Nearly Doubled Every Year

| Year | Games | Notes |
|---|---|---|
| 2020 | 287 | Partial year (joined November) |
| 2021 | 1,715 | First full year |
| 2022 | 1,208 | Declined — only year below previous |
| 2023 | 2,917 | Sharp increase resumes |
| 2024 | 5,820 | Doubled from 2023 |
| 2025 | 7,610 | New peak — another near-double |
| 2026 | 1,450 | Partial year (through May) |

From 2021 to 2025, games played increased by **344%**. A casual hobby does not
follow this trajectory. The 2022 dip is the only year where volume declined —
and the rebound was immediate and steep.

Win rate remained stable across all years (49.5%–52.6%), meaning the escalation
in volume was not driven by improvement or deterioration — it was driven purely
by increased playing time.

---

## Summary of Findings

| Signal | Finding | Verdict |
|---|---|---|
| Daily volume | 93 binge days; max 93 games in one day | ⚠️ Concerning |
| Requeue speed | Fastest after draws (6.0 min) and wins (6.3 min) | ⚠️ Reward/tension loop |
| Late night play | 21% of all games after 22:00 | ⚠️ Concerning |
| Session length | Max 16.7 hours; five sessions over 10 hours | 🔴 Severe |
| Yearly trend | 344% increase from 2021 to 2025 | 🔴 Escalating |

No single signal is conclusive on its own. Together, they paint a consistent
picture: **this is not a stable casual habit**. The volume is escalating, the
sessions are extreme, late-night play is normalized, and both wins and draws
are actively reinforcing continued play.

---

## Recommendations

These recommendations follow directly from the findings. They are practical and
specific — not generic advice to "play less."

**1. Set a hard daily game limit.**
Based on the data, 15 games/day sits comfortably below the binge threshold (38)
while still allowing meaningful play. Chess.com's Play Limit feature can enforce
this automatically.

**2. Add a mandatory cooldown after every draw.**
Draws — not wins or losses — trigger the fastest requeue in the data (6.0
minutes median). A 15-minute forced pause after a draw would directly interrupt
the tension loop identified as the primary driver of continued play.

**3. Block access after 22:00.**
21% of all games were played in this window. Using screen time controls (iOS
Screen Time or Android Digital Wellbeing) to restrict the app after 22:00 would
address the most consistent life-interference signal in the dataset.

**4. Cap session length at 10 games.**
Five separate sessions exceeded 10 hours. A self-imposed 10-game session limit —
enforced via Chess.com settings — would have prevented every extreme session in
the dataset without meaningfully restricting normal play (median session is 3 games).

---

## Reflection

This project started as a question I was uncomfortable asking out loud. I had
noticed I was sometimes playing chess without remembering opening the app — and
I wanted to know whether the data would confirm what I already suspected.

It did. Seeing the patterns laid out — the 16-hour sessions, the 344% volume
increase, the draw-triggered requeue loop, the 4,400 late-night games — made it
impossible to dismiss as a casual hobby getting slightly out of hand.

Since completing this analysis, I have set a daily game limit on Chess.com and
enabled screen time restrictions after 22:00. The recommendations in this report
are ones I am actually following.

The most useful thing data analysis can do is make the invisible visible. This
project was a reminder that the subject doesn't have to be business data to be
worth analyzing rigorously.

---

## Methodology Notes

- Game data collected via Chess.com Public API (no authentication required)
- Opponent country data collected from 20,242 individual player profiles
- Sessions defined as continuous blocks with no gap exceeding 2 hours between games
- Requeue speed calculated as time between game start timestamps (end times are
  not available in the API)
- Binge threshold defined as the 95th percentile of daily game volume
- Result classification uses the cleaned `result` column (`win`, `draw`, `loss`)
  rather than raw `player_result` subtypes, to correctly capture all draw variants
  (agreed, stalemate, repetition, insufficient material, etc.)
- Partial years (2020, 2026) excluded from year-over-year growth calculations

---

## Tools Used

- **Python** — data collection, cleaning, and analysis
- **pandas** — data manipulation
- **matplotlib / seaborn** — visualization
- **Chess.com Public API** — data source

---

*This analysis was completed as a capstone project for the Google Data Analytics Certificate.*
