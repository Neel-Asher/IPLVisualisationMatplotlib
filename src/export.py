import os
import pandas as pd


def export_reports(df):

    os.makedirs("../output", exist_ok=True)
    os.makedirs("../output/charts", exist_ok=True)

    print("\n" + "=" * 60)
    print("EXPORTING REPORTS")
    print("=" * 60)

    runs_per_match = (
        df.groupby("match_id")["total_runs"]
        .sum()
        .reset_index()
    )

    runs_per_match.columns = [
        "match_id",
        "total_runs"
    ]

    runs_per_match.to_csv(
        "../output/runs_per_match.csv",
        index=False
    )

    top_batters = (
        df.groupby("batter")["batsman_runs"]
        .sum()
        .reset_index()
    )

    top_batters.columns = [
        "batter",
        "total_runs"
    ]

    top_batters = top_batters.sort_values(
        by="total_runs",
        ascending=False
    )

    top_batters.to_csv(
        "../output/top_batters.csv",
        index=False
    )

    strike_rate = (
        df.groupby("batter")
        .agg(
            runs=("batsman_runs", "sum"),
            balls=("ball", "count")
        )
        .reset_index()
    )

    strike_rate["strike_rate"] = (
        strike_rate["runs"] /
        strike_rate["balls"]
    ) * 100

    strike_rate.to_csv(
        "../output/strike_rate.csv",
        index=False
    )

    economy = (
        df.groupby("bowler")
        .agg(
            runs_conceded=("total_runs", "sum"),
            balls=("ball", "count")
        )
        .reset_index()
    )

    economy["overs"] = economy["balls"] / 6

    economy["economy_rate"] = (
        economy["runs_conceded"] /
        economy["overs"]
    )

    economy.to_csv(
        "../output/economy.csv",
        index=False
    )

    team_scores = (
        df.groupby(
            ["match_id", "batting_team"]
        )["total_runs"]
        .sum()
        .reset_index()
    )

    team_scores.to_csv(
        "../output/team_scores.csv",
        index=False
    )

    death_overs = (
        df[df["over"] >= 16]
        .groupby("batting_team")["total_runs"]
        .sum()
        .reset_index()
    )

    death_overs.to_csv(
        "../output/death_overs.csv",
        index=False
    )

    with pd.ExcelWriter(
        "../output/ipl_analysis.xlsx"
    ) as writer:

        runs_per_match.to_excel(
            writer,
            sheet_name="Runs Per Match",
            index=False
        )

        top_batters.to_excel(
            writer,
            sheet_name="Top Batters",
            index=False
        )

        strike_rate.to_excel(
            writer,
            sheet_name="Strike Rate",
            index=False
        )

        economy.to_excel(
            writer,
            sheet_name="Economy",
            index=False
        )

        team_scores.to_excel(
            writer,
            sheet_name="Team Scores",
            index=False
        )

        death_overs.to_excel(
            writer,
            sheet_name="Death Overs",
            index=False
        )

    print("\nAll reports exported successfully.")

    print("\nFiles saved in output/ directory.")