from data_loader import load_data
from cleaning import clean_data
from visualization import *

# Stage 1: Data Ingestion
deliveries_df, matches_df = load_data()
plot_dataset_shapes(deliveries_df, matches_df)

# Stage 2: Data Cleaning
(deliveries_df,matches_df,deliveries_missing_before,matches_missing_before) = clean_data(
    deliveries_df,matches_df)
plot_missing_values(deliveries_missing_before,"Deliveries Dataset Missing Values")
plot_missing_values(matches_missing_before,"Matches Dataset Missing Values")