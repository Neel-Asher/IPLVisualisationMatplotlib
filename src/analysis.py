import pandas as pd

def total_runs_per_match(df):

    result = (
        df.groupby("match_id")["total_runs"]
        .sum()
        .sort_values(ascending=False)
    )

    return result.head()

def runs_per_team_per_match(df):

    result = (
        df.groupby(["match_id", "batting_team"])["total_runs"]
        .sum()
    )

    return result.head()

def top_10_batters(df):

    result = (
        df.groupby("batter")["batsman_runs"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    return result

def strike_rate(df):

    batter_stats = (
        df.groupby("batter")
        .agg(
            runs=("batsman_runs", "sum"),
            balls=("ball", "count")
        )
    )

    batter_stats["strike_rate"] = (
        batter_stats["runs"] / batter_stats["balls"]
    ) * 100

    result = batter_stats.sort_values(
        by="strike_rate",
        ascending=False
    )

    return result.head(10)

def top_bowlers_by_economy(df):

    bowler_stats = (
        df.groupby("bowler")
        .agg(
            runs_conceded=("total_runs", "sum"),
            balls=("ball", "count")
        )
    )

    bowler_stats["overs"] = bowler_stats["balls"] / 6

    bowler_stats["economy"] = (
        bowler_stats["runs_conceded"] /
        bowler_stats["overs"]
    )

    result = bowler_stats.sort_values(
        by="economy"
    )

    return result.head(10)

def most_consistent_batters(df):

    batter_match_runs = (
        df.groupby(["batter", "match_id"])["batsman_runs"]
        .sum()
        .reset_index()
    )

    consistency = (
        batter_match_runs.groupby("batter")
        .agg(
            average_runs=("batsman_runs", "mean"),
            matches=("match_id", "nunique")
        )
    )

    result = consistency[
        consistency["matches"] >= 30
    ].sort_values(
        by="average_runs",
        ascending=False
    )

    return result.head(10)

def highest_individual_score(df):

    batter_scores = (
        df.groupby(["match_id", "batter"])["batsman_runs"]
        .sum()
        .reset_index()
    )

    result = batter_scores.sort_values(
        by="batsman_runs",
        ascending=False
    )

    return result.head(10)

def boundary_analysis(df):

    boundaries = df[
        (df["batsman_runs"] == 4) |
        (df["batsman_runs"] == 6)
    ]

    total_fours = (boundaries["batsman_runs"] == 4).sum()
    total_sixes = (boundaries["batsman_runs"] == 6).sum()

    top_players = (
        boundaries.groupby("batter")
        .size()
        .sort_values(ascending=False)
    )

    print("\nBOUNDARY ANALYSIS")
    print(f"Total 4s: {total_fours}")
    print(f"Total 6s: {total_sixes}")

    return top_players.head(10), total_fours, total_sixes

def boundary_percentage(df):

    total_runs = (
        df.groupby("batter")["batsman_runs"]
        .sum()
    )

    boundary_runs = (
        df[df["batsman_runs"].isin([4, 6])]
        .groupby("batter")["batsman_runs"]
        .sum()
    )

    percentage = (
        (boundary_runs / total_runs) * 100
    ).sort_values(ascending=False)

    return percentage.head(10)

def dot_ball_analysis(df):

    dot_balls = df[df["total_runs"] == 0]

    result = (
        dot_balls.groupby("bowler")
        .size()
        .sort_values(ascending=False)
    )

    return result.head(10)  

def runs_per_over(df):

    result = (
        df.groupby("over")["total_runs"]
        .mean()
    )

    return result

def powerplay_performance(df):

    powerplay = df[df["over"] <= 6]

    result = (
        powerplay.groupby("batting_team")["total_runs"]
        .sum()
        .sort_values(ascending=False)
    )

    return result.head(10)

def death_overs_performance(df):

    death = df[df["over"] >= 16]

    teams = (
        death.groupby("batting_team")["total_runs"]
        .sum()
        .sort_values(ascending=False)
    )

    batters = (
        death.groupby("batter")["batsman_runs"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\nBEST TEAMS IN DEATH OVERS")
    print(teams.head(10))

    return batters.head(10)

def run_distribution_per_inning(df):

    inning_runs = (
        df.groupby("inning")["total_runs"]
        .mean()
    )

    return inning_runs

def toss_impact_analysis(df):

    toss_analysis = (
        df.groupby("toss_winner")
        .agg(
            total_runs=("total_runs", "sum")
        )
        .sort_values(by="total_runs", ascending=False)
    )

    return toss_analysis.head(10)

def toss_match_win_analysis(df):

    matches = df[
        ["match_id", "toss_winner", "winner"]
    ].drop_duplicates()

    matches["toss_advantage"] = (
        matches["toss_winner"] == matches["winner"]
    )

    result = (
        matches["toss_advantage"]
        .value_counts(normalize=True) * 100
    )

    return result

def player_of_match_contribution(df):

    player_runs = (
        df.groupby(["match_id", "batter"])["batsman_runs"]
        .sum()
        .reset_index()
    )

    top_scorers = (
        player_runs.sort_values(
            ["match_id", "batsman_runs"],
            ascending=[True, False]
        )
        .drop_duplicates("match_id")
    )

    pom = (
        df[
            ["match_id", "player_of_match"]
        ]
        .drop_duplicates()
    )

    comparison = pom.merge(
        top_scorers,
        left_on=["match_id", "player_of_match"],
        right_on=["match_id", "batter"],
        how="left"
    )

    result = comparison[
        [
            "match_id",
            "player_of_match",
            "batsman_runs"
        ]
    ]

    return result.head(20)

def venue_wise_analysis(df):

    venue_matches = (
        df.groupby("venue")["match_id"]
        .nunique()
    )

    venue_runs = (
        df.groupby("venue")["total_runs"]
        .mean()
    )
    return venue_matches.sort_values(ascending=False).head(10), venue_runs.sort_values(ascending=False).head(10)

def city_wise_scoring(df):

    result = (
        df.groupby("city")["total_runs"]
        .mean()
        .sort_values(ascending=False)
    )

    return result.head(10)

def season_wise_run_trends(df):

    result = (
        df.groupby("season")["total_runs"]
        .sum()
        .sort_values()
    )

    return result

def winning_team_analysis(df):

    inning_scores = (
        df.groupby(
            ["match_id", "inning", "batting_team"]
        )["total_runs"]
        .sum()
        .reset_index()
    )

    first_innings = inning_scores[
        inning_scores["inning"] == 1
    ]

    second_innings = inning_scores[
        inning_scores["inning"] == 2
    ]

    merged = first_innings.merge(
        second_innings,
        on="match_id",
        suffixes=("_1", "_2")
    )

    merged["predicted_winner"] = merged.apply(
        lambda row:
        row["batting_team_1"]
        if row["total_runs_1"] > row["total_runs_2"]
        else row["batting_team_2"],
        axis=1
    )

    actual_winners = (
        df[
            ["match_id", "winner"]
        ]
        .drop_duplicates()
    )

    final = merged.merge(
        actual_winners,
        on="match_id"
    )

    final["prediction_correct"] = (
        final["predicted_winner"] == final["winner"]
    )

    accuracy = (
        final["prediction_correct"]
        .mean() * 100
    )

    print("\nWINNING TEAM ANALYSIS")
    print(f"Prediction Accuracy: {accuracy:.2f}%")

    return final[
        [
            "match_id",
            "predicted_winner",
            "winner",
            "prediction_correct"
        ]
    ].head(10)  