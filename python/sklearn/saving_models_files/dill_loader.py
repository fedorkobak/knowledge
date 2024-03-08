import dill
import numpy as np

try:
    with open("dilled_other_module_transformer.pkl", "rb") as f:
        transformer_loaded = dill.load(f)
    print(transformer_loaded.fit_transform(np.array([[2],[3],[4]])))
except Exception as e:
    print("Got exception:", e)
