import pandas as pd
import numpy as np

class Data:
  def __init__(self):
    self.__df = pd.read_csv('/content/iris.csv',index_col=0)
    self.__dfCopia = None

  def mostrar(self):
    print(self.__df.head())
  
  def poner_encabezados(self):
    names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
    self.__df.columns = names
    print('Se modificò el encabezado')
  def estadistica_col1(self):
    media = self.__df['sepallength'].mean()
    mediana = self.__df['sepallength'].median()
    desviacion = self.__df['sepallength'].std()
    print(f'La media de la columna sepallength es: {media}')
    print(f'La mediana de la columna sepallength es: {mediana}')
    print(f'La desviación estándar de la columna sepallength es: {desviacion}')
  def copia_matriz(self):
    self.__dfCopia = self.__df.copy()
    cantidad = 30
    indices_nan = np.random.choice(self.__dfCopia.index, cantidad, replace=False)
    columnas_nan  = np.random.choice(self.__dfCopia.columns, cantidad, replace=True)
    for i in range(cantidad):
      self.__dfCopia.loc[indices_nan[i],columnas_nan[i]] = np.nan
    print(self.__dfCopia)
  
  def nan_colmuna2(self):
    nan_sepalwidth = self.__dfCopia['sepalwidth'].isna()
    cantidad_nan = nan_sepalwidth.sum()
    indices = self.__dfCopia[nan_sepalwidth].index.tolist()
    print(f"Cantidad de valores nan en la segunda columna: {cantidad_nan}")
    print(f"Indices de los valores nan en la segunda columna: {indices}")
  
  def filas_sin_nan(self):
    filas_sin_nan = self.__dfCopia.dropna()
    print(filas_sin_nan)
  
  def filtrar(self):
    new_data = self.__df[(self.__df['petallength'] > 1.5) & (self.__df['sepallength'] < 5.0)]
    print(new_data)

obj = Data()
obj.mostrar()
obj.poner_encabezados()
obj.mostrar()
obj.copia_matriz()
obj.nan_colmuna2()
obj.filas_sin_nan()
obj.filtrar()
