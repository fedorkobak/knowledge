import pandas as pd
from typing import Literal
import matplotlib.pyplot as plt

def plot_Q_scatter(
    x: pd.Series,
    y: pd.Series,
    c: pd.Series,
    sep_orient: Literal["h", "v"] | None = None, 
    sep_val: float | None = None,
    arrange: tuple[float, float, float, float] | None = None
):
    '''
    Plot scatter with given separation.
    '''
    if arrange is None:
        arrange = (x.min(), x.max(), y.min(), y.max())

    plt.scatter(x=x, y=y, c=c)
    plt.xlim(arrange[0], arrange[1]); plt.ylim(arrange[2], arrange[3])
    plt.xlabel(x.name);plt.ylabel(y.name)

    if (sep_orient is not None) and (sep_val is not None):
        if sep_orient == 'h':
            plt.axhline(y=sep_val, color="gray", linestyle="--")
            x_text_left, y_text_left, x_text_right, y_text_right = (
                (arrange[1] + arrange[0]) / 2, 
                (arrange[2] + sep_val) / 2,
                (arrange[1] + arrange[0]) / 2,
                (arrange[3] + sep_val) / 2,
            )
        else:
            plt.axvline(x=sep_val, color="gray", linestyle="--")
            x_text_left, y_text_left, x_text_right, y_text_right = (
                (arrange[0] + sep_val) / 2, 
                (arrange[3] + arrange[2]) / 2,
                (arrange[1] + sep_val) / 2,
                (arrange[3] + arrange[2]) / 2,
            )

        plt.text(
            x=x_text_left, 
            y=y_text_left,
            s="$Q^{left}$", 
            fontdict={"size": 20}
        )
        plt.text(
            x=x_text_right, 
            y=y_text_right,
            s="$Q^{right}$", 
            fontdict={"size": 20}
        )