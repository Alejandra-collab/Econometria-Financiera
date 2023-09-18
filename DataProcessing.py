# # ___________________________________________________
# __________ ECONOMETRÍA FINANCIERA: TALLER 1 _________
# _____________________________________________________
# _____________________________________________________
# 
#
# a. Dos empresas en la SEC que cotizan en la NYSE:
# NFLX, AMZN

# Módulos:
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy
import os
import importlib
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis, chi2
from pandas_datareader import data as wb
import datetime as dt 
from datetime import date
from pylab import * # Importamos todas las funciones de pylab
import yfinance as yf
import openpyxl

# b. Activos de Yahoo Finance:
# - Nu Bank (NU)
# - Urban Outfitters Inc. (URBN)
# - CureVac N.V. (CVAC)
# - Corporacion America Airports SA (CAAP)
# - Best Buy Co Inc (BBY)
#
# 1. Elegí esas 5 empresas porque he invertido en las primeras 3 y tenía 
# pensado invertir en CAAP y BBY pronto. He estado usando TD Ameritrade
# para analizar los activos, a través de los fundamentales de la
# empresa y he hecho un poco de trading también. He usado reportes
# financieros e índices financieros.
# En principio me atrajo los resultados financieros de las empresas, pero
# me gustaría enfocarme en un solo sector para poder especializarme.
#
# 2. Analizmos 5 aactvos que corizanen la NYSE

start = dt.datetime(2022, 9, 14)
end = dt.datetime(2023, 9, 14)

# Elegimos los equity que necesitamos:
tickers = ['NU', 'URBN', 'CVAC', 'CAAP', 'BBY']

# Descargamos y guardamos los datos en una carpeta existente:
output_folder = "C:\\Users\\LENOVO\\Desktop\\ParaGuardar\\py\\Econometria-Financiera\\data"

for ticker in tickers:
    # Obtenemos el historial de precios
    ticker_obj = yf.Ticker(ticker)
    data = ticker_obj.history(period='1y')
    data.index = data.index.tz_localize(None)
    # ELiminamos las columnas que no necesitamos:
    data = data.drop(['Open', 'High', 'Low', 'Volume', 'Dividends', 'Stock Splits'], axis = 1)
    # Cambiamos el formato de Date a fecha y Close a número
    data['Date'] = pd.to_datetime(data.index.date)
    data['Close'] = data['Close'].astype(float)
    # Imprimimos los primeros registros para verificar que todo esté bien
    print(data.head())
    # Guardamos los datos en un archivo Excel
    excel_filename = os.path.join(output_folder, f'HistoricalData_{ticker}.xlsx')
    data.to_excel(excel_filename)

# Eliminamos las columnas que no necesitamos
type(data['Date'])

# Creamos una lista para agregar los DataFrames de los archivos Excel
dataframes = []

# Iteramos a través de los archivos en la carpeta
for filename in os.listdir(output_folder):
    if filename.endswith(".xlsx"):
        file_path = os.path.join(output_folder, filename)
        df = pd.read_excel(file_path)
        dataframes.append(df)

# 
for df in dataframes:
    df['Date'] = pd.to_datetime(df['Date'])
    df['Close_previous'] = df['Close'].shift(1)
    df.sort_values(by='Date', ascending=True, inplace=True)

# Guardamos los Excel modificados
for i, df in enumerate(dataframes):
    output_file = os.path.join(output_folder, f'Modified_{i+1}.xlsx')
    df.to_excel(output_file, index=False)


# Calculamos los retornos
t['Return_close'] = t['Close']/t['Close_previous']-1

# Eliminamos los Na
t = t.dropna()

# Dado que se eliminaqron los NaN, los ìndices se modificaron
t = t.reset_index(drop = True)

# 2. Plot timeseries of prices
plt.figure()
plt.plot(t['Date'], t['Close'])
plt.title('Timeseries Close ' + ric)
plt.show()

# 3. Plot returns
plt.figure()
plt.plot(t['Date'], t['Return_close'])
plt.title('Timeseries Returns ' + ric)
plt.show()

#



ric = 'DBK.DE'
path = 'C:\\Users\\LENOVO\\Desktop\\Para guardar\\py\\python-for-finance\\data\\' + ric +'.csv'
table_raw = pd.read_csv(path)
# Create table of returns
t = pd.DataFrame()
t['Date'] = pd.to_datetime(table_raw['Date'], dayfirst=False) # Convertir la columna Date a fecha
t['Close'] = table_raw['Close']
t.sort_values(by = 'Date', ascending = True)
t['close_previous'] = table_raw['Close'].shift(1)
t['return_close'] = t['Close']/t['close_previous'] - 1 # Calculando los retornos
t = t.dropna() # Eliminar los Na
t = t.reset_index(drop = True) # Dado que se eliminaron Na's, los índices se modificaron

# Plot timeseries of prices
plt.figure()
plt.plot(t['Date'], t['Close'])
plt.title('Timeseries real prices ' + ric)
plt.show()

# input for Jarque-Bera test
x = t['return_close'].values # Guardamos los retornos como un array of float
x_str = 'Real returns ' + ric # label e.g. ric
x_size = t['return_close'].shape[0] # size of returns

# Compute risk metrics -----------------------------------------------
x_mean = np.mean(x) # Media
x_std = np.std(x) # volatilidad






#





# Visualizamos y trabajamos con los datos:
data.tail(5)
close_eqty = data['Close']

plt.plot(close_eqty)
plt.show()

# 3.
# Calculo de retornos
ret_eqty = np.log(close_eqty) - np.log(close_eqty.shift(1))
ret_eqty_1 = ret_eqty.dropna()

# Verificamos que no tengamos datos nulos
ret_eqty_1.isnull().sum()

plt.plot(ret_eqty_1)
plt.show()

# 4.
x_std = np.std(x)

