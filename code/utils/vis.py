import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go


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


def vis_scatter_data(data: pd.DataFrame, x: str, y: str, label: str):
    """_summary_

    Args:
        data (pd.DataFrame): _description_
        x (str): _description_
        y (str): _description_
        Label (str): _description_

    Returns:
        _type_: _description_
    """ """"""
    # Create a Plotly scatter plot
    fig = go.Figure()
    # Create an interactive scatter plot with tooltips
    # Add scatter trace with labels as tooltips
    fig.add_trace(
        go.Scatter(
            x=data[x],
            y=data[y],
            text=data[label],
            hoverinfo="x+y+text",  # Show text as tooltips on hover
            marker=dict(size=10),
            mode="markers",  # Only show markers
        )
    )
    # fig = px.scatter(data, x=x, y=y, text=label)

    # Customize the figure (optional)
    fig.update_traces(textposition="top center")
    fig.update_layout(title="Scatter Plot with Hover Information")

    return fig
