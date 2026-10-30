# ⚽ Premier League Analytics Dashboard

An interactive football analytics dashboard built using Python, Pandas, Plotly and Streamlit to analyse and compare English Premier League team performances across multiple seasons.

### Live Dashboard

[View the Interactive Premier League Analytics Dashboard](https://premier-league-analytics-h6vv5ehwdlplaysogchru7.streamlit.app)

## Project Overview

This project transforms historical Premier League match results into an interactive dashboard, allowing users to explore league standings, visualise team performance and compare statistics across seasons.

The dashboard currently supports the 2023/24, 2024/25 and 2025/26 seasons.

## Key Features

- **League Overview:** Automatically generated league tables with points, wins, draws, losses, goals scored, goals conceded and goal difference.
- **Interactive Visualisations:** Bar charts showing points by team and grouped bar charts comparing goals scored against goals conceded.
- **Team Analysis:** Individual team statistics and performance metrics.
- **Team Comparison:** Compare two Premier League teams using selectable performance statistics.
- **Season Selection:** Switch between three Premier League seasons.

## Technologies Used

- **Python:** Core data processing and application logic.
- **Pandas:** Data loading, filtering, manipulation and statistical calculations.
- **Plotly:** Interactive data visualisations.
- **Streamlit:** Web dashboard interface.
- **Git and GitHub:** Version control and project hosting.

## Running the Project Locally

1. Clone the repository.
2. Install the dependencies using `pip install -r requirements.txt`.
3. Run `streamlit run dashboard.py`.

The dashboard automatically retrieves Premier League match data from Football-Data.co.uk, so no manual dataset downloads are required.

## Data Source

Match results and statistics are sourced from [Football-Data.co.uk](https://www.football-data.co.uk/). Data belongs to its respective provider and is used for educational and portfolio purposes.

## Skills Demonstrated

- Cleaning and transforming structured data with Pandas.
- Calculating performance metrics from raw match results.
- Building reusable Python functions.
- Creating interactive charts and dashboards.
- Validating calculated statistics.
- Using Git and GitHub for version control.