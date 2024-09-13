import numpy as NP
import statistics as sts
import matplotlib.pyplot as plt
import seaborn as SNS
import pandas as pd

barra = '-' * 25




def coluna_open():
    Stock = pd.read_csv('stock_data.csv')
    media_open = Stock['Open'].mean()

    print("A média de Stock['Open'] é:", media_open)
    print(barra)


    #Mediana -> NP.median(dados)
    print("MEDIANA")
    print(barra)

    mediana_open = NP.median(Stock['Open'])

    print("A mediana de Stock['Open]:", mediana_open)
    print(barra)


    #HISTOGRAMA STOCK[OPEN]
    min_open = Stock['Open'].min()
    print(min_open)
    print(barra)
    max_open = Stock['Open'].max()
    print(max_open)
    print(barra)

    plt.hist(Stock['Open'], 5, (9, 73))
    plt.show()

    #BOXPLOT SOTCK[OPEN]
    SNS.boxplot(Stock['Open'])
    plt.show()

    #OUTLIERS STOCK[OPEN]
    x = Stock['Open'].mean()
    ponto_corte = Stock['Open'].std(ddof=1)*3
    inf, sup = x - ponto_corte, x + ponto_corte

    outliers = Stock['Open'][(Stock['Open']<inf) | (Stock['Open']>sup)]
    
    print(f'OUTLIERS: \n{outliers}')


def coluna_high():
    Stock = pd.read_csv('stock_data.csv')

    media_high = Stock['High'].mean()

    print("A média de Stock['High'] é:", media_high)
    print(barra)


    #Mediana -> NP.median(dados)
    print("MEDIANA")
    print(barra)

    mediana_high = NP.median(Stock['High'])

    print("A mediana de Stock['High]:", mediana_high)
    print(barra)


    #HISTOGRAMA STOCK[HIGH]
    min_high = Stock['High'].min()
    print(min_high)
    print(barra)
    max_high = Stock['High'].max()
    print(max_high)
    print(barra)

    plt.hist(Stock['High'], 5, (9, 73))
    plt.show()

    #BOXPLOT SOTCK[HIGH]
    SNS.boxplot(Stock['High'])
    plt.show()

    #OUTLIERS STOCK[HIGH]
    x = Stock['High'].mean()
    ponto_corte = Stock['High'].std(ddof=1)*3
    inf, sup = x - ponto_corte, x + ponto_corte

    outliers = Stock['High'][(Stock['High']<inf) | (Stock['High']>sup)]
    print(f'OUTLIERS: \n{outliers}')


def coluna_low():

    Stock = pd.read_csv('stock_data.csv')

    media_low = Stock['Low'].mean()

    print("A média de Stock['Low'] é:", media_low)
    print(barra)


    #Mediana -> NP.median(dados)
    print("MEDIANA")
    print(barra)

    mediana_low = NP.median(Stock['Low'])

    print("A mediana de Stock['Low']:", mediana_low)
    print(barra)


    #HISTOGRAMA STOCK[LOW]
    min_low = Stock['Low'].min()
    print(min_low)
    print(barra)
    max_low = Stock['Low'].max()
    print(max_low)
    print(barra)

    plt.hist(Stock['Low'], 5, (9, 73))
    plt.show()

    #BOXPLOT SOTCK[LOW]
    SNS.boxplot(Stock['Low'])
    plt.show()

    #OUTLIERS STOCK[LOW]
    x = Stock['Low'].mean()
    ponto_corte = Stock['Low'].std(ddof=1)*3
    inf, sup = x - ponto_corte, x + ponto_corte

    outliers = Stock['Low'][(Stock['Low']<inf) | (Stock['Low']>sup)]
    print(f'OUTLIERS: \n{outliers}')


def coluna_close():

    Stock = pd.read_csv('stock_data.csv')

    media_close = Stock['Close'].mean()

    print("A média de Stock['Close'] é:", media_close)
    print(barra)


    #Mediana -> NP.median(dados)
    print("MEDIANA")
    print(barra)

    mediana_close = NP.median(Stock['Close'])

    print("A mediana de Stock['Close']:", mediana_close)
    print(barra)


    #HISTOGRAMA STOCK[CLOSE]
    min_close = Stock['Close'].min()
    print(min_close)
    print(barra)
    max_close = Stock['Close'].max()
    print(max_close)
    print(barra)

    plt.hist(Stock['Close'], 5, (9, 73))
    plt.show()

    #BOXPLOT SOTCK[CLOSE]
    SNS.boxplot(Stock['Close'])
    plt.show()

    #OUTLIERS STOCK[CLOSE]
    x = Stock['Close'].mean()
    ponto_corte = Stock['Close'].std(ddof=1)*3
    inf, sup = x - ponto_corte, x + ponto_corte

    outliers = Stock['Close'][(Stock['Close']<inf) | (Stock['Close']>sup)]
    print(f'OUTLIERS: \n{outliers}')

def menu():
    print(f'MENU\n 1-Coluna Open.\n 2-Coluna High.\n 3- Coluna Low.\n 4- Coluna Close.')

    opcao = int(input('Digite a opção: '))
    while True:
        if opcao == 1:
            coluna_open()
            break
        if opcao == 2:
            coluna_high()
            break
        if opcao == 3:
            coluna_low()
            break

        if opcao == 4:
            coluna_close()
            break

menu()





#TEOREMAS PARA IDENTIFICAR OUTLIERS
#REGRA EMPIRICA: SÓ PODE SER UTILIZADA QUANDO A DISTRIBUIÇÃO É NORMAL
#TEOREMA DE CHEBSITEN: DISTRIBUIÇÃO ASSIMETRICA


