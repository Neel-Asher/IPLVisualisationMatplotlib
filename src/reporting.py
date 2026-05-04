import pandas as pd

def top_batters_report(df):

    report = (
        df.groupby("batter")["batsman_runs"]
        .sum()
        .reset_index()
    )

    report.columns = [
        "batter",
        "total_runs"
    ]

    report = report.sort_values(
        by="total_runs",
        ascending=False
    ).head(10)

    print("TOP BATTERS REPORT")

    print("\nTOP BATTERS REPORT")
    print(report.to_string(index=False))

    return report

def top_bowlers_report(df):

    report = (
        df.groupby("bowler")
        .agg(
            runs_conceded=("total_runs", "sum"),
            balls=("ball", "count")
        )
        .reset_index()
    )

    report["overs"] = report["balls"] / 6

    report["economy_rate"] = (
        report["runs_conceded"] /
        report["overs"]
    )

    report = report[
        [
            "bowler",
            "runs_conceded",
            "overs",
            "economy_rate"
        ]
    ]

    report = report.sort_values(
        by="economy_rate"
    ).head(10)

    print("TOP BOWLERS REPORT")

    print(report)

    return report

def venue_report(df):

    report = (
        df.groupby("venue")
        .agg(
            total_matches=("match_id", "nunique"),
            average_runs=("total_runs", "mean")
        )
        .reset_index()
    )

    report = report.sort_values(
        by="average_runs",
        ascending=False
    )

    print("VENUE REPORT")

    print(report.head(10))

    return report

def team_performance_report(df):

    report = (
        df.groupby("batting_team")
        .agg(
            total_runs=("total_runs", "sum"),
            total_matches=("match_id", "nunique")
        )
        .reset_index()
    )

    report["average_runs_per_match"] = (
        report["total_runs"] /
        report["total_matches"]
    )

    report = report.sort_values(
        by="average_runs_per_match",
        ascending=False
    )

    print("TEAM PERFORMANCE REPORT")

    print(report)

    return report

def season_report(df):

    report = (
        df.groupby("season")
        .agg(
            total_runs=("total_runs", "sum"),
            total_matches=("match_id", "nunique")
        )
        .reset_index()
    )

    report["average_runs_per_match"] = (
        report["total_runs"] /
        report["total_matches"]
    )

    report = report.sort_values(
        by="season"
    )

    print("SEASON REPORT")

    print(report)

    return report