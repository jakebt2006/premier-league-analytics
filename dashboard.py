import pandas as pd
# imports pandas using the shortcut pd

import streamlit as st
# imports streamlit using the shortcut st

import plotly.express as px
# imports plotly using the shortcut px

from main import create_league_table, create_points_chart, create_goals_chart
# retrives all the things we need from main.py

st.set_page_config(page_title="Premier League Analytics", page_icon="⚽", layout="wide")
# configures the browser tab and page layout to our specifications

st.title("⚽ Premier League Analytics Dashboard")
# displays the main dashboard heading

st.caption("Interactive Premier League performance analysis")
# creats a caption for the website

st.write("Explore Premier League statistics, league tables and team performances.")
# displays text on the webpage

season_files = {"2025/26": "https://www.football-data.co.uk/mmz4281/2526/E0.csv", "2024/25": "https://www.football-data.co.uk/mmz4281/2425/E0.csv", "2023/24": "https://www.football-data.co.uk/mmz4281/2324/E0.csv"}
# creates a dictionary where each key is a season displayed to the user and eaach value is the CVS filename

selected_season = st.sidebar.selectbox("Select Premier League season:", list(season_files.keys()))
# we make a drop down in the websites sidebar and give a list of the available seasons for the user to choose

page = st.sidebar.radio("Navigation", ["League Overview", "Team Analysis", "Team Comparison"])
# creates a menu where users can select one option

st.divider()
# creates a line to seperate sections

st.write(f"Currently viewing: **{selected_season} Premier League**")
#  shows the user what season they are viewing

stats_table = create_league_table(season_files[selected_season])
# the user picks a season and the filename is passed into our function

team_names = stats_table["Team"].tolist()
# selects the Team column from our DataFrame and converts it into a lsit

st.sidebar.divider()
# creates another divider but in the sidebar

st.sidebar.subheader("Season Summary")
# gives a subheading in the sideabr

st.sidebar.metric("Teams", len(stats_table))
# calculates the total number of teams

st.sidebar.metric("Matches Played",int(stats_table["Played"].sum() // 2))
# calculates the total number of matches

st.sidebar.metric("Total Goals",int(stats_table["GF"].sum()))
# calculates the total amount of goals

if page == "League Overview":
    st.subheader("Season Overview")
    # gives our webpage the sub heading for the season overview

    st.subheader(f"{selected_season} Premier League Table")
    # adds a heading to our website

    styled_table = stats_table.style.apply(lambda row: ["background-color: #E8C66A" if row["Position"] == 1 else "" for _ in row], axis=1)
    # makes the team in firsts background green

    st.dataframe(styled_table, hide_index=True)
    # displays our data frame as an interactive table

    st.subheader("Points by Team")
    # gives our website another heading

    points_fig = create_points_chart(stats_table)
    st.plotly_chart(points_fig, width="stretch")
    # puts our graph of teams by points on the website

    st.subheader("Goals Scored vs Conceded")
    # gives our website another heading

    goals_fig = create_goals_chart(stats_table)
    st.plotly_chart(goals_fig, width="stretch")
    # puts our graph of goals on the website 
# creates an if statment to display this code when they select league overview

elif page == "Team Analysis":
    st.subheader("Team Analysis")
    # creates a subheader for the team analysis section of our website

    selected_team = st.selectbox("Choose a Premier League team:", team_names)
    # creates an interactive dropdown menu on our website

    st.write("You selected:", selected_team)
    # displays the selection made 

    team_data = stats_table[stats_table["Team"] == selected_team]
    # python checks each team name against the one selected and keeps only the rows where the condition is true 

    st.dataframe(team_data, hide_index=True)
    # displays our selected teams statistics


    team_stats = team_data.iloc[0]
    # extracts the first row as a pandas series

    col1, col2, col3 = st.columns(3)
    # divides our dashboard into three equal-width columns

    with col1:
        st.metric("Points", int(team_stats["Points"]))

    with col2:
        st.metric("Wins", int(team_stats["Wins"]))

    with col3:
        st.metric("Goal Difference", int(team_stats["GD"]))
    # tells python what should appear in each of the columns
# if team analysis is selected then this section will be displayed

elif page == "Team Comparison":
    st.subheader("Team Comparison")
    #creates a heading for the team comparison section on oue website

    col1, col2 = st.columns(2)

    with col1:
        team1 = st.selectbox("Select first team:", team_names)

    with col2:
        team2 = st.selectbox("Select second team:", team_names, index=1)
        # tells pythin what should appear in each of the columns


    if team1 == team2:
        st.warning("Please select two different teams.")
        # ensures people dont pick the same teams and warns them if they do

    else:
        team1_stats = stats_table[stats_table["Team"] == team1].iloc[0]
        team2_stats = stats_table[stats_table["Team"] == team2].iloc[0]
        # extracts the stats of the teams as a series

        comparison_stats = ["Points", "Wins", "Draws", "Losses", "GF", "GA", "GD"]
        # variable containing the list of statistics that we want to compare

        comparison_data = {"Statistic": comparison_stats, team1: [team1_stats[stat] for stat in comparison_stats], team2: [team2_stats[stat] for stat in comparison_stats]}
        # creates a dictionary containing the statistics of both the teams

        comparison_table = pd.DataFrame(comparison_data)
        # converts our dictionary into a pandas table 

        st.dataframe(comparison_table, hide_index=True)
        # displays the table on our website
        
        st.subheader("Visual Team Comparison")

        selected_stat = st.selectbox("Choose a statistic to compare:", comparison_stats)
        # create a dropdown allowing users to select the stat they want to compare

        chart_data = comparison_table[comparison_table["Statistic"] == selected_stat]
        # allows us to store only the row they selected

        comparison_chart = px.bar(chart_data, x=[team1, team2], y="Statistic", orientation="h", barmode="group", title=f"{team1} vs {team2} - {selected_stat}")
        # creates the bar chart where the statistic is on the y-axis and the two teams are on the x-axis

        st.plotly_chart(comparison_chart, width="stretch")
        # displays the chart on our website 
        # if team comparison is selected then this section is displayed

    















