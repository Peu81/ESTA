from math import *
import numpy as np
from statistics import *
from matplotlib.pyplot import *
from matplotlib.dates import *
from seaborn import *
from pandas import *
from scipy.stats import *

#Inferência estatística

#tirar conclusões acerca de um ou mais parâmetros de uma população a partir de uma amostra

#x barra: média amostral / M = média populacional
#S^2: variância amostral / a^2 = variância populacional
#P^ = x/n: proporção amostral / P: proporção populacional

#ERRO PADRÃO: EP(xbarra) = S/sqrt(n = x amostra)


# dados = array([41.60, 41.48, 42.34, 41.95, 41.86, 42.18, 41.72, 42.26, 41.81, 42.04])
# #condutividade termica do aço em btu/h ft - F

# erro_padrao = (dados.std(ddof=1)) / sqrt(len(dados))
# print(f"Erro Padrão: {erro_padrao:.2f}")
# print()

# media_dados = dados.mean()
# print(f"Média dos dados: {media_dados:.2f}")
# print()

# #MARGEM DE ERRO
# erro_para_menos = media_dados - 3* erro_padrao
# erro_para_mais = media_dados + 3* erro_padrao  
# print(f"Margem de erro: [{erro_para_menos:.2f}, {erro_para_mais:.2f}]")


#BOOTSTRAP: n amostras simuladas

# bootsample = np.random.choice(dados, size=10, replace=True)
# print(f"Teste: {bootsample}")


#tempo de resposta (em horas) de processamento do pedido de emprestimo

#para cada bootsample, calcular a média, armazena em uma lista

# for i in range(0, 201):
#     bootsample2 = np.random.choice(dados2, size=10, replace=True)
#     lista_medias2.append(bootsample2.mean())

# print(lista_medias)

# bootmean = mean(lista_medias)
# print(bootmean)

# bootstd = np.std(lista_medias)
# print(bootstd)

dados2 = array([24.1514, 27.4145, 20.4000, 22.5151, 28.5152, 28.5611, 21.2489, 20.9983, 24.9840, 22.6245])

erro_padrao2 = (dados2.std(ddof=1)) / sqrt(len(dados2))
print(f"Erro Padrão: {erro_padrao2:.2f}")
print()

media_dados2 = dados2.mean()
print(f"Média dos dados: {media_dados2:.2f}")
print()

#MARGEM DE ERRO
erro_para_menos2 = media_dados2 - 3* erro_padrao2
erro_para_mais2 = media_dados2 + 3* erro_padrao2 
print(f"Margem de erro: [{erro_para_menos2:.2f}, {erro_para_mais2:.2f}]")



lista_medias2 = []

for i in range(0, 201):
    bootsample2 = np.random.choice(dados2, size=10, replace=True)
    lista_medias2.append(bootsample2.mean())

bootmean2 = mean(lista_medias2)
print(bootmean2)

bootstd2 = np.std(lista_medias2)
print(bootstd2)
