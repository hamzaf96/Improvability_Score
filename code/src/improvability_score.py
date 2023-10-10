import pandas as pd
import numpy as np


class ImprovabilityScore:
    """Class responsible for computing the imrovability score that will be used to choose the student that needs help"""

    def __init__(
        self, data: pd.DataFrame, threshold: float = 0.14, main_feat: str = "FinalGrade"
    ) -> None:
        self.data = data
        self.threshold = threshold
        self.improvability_score_list = []
        self.feat_corr = {}
        self.main_feat = main_feat

    def get_high_corr_feature(self):
        """Extact the most correlated feature with the main feature that needs improvement."""
        for i in range(len(self.data.corr()[self.main_feat])):
            if abs(self.data.corr()[self.main_feat].iloc[i]) > self.threshold:
                self.feat_corr[
                    self.data.corr()[self.main_feat].index[i]
                ] = self.data.corr()[self.main_feat].iloc[i]

    def compute_score(self):
        """Compute the Imrprovability Score."""
        for student in self.data[self.feat_corr.keys()].values:
            improvability_score = 0
            for val in range(len(student)):
                if list(self.feat_corr.values())[val] < 0:
                    improvability_score += student[val] / np.max(
                        self.data[list(self.feat_corr)[val]]
                    )
                else:
                    improvability_score += ((-1) * student[val]) / np.max(
                        self.data[list(self.feat_corr)[val]]
                    )
            self.improvability_score_list.append(improvability_score)

    def __call__(self) -> list:
        self.get_high_corr_feature()
        self.compute_score()
        return self.improvability_score_list
