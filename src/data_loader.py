import pandas as pd

def load_data():
    deliveries_df = pd.read_csv("../data/deliveries.csv")
    matches_df = pd.read_csv("../data/matches.csv")

    return deliveries_df, matches_df