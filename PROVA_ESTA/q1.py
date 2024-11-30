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
stat_rm_medv, p_valor_stat_rm_medv = spearmanr(bostonHousing['rm'], bostonHousing['medv'])
print("Correlação de spearmanr entre 'rm' e 'medv': ")
if p_valor_stat_rm_medv < 0.05:
    print(f"são correlacionados.\n")
else:
    print(f"não são correlacionados.\n")
print("estatistica: ", stat_rm_medv)
print("p-valor: ", p_valor_stat_rm_medv)

# Realizando inicialmente o teste de shapiro-wilk para obter a normalidade de cada coluna (rm e medv)
# foram encontrados valores muito menores que 0.05, o que implica na anormalidade das amostras.
# Sabendo disso, realizei o teste de correlação de spearman e como conclusão, provou-se que há
# uma relação direta entre o número de quartos (rm) e o valor médio das casas.