import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def vis_corr_map(data: pd.DataFrame):
    """_summary_

    Args:
        data (pd.DataFrame): _description_
    """
    # visualize the correlation map
    plt.figure(figsize=(20, 15))
    sns.heatmap(data.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=1)
    plt.title("Correlation Heatmap")
    plt.show()


def vis_distribution_data(data: pd.DataFrame):
    """_summary_

    Args:
        data (pd.DataFrame): _description_
    """
    plt.figure(figsize=(10, 8))
    sns.displot(data)
    plt.title("Distribution of the data")
    plt.show()
