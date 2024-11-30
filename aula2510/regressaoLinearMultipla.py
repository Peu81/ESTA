import pandas as pd
import math
from scipy.stats import shapiro
from scipy.stats import spearmanr
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression


stockdata = pd.read_csv('stock_data.csv')

#y = close
# x = high, low e open

colunas = ['Close','High', 'Low', 'Open']

# for col in colunas:
#     data_coluna = stockdata[col]
#     stat, p_value = shapiro(data_coluna)
#     print(f"'{col}': Statistic = {stat}, p-value = {p_value}")

#     if p_value > 0.05:
#         print(f"{col} é normal")
#     else:
#         print(f"{col} não é normal")


stat_close_high, p_valor_stat_close_high = spearmanr(stockdata['Close'], stockdata['High'])
print("Correlação de spearmanr entre 'close' e 'high': ")
if p_valor_stat_close_high < 0.05:
    print(f"são correlacionados.\n")
else:
    print(f"não são correlacionados.\n")

stat_close_low, p_valor_stat_close_low = spearmanr(stockdata['Close'], stockdata['Low'])
print("Correlação de spearmanr entre 'close' e 'low': ")
if p_valor_stat_close_low < 0.05:
    print(f"são correlacionados.\n")
else:
    print(f"não são correlacionados.\n")

stat_close_open, p_valor_stat_close_open = spearmanr(stockdata['Close'], stockdata['Open'])
print("Correlação de spearmanr entre 'close' e 'high': ")
if p_valor_stat_close_open < 0.05:
    print(f"são correlacionados.\n")
else:
    print(f"não são correlacionados.\n")


x = stockdata[['High', 'Low', 'Open']]
y = stockdata[['Close']]

model = LinearRegression()
model.fit(x, y)

print(f"interceptos: {model.intercept_}")
print(f"Coeficientes: {model.coef_}")
print(f"R-Squared: {model.score(x, y)}")

y1 = (0.78 * 41.22) + (0.76 * 38.79) - (0.53 * 39.69)

print(y1)

#1/3/2006,39.69,41.22,38.79,40.91,24232729,AABA