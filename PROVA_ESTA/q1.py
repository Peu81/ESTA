import pandas as pd
import math
from scipy.stats import shapiro
from scipy.stats import spearmanr
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression


bostonHousing = pd.read_csv('BostonHousing.csv')

x = bostonHousing['rm'].values.reshape(-1, 1)
y = bostonHousing['medv'].values

modelo = LinearRegression()

modelo.fit(x, y)

predicaoY = modelo.predict(x)

print("coeficiente: ", modelo.coef_[0])
print("intercepto: ", modelo.intercept_)

beta0 = modelo.intercept_
beta1 = modelo.coef_[0]


#y (medv) = beta0 (intercepto) + beta1 (coeficiente) * x1 ('rm') + erro
print(f"Equação da regressão: MEDV = {beta0:.2f} + {beta1:.2f} * RM")

predicao_medv_atual = modelo.intercept_ + (modelo.coef_ * x)
predicao_medv_futura = modelo.intercept_ + (modelo.coef_ * (x + 1))

# print(predicao_medv_atual[0])
# print(predicao_medv_futura[0])

# print(predicao_medv_futura - predicao_medv_atual)

#
#
#
#