import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def vis_corr_map(data: pd.DataFrame):
    """_summary_

    Args:
        data (pd.DataFrame): _description_
    """
    # visualize the correlation map
    fig, _ = plt.subplots(figsize=(20, 15))
    sns.heatmap(data.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=1)
    plt.title("Correlation Heatmap")
    return fig


def vis_distribution_data(data: pd.DataFrame):
    """_summary_

    Args:
        data (pd.DataFrame): _description_
    """
    fig, _ = plt.subplots(figsize=(10, 8))
    sns.displot(data)
    plt.title("Distribution of the data")
    plt.show()
    return fig


def vis_scatter_data(x: pd.Series, y: pd.Series):
    """_summary_

    Args:
        X (pd.Series): _description_
        Y (pd.Series): _description_
    """
    # Create a scatter plot with Seaborn
    sns.set(style="whitegrid")  # Set the plot style
    fig, ax = plt.subplots(figsize=(8, 6))  # Set the figure size

    # Create the scatter plot
    scatter = ax.scatter(x=x, y=y, marker="o", color="blue", s=50, label="Student")

    # Add labels and a legend
    plt.xlabel(x.name)
    plt.ylabel(y.name)
    # plt.title('Insights on Students that needs help')

    # Customize the appearance further
    sns.despine(left=True, bottom=True)  # Remove the spines
    plt.grid(True, linestyle="--", alpha=0.6)  # Add grid lines
    plt.legend()

    return fig, scatter
