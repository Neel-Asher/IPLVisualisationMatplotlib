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