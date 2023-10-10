import pandas as pd
from Improvability_Score.code.src.improvability_score import ImprovabilityScore


def test_improvability_score():
    # Sample data in a Pandas DataFrame
    data = pd.DataFrame(
        {"X": [1, 2, 3, 4, 5], "Y": [10, 12, 5, 8, 3], "FinalGrade": [20, 5, 15, 8, 2]}
    )
    improvability_score = ImprovabilityScore(data=data)
    improvability_score_list = improvability_score()
    assert isinstance(improvability_score_list, list)
    assert len(improvability_score_list) > 0
