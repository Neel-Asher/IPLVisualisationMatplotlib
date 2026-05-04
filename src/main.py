from data_loader import load_data
from visualization import plot_dataset_shapes

# Stage 1: Data Ingestion
deliveries_df, matches_df = load_data()
print("Deliveries Shape:", deliveries_df.shape)
print("Matches Shape:", matches_df.shape)
print("\nDeliveries Columns:")
print(deliveries_df.columns)
print("\nMatches Columns:")
print(matches_df.columns)
print("\nDeliveries Data Types:")
print(deliveries_df.dtypes)
print("\nMatches Data Types:")
print(matches_df.dtypes)
plot_dataset_shapes(deliveries_df, matches_df)

