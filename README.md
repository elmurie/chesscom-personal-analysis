# Chess.com Personal Performance Analysis
### Google Data Analytics Certificate — Capstone Project (Case Study 3)

---

## Background

This project is the capstone case study for the Google Data Analytics Professional Certificate. As a junior data analyst working for a business intelligence consultant, I was tasked with leading an end-to-end analytics project — from defining the business question through presenting data-driven recommendations.

I chose to analyze my personal Chess.com game history, as it provides a rich, structured, and personally meaningful dataset with clear performance metrics.

---

## Ask

### Business Task

> **How can a chess player optimize their performance on Chess.com by identifying the conditions — time of day, day of the week, game format, opening, and color — that consistently lead to better results?**

### Key Questions

- Does the hour of day or day of the week affect win rate?
- Which game formats (Bullet, Blitz, Rapid) show the strongest rating progression?
- Does playing White or Black lead to meaningfully different outcomes?
- Which openings produce the best results when played consistently?
- How does opponent strength (rating difference) affect expected performance?
- Which countries produce the toughest opponents on average?

### Stakeholders

- **Primary:** The player (personal improvement decision-making)
- **Secondary:** Any chess player or coach looking to apply data-driven training prioritization

---

## Prepare

### Data Sources

| Source | Description |
|---|---|
| [Chess.com Public API](https://api.chess.com/pub/) | Monthly game archives, player profile, player stats |
| Chess.com opponent profiles | Country, title, join date, follower count for each unique opponent |

All data was collected programmatically via the Chess.com Public API using Python (`requests`). The API is publicly available and does not require authentication for public player data.

### Data Organization

The raw dataset contains one row per game and includes:
- Game date and time
- Time class and time control
- Player and opponent usernames and ratings
- Game result (raw Chess.com format)
- ECO opening URL
- PGN string

Opponent profiles were fetched separately and stored as a lookup table, then merged with the game data on the cleaned opponent username.

### Data Credibility (ROCCC)

- **Reliable:** Data comes directly from Chess.com's official API
- **Original:** First-party data collected from the primary source
- **Comprehensive:** Full game history across all formats and time periods
- **Current:** Data reflects the complete activity history up to the collection date
- **Cited:** Source clearly documented and reproducible

### Licensing & Privacy

Chess.com's Public API provides access to public player data. No personal or private information beyond publicly visible profile data was collected. The username used is the analyst's own account.

---

## Process

### Tools

- **Python** (pandas, numpy) — data collection, cleaning, feature engineering
- **Jupyter Notebooks** — reproducible, documented analysis pipeline
- **Plotly / Matplotlib** — visualization

### Cleaning Steps

1. Parsed timestamps into structured date features (`year`, `month`, `weekday`, `hour`)
2. Created player-centric columns (side played, player rating, opponent rating, rating difference)
3. Standardized game results from Chess.com's raw outcome codes into `win`, `draw`, `loss`
4. Assigned a numeric score (`win=1`, `draw=0.5`, `loss=0`) for aggregation
5. Extracted opening names from ECO URLs
6. Merged opponent country codes from the enriched profiles table
7. Applied a minimum games threshold (≥20 games per country, ≥500 per opening) to filter statistically insignificant groups

All cleaning steps are documented in `02_data_cleaning.ipynb`.

---

## Analyze

### Key Findings

- **Time of day matters:** Win rate varies noticeably across hours, with a clear peak performance window identifiable in the data
- **Day of the week:** Performance and volume differ across weekdays, suggesting certain days are better for competitive play
- **Color advantage:** A measurable difference exists between performance as White vs Black
- **Openings:** Several openings played 500+ times show consistently above-average scores; others consistently underperform
- **Rating difference:** Performance degrades predictably against stronger opponents, but the rate of degradation reveals how competitive the player is near their rating ceiling
- **Geography:** Certain countries produce significantly stronger average opponents, while win rates against others are above or below the overall average

Full analysis is in `03_exploratory_analysis.ipynb`.

---

## Share

### Visualizations

All publication-ready charts are saved in the `/plots` directory and were built in `04_visualizations.ipynb`:

- `rating_progression.png` — Rating over time by format (Bullet, Blitz, Rapid)
- `performance_by_hour.png` — Win rate and game volume by hour of day
- `white_vs_black.png` — Average score by color
- `best_openings.png` — Top performing openings (min. 500 games)
- Interactive choropleth maps (Plotly) for games played, win rate, and average opponent rating by country

---

## Act

### Recommendations

Based on the analysis, the following actions would most likely improve rating and performance:

1. **Schedule competitive games during peak performance hours** — avoid late-night sessions if the data shows a drop in win rate
2. **Prioritize the best-performing day of the week** for rated games; use lower-performance days for casual or experimental play
3. **Double down on high-performing openings** — if a specific opening has a strong win rate across 500+ games, it's worth studying deeper
4. **Be selective with formats** — if one time class shows a stronger rating trajectory, focus competitive effort there
5. **Study opponent patterns by country** — if certain countries consistently produce higher-rated opponents, use those matchups as benchmarks

### Further Exploration

- Add **time-series forecasting** to project rating trajectory under different training scenarios
- Incorporate **move-level data** from PGN to identify where games are won or lost (opening vs middlegame vs endgame)
- Analyze **opponent recurrence** — are there repeat opponents, and does performance change over rematches?
- Build a **personal opening repertoire dashboard** combining win rate, frequency, and opponent response rates

---

## Repository Structure

```
chesscom-personal-analysis/
├── dataset/
│   ├── raw/            # Raw API data (games, profiles)
│   └── processed/      # Cleaned, analysis-ready dataset
├── notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_exploratory_analysis.ipynb
│   └── 04_visualizations.ipynb
├── plots/              # Exported charts
├── src/
│   └── config.py       # Username configuration
├── requirements.txt
└── README.md
```

---

## How to Reproduce

```bash
git clone https://github.com/elmurie/chesscom-personal-analysis
cd chesscom-personal-analysis
pip install -r requirements.txt
# Set your Chess.com username in src/config.py
# Run notebooks in order: 01 → 02 → 03 → 04
```

---

*Google Data Analytics Professional Certificate — Capstone Project*
