import pandas as pd


def clean_data(deliveries_df, matches_df):

    deliveries_missing_before = deliveries_df.isnull().sum()
    matches_missing_before = matches_df.isnull().sum()

    matches_df["winner"] = matches_df["winner"].fillna("No Result")
    matches_df["player_of_match"] = matches_df["player_of_match"].fillna("Not Awarded")

    deliveries_df.columns = deliveries_df.columns.str.lower().str.strip()
    matches_df.columns = matches_df.columns.str.lower().str.strip()

    deliveries_match_ids = set(deliveries_df["match_id"].unique())
    matches_ids = set(matches_df["id"].unique())

    valid_match_ids = deliveries_match_ids.intersection(matches_ids)

    print("Valid Match IDs:", len(valid_match_ids))

    return (
        deliveries_df,
        matches_df,
        deliveries_missing_before,
        matches_missing_before
    )