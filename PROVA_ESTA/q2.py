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


print("EQUAÇÃO DA REGRESSÃO: ")

print("y1o = -34.67 + 9.1 * x1")
print("-y1 = 34.67 - 9.1 * (x1 + 1)")

print("y2 = -34.67 + 9.1 * x1")
print("-y1 = 34.67 - 9.1 * x1 - 9.1")

print("y2 - y1 = + 9.1")
print("y2 = y1 + 9.1")

#Se aumentarmos em 1 a media do número de quartos, o valor medio aumentará em 9.1 
