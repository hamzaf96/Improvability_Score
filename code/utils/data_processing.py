import pandas as pd
from sklearn.preprocessing import OneHotEncoder


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


def convert_categorical_to_ohe(dataframe: pd.DataFrame) -> pd.DataFrame:
    """convert categorical data into numerical feature using One Hot Encoder

    Args:
        dataframe (pd.DataFrame): initial dataframe

    Returns:
        pd.DataFrame: dataframe with converted categorical into numerical
    """
    # convert categorical data into numerical using ohe
    for col in dataframe.select_dtypes(include="object").columns:
        encoder = OneHotEncoder()
        encoded_category = encoder.fit_transform(
            dataframe[col].array.reshape(-1, 1)
        ).toarray()
        dataframe[col] = encoded_category

    return dataframe


def save_csv(file_path: str, data: pd.DataFrame):
    """_summary_

    Args:
        file_path (str): _description_
        data (pd.DataFrame): _description_
    """
    data.to_csv(file_path, index=False)
    print(f"DataFrame saved as {file_path}")
