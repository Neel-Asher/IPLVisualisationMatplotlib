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