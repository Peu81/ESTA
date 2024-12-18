import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([5, 20, 14, 32, 22, 38])

modelo = LinearRegression()
modelo.fit(x, y)
predicaoY = modelo.predict(x)

print(modelo.coef_)
print(modelo.intercept_)
print("Predição de Y: ",predicaoY)


rSq = modelo.score(x,y)
print(rSq)

ssr = sum(np.square(predicaoY - y))
print(ssr)

