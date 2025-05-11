class Cliente:
    def __init__(self, dni, nombre, direccion, numero_telefono,correo, clientePreferente):
        self.__dni = dni
        self.__nombre = nombre
        self.__direccion = direccion
        self.__numero_telefono = numero_telefono
        self.__correo = correo
        self.__clientePreferente = clientePreferente

    #get
    def get_dni(self):
        return self.__dni
    def get_nombre(self):
        return self.__nombre
    def get_direccion(self):
        return self.__direccion
    def get_numero_telefono(self):
        return self.__numero
    def get_correo(self):
        return self.__correo
    def get_clientePreferente(self):
        return self.__clientePreferente
    
    #set
    def set_dni(self, value):
        self.__dni = value
    def set_nombre(self, value):
        self.__nombre = value
    def set_direccion(self, value):
        self.__direccion = value
    def set_numero_telefono(self, value):
        self.__numero_telefono = value
    def set_correo(self, value):
        self.__correo = value
    def set_clientePreferente(self, value):
        self.__clientePreferente = value

    def __str__(self):
        return f"{self.__dni}\t{self.__nombre}\t{self.__direccion}\t{self.__numero_telefono}\t{self.__correo}\t{self.__clientePreferente}"




class baseCLientes:
  def __init__(self):
    self.listaClientes = []
  
  def registrarCliente(self,objetoCliente):
    self.listaClientes.append(objetoCliente)
  
  def actualizarCliente(self,dni,objetoNuevo):
    for i in range(len(self.listaClientes)):
      if self.listaClientes[i].get_dni() == dni:
        self.listaClientes[i] = objetoNuevo
  
  def eliminarCliente(self,dni):
    for cliente in self.listaClientes:
      if cliente.get_dni() == dni:
        self.listaClientes.remove(cliente)
        print('Cliente eliminado')
    
        
  def mostrar(self):
    print('DNI\tNombre\tDirección\tTeléfono\tCorreo\tPreferente')
    for cliente in self.listaClientes:
      print(cliente)

  def buscarClienteNombre(self,nombre):
    print('DNI\tNombre\tDirección\tTeléfono\tCorreo\tPreferente')
    for cliente in self.listaClientes:
      if cliente.get_nombre() == nombre:
         print(cliente)





def pedirOpcion():
  print('(1) Añadir cliente: ')
  print('(2) Buscar cliente: ')
  print('(3) Actualizar cliente: ')
  print('(4) Eliminar cliente: ')
  print('(5) Listar todos los clientes: ')
  print('(6) Terminar: ')
  opcion = -1
  while opcion < 1 or opcion > 6:
    try:
      opcion = int(input('Ingrese una opción: '))
    except ValueError:
      print('Error, solo valores numéricos')
  return opcion


def pedir_datos(caso="ingresar",dni="123"):
  if caso == "ingresar":
    dni = ''
    while len(dni) != 8 or not dni.isdigit():
      dni = input('Ingrese el dni: ')
      if len(dni) != 8:
        print('Error, el dni debe tener 8 dígitos')
  nombre = input('Ingrese el nombre: ')
  direccion = input('Ingrese la dirección: ')
  numero_telefono = input('Ingrese el número de teléfono: ')
  correo = nombre + '@empsac.com'
  clientePreferente = bool(int(input('Ingrese si es cliente preferente (si: 1, no:0): ')))
  cliente = Cliente(dni, nombre, direccion, numero_telefono, correo, clientePreferente)
  return cliente


def menu():
  objetoBaseCLientes = baseCLientes()
  opcion = -1
  while opcion != 6:
    opcion = pedirOpcion()
    match opcion:
      case 1:
        cliente = pedir_datos()
        objetoBaseCLientes.registrarCliente(cliente)
      case 2:
        nombre = input('Ingrese el nombre del cliente: ')
        objetoBaseCLientes.buscarClienteNombre(nombre)
      case 3:
        dni = input('Ingrese el dni del cliente: ')
        cliente = pedir_datos("actualizar",dni)
        objetoBaseCLientes.actualizarCliente(dni, cliente)
      case 4:
        dni = input('Ingrese el dni del cliente: ')
        objetoBaseCLientes.eliminarCliente(dni)
      case 5:
        objetoBaseCLientes.mostrar()
  print('Saliendo del programa...')

#main
menu()
