def generate_insights(df):

    print("\n" + "=" * 70)
    print("STAGE 5 — DERIVED INSIGHTS")
    print("=" * 70)

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

    consistency = consistency[
        consistency["matches"] >= 30
    ]

    top_batter = consistency.sort_values(
        by="average_runs",
        ascending=False
    ).head(1)

    batter_name = top_batter.index[0]
    average_runs = top_batter.iloc[0]["average_runs"]

    print("\nMOST CONSISTENT BATTER")
    print(top_batter)

    print(
        f"\nINSIGHT: {batter_name} appears to be the most "
        f"consistent batter with an average of "
        f"{average_runs:.2f} runs per match."
    )

    death_overs = df[df["over"] >= 16]

    death_team = (
        death_overs.groupby("batting_team")["total_runs"]
        .sum()
        .sort_values(ascending=False)
        .head(1)
    )

    team_name = death_team.index[0]
    total_runs = death_team.iloc[0]

    print("\nBEST DEATH OVER TEAM")
    print(death_team)

    print(
        f"\nINSIGHT: {team_name} has been the strongest "
        f"death-over batting team with "
        f"{total_runs} runs scored in overs 16–20."
    )

    venue_runs = (
        df.groupby("venue")["total_runs"]
        .mean()
        .sort_values(ascending=False)
        .head(5)
    )

    print("\nHIGH SCORING VENUES")
    print(venue_runs)

    top_venue = venue_runs.index[0]
    avg_runs = venue_runs.iloc[0]

    print(
        f"\nINSIGHT: {top_venue} appears to be the highest "
        f"scoring venue with an average of "
        f"{avg_runs:.2f} runs per ball/event."
    )

    powerplay = df[df["over"] <= 6]

    powerplay_team = (
        powerplay.groupby("batting_team")["total_runs"]
        .sum()
        .sort_values(ascending=False)
        .head(1)
    )

    pp_team = powerplay_team.index[0]
    pp_runs = powerplay_team.iloc[0]

    print("\nBEST POWERPLAY TEAM")
    print(powerplay_team)

    print(
        f"\nINSIGHT: {pp_team} has demonstrated aggressive "
        f"powerplay batting with "
        f"{pp_runs} runs scored in the first six overs."
    )

    boundaries = df[
        df["batsman_runs"].isin([4, 6])
    ]

    top_boundary_player = (
        boundaries.groupby("batter")
        .size()
        .sort_values(ascending=False)
        .head(1)
    )

    player = top_boundary_player.index[0]
    count = top_boundary_player.iloc[0]

    print("\nTOP BOUNDARY PLAYER")
    print(top_boundary_player)

    print(
        f"\nINSIGHT: {player} has hit the most boundaries "
        f"in the dataset with "
        f"{count} boundary shots."
    )

    dot_balls = df[df["total_runs"] == 0]

    top_bowler = (
        dot_balls.groupby("bowler")
        .size()
        .sort_values(ascending=False)
        .head(1)
    )

    bowler = top_bowler.index[0]
    dots = top_bowler.iloc[0]

    print("\nDOT BALL SPECIALIST")
    print(top_bowler)

    print(
        f"\nINSIGHT: {bowler} has bowled the highest "
        f"number of dot balls ({dots}), indicating "
        f"strong run containment ability."
    )

    print("\n" + "=" * 70)
    print("INSIGHT GENERATION COMPLETED")
    print("=" * 70)

    return {
        "consistent_batters": consistency.sort_values(
            by="average_runs",
            ascending=False
        ).head(10),

        "death_teams": death_overs.groupby(
            "batting_team"
        )["total_runs"].sum().sort_values(
            ascending=False
        ).head(10),

        "venues": venue_runs
    }