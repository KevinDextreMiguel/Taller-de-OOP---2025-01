import pandas as pd
class Data:
  def __init__(self):
    self.dataFrame = None
  
  def generar(self):
    meses = ["Enero","Febrero","Marzo","Abril"]
    ventas = [30500,35600,28300,33900]
    gastos = [22000,23400,18100,20700]
    dicc = {"mes":meses,"ventas":ventas,"gasto":gastos}
    self.dataFrame = pd.DataFrame(dicc)
  
  def imprimir(self):
    print(self.dataFrame)
  
  def balance(self):
    self.dataFrame["ganancia"] = self.dataFrame["ventas"] - self.dataFrame["gasto"]
    print("\nSe realizò el balance")

  
objetoData = Data()
objetoData.generar()
objetoData.imprimir()
objetoData.balance()
objetoData.imprimir()
