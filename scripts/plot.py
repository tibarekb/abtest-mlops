import sys
from turtle import color

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

class Plot:
    def __init__(self) -> None:
        pass
    
    def plot_hist(self,df:pd.DataFrame,column:str,)->None:
        """
            Plot the hist of the column
        """

        sns.displot(data=df, x = column, color = color,kde=True,height=7,aspect=2)
        plt.title(f'Distribution of {column}', size =20, fontweight='bold')
        plt.show()

    