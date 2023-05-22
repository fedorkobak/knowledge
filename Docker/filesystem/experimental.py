'''
    Простая программка которая умеет работать с файлами
    для того, чтобы поэкспериментировать по поводу того
    как docker работает с файлами.
'''

import pandas as pd
import numpy as np


data = pd.read_csv("my_datafile.csv")

rand_d = pd.DataFrame(
    np.random.rand(1, 2),
    columns = data.columns
)

pd.concat(
    [data, rand_d], axis=0
).to_csv(
    "my_datafile.csv", index=None
)