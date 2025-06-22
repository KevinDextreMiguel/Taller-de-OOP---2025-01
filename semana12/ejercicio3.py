import pandas as pd
class Data:
  def __init__(self):
    self.df = None
    self.nuevoDF = None
  
  def leer(self):
    self.df = pd.read_excel("cotizacion.xlsx")
    print("Lectura correcta")
  
  def mostrar(self):
    print(self.df)
  
  def estadistica(self):
    """
    self.nuevoDF = self.df.describe()
    resultado = self.nuevoDF.loc[["min","max","mean"]]
    resultado.index = ["Mínimo","Máximo","Promedio"]"""

    self.nuevoDF = self.df.select_dtypes(exclude="object")

    data = {
        "Mínimo":self.nuevoDF.min(),
        "Máximo":self.nuevoDF.max(),
        "Promedio":self.nuevoDF.mean()
    }

    resultado = pd.DataFrame(data)
    resultado = resultado.transpose()
    print(f"\n\n{resultado}")


objetoData = Data()
objetoData.leer()
objetoData.mostrar()
objetoData.estadistica()
