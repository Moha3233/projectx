import pandas as pd

class FeatureEncoder:
    def __init__(self, aa_file):
        self.aa_data = pd.read_csv(aa_file)

    def encode_sequence(self, sequence):
        features = []
        for aa in sequence:
            row = self.aa_data[self.aa_data["code"] == aa]
            if not row.empty:
                features.append(row.iloc[0].to_dict())
        return pd.DataFrame(features)
