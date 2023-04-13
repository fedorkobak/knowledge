import pandas as pd

data = pd.read_csv("example.csv", index_col=0)
data.mean().to_csv("means.csv")