import pandas as pd
# imports pandas library and give it the shorter name of pd

import plotly.express as px
# imports plotly and gives it the shorter name of px


def create_league_table(filename):
    matches = pd.read_csv(filename)
    # creates a function where we tell it what to read

    columns = ["Date","HomeTeam","AwayTeam","FTHG","FTAG","FTR","HS","AS","HST","AST"]
    # stores the names of the columns we want to analyse

    football_data = matches[columns]
    # creates a new dataframe containing the columns we want to analyse

    teams = football_data["HomeTeam"].unique()
    # finds all of the premier league teams

    team_stats = {}

    for team in teams:
        home_wins = football_data[(football_data["HomeTeam"] == team) & (football_data["FTR"] == "H")]
        away_wins =  football_data[(football_data["AwayTeam"] == team) & (football_data["FTR"] == "A")]

        total_wins = len(home_wins) + len(away_wins)
        # calculate total wins for every team

        home_draws = football_data[(football_data["HomeTeam"] == team) & (football_data["FTR"] == "D")]
        away_draws = football_data[(football_data["AwayTeam"] == team) & (football_data["FTR"] == "D")]

        total_draws = len(home_draws) + len(away_draws)
        # calculates total draws for each team

        home_losses = football_data[(football_data["HomeTeam"] == team) & (football_data["FTR"] == "A")]
        away_losses = football_data[(football_data["AwayTeam"] == team) & (football_data["FTR"] == "H")]
        
        total_losses = len(home_losses) + len(away_losses)
        # calculates total losses for each team

        home_matches = football_data[football_data["HomeTeam"] == team]
        away_matches = football_data[football_data["AwayTeam"] == team]
        # makes a DataFrame that contains all the matches here the team where the home or away team respectivley

        home_goals_scored = home_matches["FTHG"].sum()
        away_goals_scored = away_matches["FTAG"].sum()
        # stores the amount of goals scored by the team when at home and away

        total_goals_scored = home_goals_scored + away_goals_scored
        # calculates the total goals scored by a team
        
        home_goals_conceded = home_matches["FTAG"].sum()
        away_goals_conceded = away_matches["FTHG"].sum()
        # stores the amount of goals conceded by the team when at home and away

        total_goals_conceded = home_goals_conceded + away_goals_conceded
        # calculates the total goals conceded by a team

        goal_difference = total_goals_scored - total_goals_conceded
    
        team_stats[team] = {"Wins": total_wins, "Draws": total_draws, "Losses": total_losses, "GF": total_goals_scored, "GA": total_goals_conceded, "GD": goal_difference}
        # tells python to store each team name as a key and another "nested" dictionary as its value which holds the teams stats

    stats_table = pd.DataFrame.from_dict(team_stats, orient="index")
    # creates a table containing all the teams and their corresponding stats 

    stats_table["Played"] = stats_table["Wins"] + stats_table["Draws"] + stats_table["Losses"]
    # creates a column where we can see how many games have been played

    stats_table["Points"] = 3*stats_table["Wins"] + stats_table["Draws"]
    # creates a column where we can calculate the points earned by each team

    stats_table = stats_table.sort_values(by=["Points", "GD", "GF"], ascending=False)
    # sorts all of the teams based off points and then followed by goal difference and goals for

    stats_table = stats_table.reset_index()
    # moves team names into normal columns

    stats_table = stats_table.rename(columns={"index": "Team"})
    # rename the new column from index to Teams

    stats_table.insert(0, "Position", range(1, len(stats_table) + 1))
    # inserts the new column at the beggining called positionand creats columns for the numbers 1 through 20

    column_order = ["Position", "Team", "Points", "Played", "Wins", "Draws", "Losses", "GF", "GA", "GD"]
    stats_table = stats_table[column_order]
    # sorts the columns into a professional

    return stats_table

stats_table = create_league_table("matches.csv")
# we call the funtion and give it the aurgument 


def create_points_chart(stats_table):
    fig = px.bar(stats_table, x="Points", y="Team", orientation="h", color="Points", color_continuous_scale="Reds", title="Premier League - Points by Team")
    # creates a bar chart and then puts points on the x-axis and the team on the y-axis
    # we also tell plotly to plot the bars horizontally
    # we tell it to colour the bars based of points in shades of blue
    # we give the graph the title "Premier League 2025/26"
    
    fig.update_yaxes(autorange="reversed")
    # reverses the order the teams are displayed

    fig.update_layout(height=750)
    # gives the graph more height

    return fig
# a function that we use to create our points graph 

def create_goals_chart(stats_table):
    goals_table = stats_table.sort_values(by="GD", ascending=False)
    # creates a second DataFrame which allows us to sort the data into goal difference order 

    goals_fig = px.bar(goals_table, x=["GF", "GA"], y="Team", orientation="h", barmode="group", hover_data=["GD"], color_discrete_map={"GF": "green", "GA": "red"}, title="Premier League - Goals Scored vs Conceded")
    # creates a second graph comparing goals scored and goals conceded
    # we give plotly two columns to plot and tell it to place them next to eachother rather than on top of eachother
    # we tell it that when hovering over the graph we want to display the goal difference
    # we tell plotly to have the two bars coloured in green and red
     
    goals_fig.update_yaxes(categoryorder="array", categoryarray=goals_table["Team"].tolist(), autorange="reversed")
    # reverses the order the teams are displayed
     
    goals_fig.update_layout(height=750)
    # gives the graph more height

    return goals_fig
# a function to create our graph of goals

def validate_league_table(stats_table):
    calculated_matches = (stats_table["Wins"] + stats_table["Draws"] + stats_table["Losses"])
    # stores the calculated matches in the variable

    assert (stats_table["Played"] == calculated_matches).all()
    # checks wether the matches played is equal to the wins pluss the draws pluss the losses

    calculated_points = (3 * stats_table["Wins"] + stats_table["Draws"])
    # stores the calculated points

    assert (stats_table["Points"] == calculated_points).all()
    # checks the points is calculated correctly

    calculated_gd = stats_table["GF"] - stats_table["GA"]
    # stores the calculated goal difference

    assert (stats_table["GD"] == calculated_gd).all()
    # checks the goal difference is the difference between goals for and goals against

    print("All validation tests passed!")
    # prints a message to confirm they passed the tests
  

if __name__ == "__main__":
    season_files = {"2025/26": "matches.csv", "2024/25": "matches_2024.csv", "2023/24": "matches_2023.csv"}
    # creates a dictionary where each key is a season displayed to the user and eaach value is the CVS filename

    for season, filename in season_files.items():
        print(f"Testing {season}...")

        season_table = create_league_table(filename)

        validate_league_table(season_table)
        # runs the function to execute the testing
# ensures the testing is ran on all of the seasons

    





