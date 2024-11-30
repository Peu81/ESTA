import pandas as pd
import math
from scipy.stats import shapiro
from scipy.stats import spearmanr
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression


bostonHousing = pd.read_csv('BostonHousing.csv')

colunas = ['rm', 'medv']

for col in colunas:
    data_coluna = bostonHousing[col]
    stat, p_value = shapiro(data_coluna)
    print(f"'{col}': Statistic = {stat}, p-value = {p_value}")

    if p_value > 0.05:
        print(f"{col} é normal")
    else:
        print(f"{col} não é normal")
print("")