import matplotlib.pyplot as plt

def plot_dataset_shapes(deliveries_df, matches_df):

    dataset_names = ["Deliveries", "Matches"]

    row_counts = [
        deliveries_df.shape[0],
        matches_df.shape[0]
    ]

    plt.figure(figsize=(8, 5))

    plt.bar(dataset_names, row_counts)

    plt.title("Dataset Size Comparison")
    plt.xlabel("Dataset")
    plt.ylabel("Number of Rows")

    plt.show()

import matplotlib.pyplot as plt


def plot_missing_values(missing_series, title):

    missing_series = missing_series[missing_series > 0]

    if missing_series.empty:
        print(f"No missing values in {title}")
        return

    plt.figure(figsize=(10, 5))

    plt.bar(
        missing_series.index,
        missing_series.values
    )

    plt.title(title)
    plt.xlabel("Columns")
    plt.ylabel("Missing Values")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()

def plot_total_runs_distribution(merged_df):

    run_counts = (
        merged_df["total_runs"]
        .value_counts()
        .sort_index()
    )

    plt.figure(figsize=(10, 5))

    plt.bar(
        run_counts.index,
        run_counts.values
    )

    plt.title("Distribution of Runs Per Ball")

    plt.xlabel("Runs Scored")
    plt.ylabel("Frequency")

    plt.xticks(run_counts.index)

    plt.tight_layout()

    plt.show()


def plot_top_batters(result):

    plt.figure(figsize=(10, 6))

    plt.barh(
        result.index,
        result.values
    )

    plt.title("Top 10 Batters")
    plt.xlabel("Runs")
    plt.ylabel("Batters")

    plt.gca().invert_yaxis()

    plt.tight_layout()

    plt.show()

def plot_runs_per_over(result):

    plt.figure(figsize=(10, 5))

    plt.plot(
        result.index,
        result.values,
        marker="o"
    )

    plt.title("Average Runs Per Over")

    plt.xlabel("Over")
    plt.ylabel("Average Runs")

    plt.grid(True)

    plt.xticks(range(1, 21))

    plt.show()

def plot_season_trends(result):

    plt.figure(figsize=(12, 5))

    plt.plot(
        result.index.astype(str),
        result.values,
        marker="o"
    )

    plt.title("Season Wise Total Runs")

    plt.xlabel("Season")
    plt.ylabel("Total Runs")

    plt.xticks(rotation=45)

    plt.grid(True)

    plt.tight_layout()

    plt.show()

def plot_top_bowlers(result):

    plt.figure(figsize=(10, 6))

    plt.barh(
        result.index,
        result["economy"]
    )

    plt.title("Top Bowlers by Economy")

    plt.xlabel("Economy Rate")
    plt.ylabel("Bowler")

    plt.gca().invert_yaxis()

    plt.tight_layout()

    plt.show()

def plot_toss_advantage(result):

    plt.figure(figsize=(6, 6))

    plt.pie(
        result.values,
        labels=result.index,
        autopct="%1.1f%%"
    )

    plt.title("Toss Advantage")

    plt.show()

def plot_boundary_analysis(total_fours, total_sixes):

    labels = ["Fours", "Sixes"]
    values = [total_fours, total_sixes]

    plt.figure(figsize=(6, 6))

    plt.pie(
        values,
        labels=labels,
        autopct="%1.1f%%"
    )

    plt.title("Boundary Distribution")

    plt.show()

def plot_high_scoring_venues(venue_runs):

    plt.figure(figsize=(12, 6))

    plt.barh(
        venue_runs.index,
        venue_runs.values
    )

    plt.title("Top High-Scoring Venues")

    plt.xlabel("Average Runs")
    plt.ylabel("Venue")

    plt.gca().invert_yaxis()

    plt.tight_layout()

    plt.show()

def plot_best_death_over_teams(result):

    plt.figure(figsize=(10, 6))

    plt.barh(
        result.index,
        result.values
    )

    plt.title("Best Death Over Teams")

    plt.xlabel("Runs Scored (Overs 16-20)")
    plt.ylabel("Team")

    plt.gca().invert_yaxis()

    plt.tight_layout()

    plt.show()

def plot_consistent_batters(result):

    plt.figure(figsize=(10, 6))

    plt.barh(
        result.index,
        result["average_runs"]
    )

    plt.title("Most Consistent Batters")

    plt.xlabel("Average Runs Per Match")
    plt.ylabel("Batter")

    plt.gca().invert_yaxis()

    plt.tight_layout()

    plt.show()