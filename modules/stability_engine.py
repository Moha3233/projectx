import numpy as np

class StabilityEngine:
    def __init__(self):
        pass

    def calculate_stability(self, feature_df):
        hydrophobic_score = feature_df["hydrophobicity"].sum()
        charge_penalty = abs(feature_df["charge"].sum()) * 2

        stability_score = hydrophobic_score - charge_penalty
        normalized_score = 1 / (1 + np.exp(-stability_score/50))

        return normalized_score, stability_score
