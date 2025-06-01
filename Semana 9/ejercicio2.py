class Terreno:
  __diccTerreno = {}

  def __init__(self, codigo, ubicacion, area,valorComercialm2,valorPredialM2):
    self.__codigo = codigo
    self.__ubicacion = ubicacion
    self.__area = area
    self.__valorComercialm2 = valorComercialm2
    self.__valorPredialM2 = valorPredialM2
  
  def valorPredial(self):
    return self.__area * self.__valorPredialM2
  def valorComercial(self):
    return self.__area * self.__valorComercialm2
  def margenGanancia(self):
    return self.valorComercial() - self.valorPredial()
  
  def agregar(self,objetoTerreno):
    if objetoTerreno.codigo in self.__diccTerreno:
      print("El código ya existe")
    else:
      self.__diccTerreno[self.__codigo] = objetoTerreno
      print('Agregado')
  
  def imprimir(self):
    print(self.__ubicacion)
    print(self.__area)
    print(self.__valorComercialm2)
    print(self.__valorPredialM2)
    print(f'Valor Predial: {self.valorPredial()}')
    print(f'Valor Comercial: {self.valorComercial()}')
    print(f'Margen de Ganancia: {self.margenGanancia()}')
  
  def mostrarTodos(self):
    for clave,valor in self.__diccTerreno.items():
      print(f'=================================')
      print(f'Código: {clave}')
      valor.imprimir()
  

  #get
  @property
  def codigo(self):
    return self.__codigo
  @property
  def ubicacion(self):
    return self.__ubicacion
  @property
  def area(self):
    return self.__area
  @property
  def valorComercialm2(self):
    return self.__valorComercialm2
  @property
  def valorPredialM2(self):
    return self.__valorPredialM2

  #set
  @codigo.setter
  def codigo(self, codigo):
    self.__codigo = codigo
  @ubicacion.setter
  def ubicacion(self, ubicacion):
    self.__ubicacion = ubicacion
  @area.setter
  def area(self, area):
    self.__area = area
  @valorComercialm2.setter
  def valorComercialm2(self, valorComercialm2):
    self.__valorComercialm2 = valorComercialm2
  @valorPredialM2.setter
  def valorPredialM2(self, valorPredialM2):
    self.__valorPredialM2 = valorPredialM2



obj1 = Terreno("1234","ubicacion1",10,10,1)
obj1.agregar(obj1)
obj2 = Terreno("2789","ubicacion2",2,20,2)
obj2.agregar(obj2)
obj3 = Terreno("3331","ubicacion3",20,52,42)
obj3.agregar(obj3)

obj1.mostrarTodos()
