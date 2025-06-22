import pandas as pd
class Data:
  def __init__(self):
    self.df = None
  
  def leer(self):
    self.df = pd.read_csv("titanic.csv",sep=";")

  def dimension(self):
    print("Dimensiones: ",self.df.shape)#tupla(filas,columnas)
    print("Número de datos: ",self.df.size)
    print("Nombres de columnas: ",self.df.columns)
    print("Nombres de filas: ",self.df.index)
    print("Tipos de datos: ",self.df.dtypes)
  
  def mostrar_primeras_filas(self):
    print(self.df.head())
  
  def mostrar_ultimas_filas(self):
    print(self.df.tail())

  def mostrar_pasejero_id(self,id):
    filtro = self.df["PassengerId"] == id
    resultado = self.df[filtro]
    print(f"\n\nLos datos para el pasajero con id: {id}:\n{resultado}")

  def filas_pares(self):
    resultado = self.df.iloc[::2]
    print(f"\n\nLos datos de las filas pares\n{resultado}")

  def nombres_primera_clase(self):
    filtro = self.df["Pclass"] == 1
    resultado = self.df[filtro].sort_values("Name")
    print(f"\n\nNombres de las personas de la primera clase, ordenados:\n{resultado}")

  def porcentaje_sobrevivientes(self):
    resultado = self.df["Survived"].value_counts(normalize=True)*100
    print(f"\n\nPorcentaje de personas que sobrevivieron:\n{resultado}")
 
  def porcentaje_sobrevivientes_clase(self):
    resultado = self.df.groupby("Pclass")["Survived"].value_counts(normalize=True)*100
    print(f"\n\nPorcentaje de personas que sobrevivieron por clase:\n{resultado}")
  
  def eliminar_edad_desconocida(self):
    self.df.dropna(subset=["Age"])
    print(f"\n\nSe eliminò los datos con edad desconocida")
  
  def edad_media_mujeres_clase(self):
    filtro = self.df["Sex"] == "female"
    resultado = self.df[filtro].groupby("Pclass")["Age"].mean()
    print(f"\n\nLa edad media de las mujeres por clase es:\n{resultado}")

  def add_columna_bool(self):
    self.df["MenorEdad"] = self.df["Age"] < 18
    print(f"\n\nColumna añadida correctamente")
    print(f"\n\n{self.df}")
  
  def porcentaje_menores_mayores_clase(self):
    df_sobrevivientes = self.df[self.df["Survived"] == 1]
    conteo = df_sobrevivientes.groupby(["Pclass", "MenorEdad"]).size()
    total_por_clase = df_sobrevivientes.groupby(["Pclass", "MenorEdad"]).size()
    porcentaje = conteo / total_por_clase * 100
    print(f"\n\nPorcentaje de menores y mayores por clase:\n{porcentaje}")
  
  

objetoData = Data()
objetoData.leer()
objetoData.dimension()
objetoData.mostrar_primeras_filas()
objetoData.mostrar_ultimas_filas()
objetoData.mostrar_pasejero_id(148)
objetoData.filas_pares()
objetoData.nombres_primera_clase()
objetoData.porcentaje_sobrevivientes()
objetoData.porcentaje_sobrevivientes_clase()
objetoData.eliminar_edad_desconocida()
objetoData.edad_media_mujeres_clase()
objetoData.add_columna_bool()
objetoData.porcentaje_menores_mayores_clase()
