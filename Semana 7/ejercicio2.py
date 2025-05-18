class Laptop:
  def __init__(self,marca,procesador,pantalla):
    self.__marca = marca
    self.__procesador = procesador
    self.__pantalla = pantalla
    self.__precioBase = 1000
    self.__precioFinal = 0

  #get
  def getMarca(self):
    return self.__marca
  def getProcesador(self):
    return self.__procesador
  def getPantalla(self):
    return self.__pantalla
  def getPrecioFinal(self):
    return self.__precioFinal

  #set

  def IncrementoMarca(self):
    if self.__marca == 'D':
      return self.__precioBase * 0.2
    elif self.__marca == 'A':
      return self.__precioBase * 0.1
    return 0

  def IncrementoProcesador(self):
    if self.__procesador == 'i5':
      return self.__precioBase * 0.1
    elif self.__procesador == 'i7':
      return self.__precioBase * 0.15
    return 0

  def IncrementoPantalla(self):
    if self.__pantalla == 'táctil':
      return self.__precioBase * 0.05
    return 0

  def calcularPrecioFinal(self):
    self.__precioFinal = self.__precioBase + self.IncrementoMarca() + self.IncrementoProcesador() + self.IncrementoPantalla()

  def __str__(self):
    return f"Marca: {self.__marca}\nProcesador: {self.__procesador}\nPantalla: {self.__pantalla}\nPrecio Base: {self.__precioBase}\nPrecio Final: {self.__precioFinal}"







class Catalogo: # base, manejadora, 
  def __init__(self):
    self.__listaLaptops = []
  
  def agregarLaptop(self,objetoLaptop):
    objetoLaptop.calcularPrecioFinal()
    self.__listaLaptops.append(objetoLaptop)

  def mostrar(self):
    for laptop in self.__listaLaptops:
      print('=================================')
      print(laptop)
  
  def ordenarPorPrecio(self):
    aux = []
    for laptop in self.__listaLaptops:   
      aux2 = [laptop.getPrecioFinal(),laptop.getMarca(),laptop.getProcesador(),laptop.getPantalla()]
      aux.append(aux2)
    aux.sort(reverse=True)
    for i in aux:
      print(i)

  def mostrarXMarcaYProcesador(self,marca,procesador):
    for laptop in self.__listaLaptops:
      if laptop.getMarca() == marca and laptop.getProcesador() == procesador:
        print('=================================')
        print(laptop)

  def CantidadTipoProcesador(self):
    i3 = 0
    i5 = 0
    i7 = 0
    for laptop in self.__listaLaptops:
      if laptop.getProcesador() == 'i3':
        i3 += 1
      elif laptop.getProcesador() == 'i5':
        i5 += 1
      else:
        i7 += 1
    print(f"i3: {i3}\ni5: {i5}\ni7: {i7}")





def opciones():
  print('1: Registrar las computadoras ')
  print('2: Listar todas las computadoras, ordenadas por precio final de mayor a menor')
  print('3: Listar por marca y el procesador')
  print('4: Un reporte por tipo de procesador')
  print('5: Mostrar todos')
  print('6: Salir')
  opcion = -1
  while opcion < 1 or opcion > 6:
    try:
      opcion = int(input("opcion: "))
    except:
      print("opcion incorrecta")
  return opcion

def main():
  objetoCatalogo = Catalogo()
  while True:
    opcion = opciones()
    if opcion == 1:
      marca = input("marca: ")
      procesador = input("procesador: ")
      pantalla = input("pantalla: ")
      objetoLaptop = Laptop(marca,procesador,pantalla)
      objetoCatalogo.agregarLaptop(objetoLaptop)
    elif opcion == 2:
      objetoCatalogo.ordenarPorPrecio()
    elif opcion == 3:
      marca = input("marca: ")
      procesador = input("procesador: ")
      objetoCatalogo.mostrarXMarcaYProcesador(marca,procesador)
    elif opcion == 4:
      objetoCatalogo.CantidadTipoProcesador()
    elif opcion == 5:
      objetoCatalogo.mostrar()
    else:
      break


main()
