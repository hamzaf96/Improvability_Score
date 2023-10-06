import pandas as pd


def remove_duplicate(dataframe: pd.DataFrame) -> pd.DataFrame:
    """remove duplicated rows in dataframe

    Args:
        dataframe (pd.DataFrame): initial dataframe

    Returns:
        pd.DataFrame: datafame with no duplicate rows
    """
    # checking the duplicate values in the data
    duplicate_values = dataframe.duplicated().sum()
    print(f"The data contains {duplicate_values} duplicate values")

    # drop the duplicated values in the dataset
    dataframe = dataframe.drop_duplicates()
    print(f"New dataset shape {dataframe.shape}")

    return dataframe


def remove_nan_values(dataframe: pd.DataFrame) -> pd.DataFrame:
    """remove NaN values from dataframe

    Args:
        dataframe (pd.DataFrame): initial dataframe

    Returns:
        pd.DataFrame: datafame with no NaN values
    """
    # checking the NaN values in the data
    nan_values = dataframe.isna().sum()
    print("The data NaN values:", nan_values)

    # remove NaN values in the dataset
    dataframe = dataframe.dropna()
    print(f"New dataset shape {dataframe.shape}")

    return dataframe


def convert_categorical_to_ohe(df: pd.DataFrame) -> pd.DataFrame:
    """_summary_

    Args:
        df (pd.DataFrame): _description_

    Returns:
        pd.DataFrame: _description_
    """
    pass
