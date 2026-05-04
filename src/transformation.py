def transform_data(deliveries_df, matches_df):

    deliveries_df["total_runs"] = (
        deliveries_df["batsman_runs"] +
        deliveries_df["extra_runs"]
    )

    merged_df = deliveries_df.merge(
        matches_df,
        left_on="match_id",
        right_on="id",
        how="inner"
    )

    return merged_df