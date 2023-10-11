import pandas as pd
from Improvability_Score.code.src.improvability_score import ImprovabilityScore
from Improvability_Score.code.utils.data_processing import (
    convert_categorical_to_ohe,
    remove_duplicate,
    remove_nan_values,
)


def test_improvability_score():
    # Sample data in a Pandas DataFrame
    data = pd.DataFrame(
        {"X": [1, 2, 3, 4, 5], "Y": [10, 12, 5, 8, 3], "FinalGrade": [20, 5, 15, 8, 2]}
    )
    improvability_score = ImprovabilityScore(data=data)
    improvability_score_list = improvability_score()
    assert isinstance(improvability_score_list, list)
    assert len(improvability_score_list) > 0


def test_convert_categorical_to_ohe():
    # Sample data in a Pandas DataFrame
    data = pd.DataFrame(
        {"X": [1, 2, 3, 4, 5], "Y": [10, 12, 5, 8, 3], "FinalGrade": [20, 5, 15, 8, 2]}
    )
    assert isinstance(convert_categorical_to_ohe(data), pd.DataFrame)


def test_remove_duplicate():
    # Sample data in a Pandas DataFrame
    data = pd.DataFrame(
        {"X": [1, 2, 3, 4, 5], "Y": [10, 12, 5, 8, 3], "FinalGrade": [20, 5, 15, 8, 2]}
    )
    assert isinstance(remove_duplicate(data), pd.DataFrame)


def test_remove_nan_values():
    # Sample data in a Pandas DataFrame
    data = pd.DataFrame(
        {"X": [1, 2, 3, 4, 5], "Y": [10, 12, 5, 8, 3], "FinalGrade": [20, 5, 15, 8, 2]}
    )
    assert isinstance(remove_nan_values(data), pd.DataFrame)
