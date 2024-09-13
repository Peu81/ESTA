import numpy as NP
import statistics as sts
import matplotlib.pyplot as plt
import seaborn as SNS
import pandas as pd



barra = '-' * 25

def Coluna_SepalLengthCm():
    Iris = pd.read_csv('Iris.csv')
    media_SLC = Iris['SepalLengthCm'].mean()

    print("A média de Iris['SepalLengthCm'] é:", media_SLC)
    print(barra)


    #Mediana -> NP.median(dados)
    print("MEDIANA")
    print(barra)

    mediana_SLC = NP.median(Iris['SepalLengthCm'])

    print("A mediana de Stock['Open']:", mediana_SLC)
    print(barra)


    #HISTOGRAMA IRIS[SEPALLENGTHCM]
    min_open = Iris['SepalLengthCm'].min()
    print(min_open)
    print(barra)
    max_open = Iris['SepalLengthCm'].max()
    print(max_open)
    print(barra)

    plt.hist(Iris['SepalLengthCm'], 4, (4, 8))
    plt.show()

    #BOXPLOT IRIS[SEPALLENGTHCM]
    SNS.boxplot(Iris['SepalLengthCm'])
    plt.show()

    #OUTLIERS IRIS[SEPALLENGTHCM]
    x = Iris['SepalLengthCm'].mean()
    ponto_corte = Iris['SepalLengthCm'].std(ddof=1)*3
    inf, sup = x - ponto_corte, x + ponto_corte

    outliers = Iris['SepalLengthCm'][(Iris['SepalLengthCm']<inf) | (Iris['SepalLengthCm']>sup)]
    print(f'OUTLIERS: {outliers}')


def Coluna_SepalWidthCm():
    Iris = pd.read_csv('Iris.csv')
    media_SWC = Iris['SepalWidthCm'].mean()

    print("A média de Iris['SepalWidthCm'] é:", media_SWC)
    print(barra)


    #Mediana -> NP.median(dados)
    print("MEDIANA")
    print(barra)

    mediana_SWC = NP.median(Iris['SepalWidthCm'])

    print("A mediana de Stock['Open']:", mediana_SWC)
    print(barra)


    #HISTOGRAMA IRIS[SEPALWIDTHCM]
    min_SWC = Iris['SepalWidthCm'].min()
    print(min_SWC)
    print(barra)
    max_SWC = Iris['SepalWidthCm'].max()
    print(max_SWC)
    print(barra)

    plt.hist(Iris['SepalWidthCm'], 4, (2, 4))
    plt.show()

    #BOXPLOT IRIS[SEPALWIDTHCM]
    SNS.boxplot(Iris['SepalWidthCm'])
    plt.show()

    #OUTLIERS IRIS[SEPALWIDTHCM]
    x = Iris['SepalWidthCm'].mean()
    ponto_corte = Iris['SepalWidthCm'].std(ddof=1)*3
    inf, sup = x - ponto_corte, x + ponto_corte

    outliers = Iris['SepalWidthCm'][(Iris['SepalWidthCm']<inf) | (Iris['SepalWidthCm']>sup)]
    print(f'OUTLIERS: {outliers}')


def Coluna_PetalLengthCm():
    Iris = pd.read_csv('Iris.csv')
    media_PLC = Iris['PetalLengthCm'].mean()

    print("A média de Iris['PetalLengthCm'] é:", media_PLC)
    print(barra)


    #Mediana -> NP.median(dados)
    print("MEDIANA")
    print(barra)

    mediana_PLC = NP.median(Iris['PetalLengthCm'])

    print("A mediana de Stock['PetalLengthCm']:", mediana_PLC)
    print(barra)


    #HISTOGRAMA IRIS[PETHALLENGTHCM]
    min_PLC = Iris['PetalLengthCm'].min()
    print(min_PLC)
    print(barra)
    max_PLC = Iris['PetalLengthCm'].max()
    print(max_PLC)
    print(barra)

    plt.hist(Iris['PetalLengthCm'], 7, (1, 7))
    plt.show()

    #BOXPLOT IRIS[PETHALLENGTHCM]
    SNS.boxplot(Iris['PetalLengthCm'])
    plt.show()

    #OUTLIERS IRIS[PETHALLENGTHCM]
    x = Iris['PetalLengthCm'].mean()
    ponto_corte = Iris['PetalLengthCm'].std(ddof=1)*3
    inf, sup = x - ponto_corte, x + ponto_corte

    outliers = Iris['PetalLengthCm'][(Iris['PetalLengthCm']<inf) | (Iris['PetalLengthCm']>sup)]
    print(f'OUTLIERS: {outliers}')

def Coluna_PetalWidthCm():
    Iris = pd.read_csv('Iris.csv')
    media_PWC = Iris['PetalWidthCm'].mean()

    print("A média de Iris['PetalWidthCm'] é:", media_PWC)
    print(barra)


    #Mediana -> NP.median(dados)
    print("MEDIANA")
    print(barra)

    mediana_PWC = NP.median(Iris['PetalWidthCm'])

    print("A mediana de Stock['PetalWidthCm']:", mediana_PWC)
    print(barra)


    #HISTOGRAMA IRIS[PETHALWIDTHCM]
    min_PWC = Iris['PetalWidthCm'].min()
    print(min_PWC)
    print(barra)
    max_PWC = Iris['PetalWidthCm'].max()
    print(max_PWC)
    print(barra)

    plt.hist(Iris['PetalWidthCm'], 4, (0.1, 2.5))
    plt.show()

    #BOXPLOT IRIS[PETHALWIDTHCM]
    SNS.boxplot(Iris['PetalWidthCm'])
    plt.show()

    #OUTLIERS IRIS[PETHALWIDTHCM]
    x = Iris['PetalWidthCm'].mean()
    ponto_corte = Iris['PetalWidthCm'].std(ddof=1)*3
    inf, sup = x - ponto_corte, x + ponto_corte

    outliers = Iris['PetalWidthCm'][(Iris['PetalWidthCm']<inf) | (Iris['PetalWidthCm']>sup)]
    print(f'OUTLIERS: {outliers}')




def menu():
    print(f'MENU\n 1-Coluna SepalLengthCm.\n 2-Coluna SepalWidthCm.\n 3- Coluna PetalLengthCm.\n 4- Coluna PetalWidthCm.')

    opcao = int(input('Digite a opção: '))
    while True:
        if opcao == 1:
            Coluna_SepalLengthCm()
            break
        if opcao == 2:
            Coluna_SepalWidthCm()
            break
        if opcao == 3:
            Coluna_PetalLengthCm()
            break

        if opcao == 4:
            Coluna_PetalWidthCm()
            break

menu()