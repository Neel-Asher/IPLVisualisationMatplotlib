from data_loader import load_data
from cleaning import clean_data
from insights import generate_insights
from insights import generate_insights
from transformation import transform_data
from analysis import *
from reporting import *
from export import export_reports
from visualization import *

# Stage 1: Data Ingestion
deliveries_df, matches_df = load_data()
plot_dataset_shapes(deliveries_df, matches_df)

# Stage 2: Data Cleaning
(deliveries_df,matches_df,deliveries_missing_before,matches_missing_before) = clean_data(
    deliveries_df,matches_df)
plot_missing_values(deliveries_missing_before,"Deliveries Dataset Missing Values")
plot_missing_values(matches_missing_before,"Matches Dataset Missing Values")

# Stage 3: Data Transformation
merged_df = transform_data(deliveries_df,matches_df)
plot_total_runs_distribution(merged_df)
print("\nPipeline execution completed successfully.")

# Stage 4: Core Analysis
top_batters_result = top_10_batters(merged_df)
plot_top_batters(top_batters_result)
runs_over_result = runs_per_over(merged_df)
plot_runs_per_over(runs_over_result)
season_result = season_wise_run_trends(merged_df)
plot_season_trends(season_result)
bowler_result = top_bowlers_by_economy(merged_df)
plot_top_bowlers(bowler_result.head(10))
toss_result = toss_match_win_analysis(merged_df)
plot_toss_advantage(toss_result)

# Stage 5: Derived Insights
insight_results = generate_insights(merged_df)
plot_high_scoring_venues(insight_results["venues"])
plot_best_death_over_teams(insight_results["death_teams"])
plot_consistent_batters(insight_results["consistent_batters"])

# Stage 6: Final Reporting
batters_report = top_batters_report(merged_df)

plot_report_barh(
    batters_report,
    x_column="total_runs",
    y_column="batter",
    title="Top Batters Report",
    xlabel="Runs",
    ylabel="Batter"
)

# Stage 7: Data Export
export_reports(merged_df)