class Encomienda:
  __diccEncomienda = {}

  def __init__(self, codigo, remitente, destinatario,direccionEntrega,pesokg,volumenm3,costokg,costom3 ):
    self.__codigo = codigo
    self.__remitente = remitente
    self.__destinatario = destinatario
    self.__direccionEntrega = direccionEntrega
    self.__pesokg = pesokg
    self.__volumenm3 = volumenm3
    self.__costokg = costokg
    self.__costom3 = costom3

  #get
  @property
  def codigo(self):
    return self.__codigo
  @property
  def remitente(self):
    return self.__remitente
  @property
  def destinatario(self):
    return self.__destinatario
  @property
  def direccionEntrega(self):
    return self.__direccionEntrega
  @property
  def pesokg(self):
    return self.__pesokg
  @property
  def volumenm3(self):
    return self.__volumenm3
  @property
  def costokg(self):
    return self.__costokg
  @property
  def costom3(self):
    return self.__costom3

  #set
  @codigo.setter
  def codigo(self, codigo):
    self.__codigo = codigo
  @remitente.setter
  def remitente(self, remitente):
    self.__remitente = remitente
  @destinatario.setter
  def destinatario(self, destinatario):
    self.__destinatario = destinatario
  @direccionEntrega.setter
  def direccionEntrega(self, direccionEntrega):
    self.__direccionEntrega = direccionEntrega
  @pesokg.setter
  def pesokg(self, pesokg):
    self.__pesokg = pesokg
  @volumenm3.setter
  def volumenm3(self, volumenm3):
    self.__volumenm3 = volumenm3
  @costokg.setter
  def costokg(self, costokg):
    self.__costokg = costokg
  @costom3.setter
  def costom3(self, costom3):
    self.__costom3 = costom

  def costoPorPeso(self):
    return self.__pesokg * self.__costokg
  def costoPorVolumen(self):
    return self.__volumenm3 * self.__costom3
  def valorEnvio(self):
    return self.costoPorPeso() + self.costoPorVolumen()
  
  def imprimir(self):
    print(self.__remitente)
    print(self.__destinatario)
    print(self.__direccionEntrega)
    print(self.__pesokg)
    print(self.__volumenm3)
    print(self.__costokg)
    print(self.__costom3)
    print(f'valor Envio: {self.valorEnvio()}')

  def agregar(self,objetoEncomienda):
    if objetoEncomienda.codigo in self.__diccEncomienda:
      print("El código ya existe")
    else:
      self.__diccEncomienda[self.__codigo] = objetoEncomienda
      print('Agregado')
  
  def mostrar(self):
    for clave,valor in self.__diccEncomienda.items():
      print(f'================={clave}================')
      valor.imprimir()




obj1 = Encomienda("1","remitente1","destinatario1","direccionEntrega1",10,1,1,1)
obj2 = Encomienda("2","remitente2","destinatario2","direccionEntrega2",2,2,2,2)
obj3 = Encomienda("3","remitente3","destinatario3","direccionEntrega3",20,32,42,52)

obj1.agregar(obj1)
obj2.agregar(obj2)
obj3.agregar(obj3)

obj1.mostrar()
