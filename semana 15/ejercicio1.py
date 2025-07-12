class Administrador:
  def __init__(self,id,nombre):
    self.__id = id
    self.__nombre = nombre
  
  def __str__(self):# mostrar()
    return f'Id: {self.__id}, Nombre: {self.__nombre}'

class Propietario:
  def __init__(self,id,nombre):
    self.__id = id
    self.__nombre = nombre
  
  def __str__(self):# mostrar()
    return f'Id: {self.__id}, Nombre: {self.__nombre}'

class JuntaPropietarios:
  def __init__(self,id,fecha_creacion):
    self.__id = id
    self.__fecha_creacion = fecha_creacion
    self.__propietarios = []
  
  def agregar_propietario(self,propietario):
    self.__propietarios.append(propietario)
  def obtener_info(self):
    print(f"Id: {self.__id}, Fecha de creación: {self.__fecha_creacion}")
    print("Propietarios: ")
    for propietario in self.__propietarios:
      print(propietario)
  
class Departamento:
  def __init__(self,id,numero_habitacion):
    self.__id = id
    self.__numero_habitacion = numero_habitacion
  
  def __str__(self):# mostrar()
    return f'Id: {self.__id}, Número de habitación: {self.__numero_habitacion}'

class Edificio:
  def __init__(self,id,direccion):
    self.__id = id
    self.__direccion = direccion
    self.__departamentos = []
    self.__junta_propietarios = None
    self.__administrador = None
  
  def agregar_departamento(self,departamento):
    self.__departamentos.append(departamento)
  def asignar_administrador(self,administrador):
    self.__administrador = administrador
  def asignar_junta_propietarios(self,junta_propietarios):
    self.__junta_propietarios = junta_propietarios
  def obtener_info(self):
    print(f"Id: {self.__id}, Dirección: {self.__direccion}")
    print("Departamentos: ")
    for departamento in self.__departamentos:
      print(departamento)
    print('Información del administrador: ')
    print(self.__administrador)
    print('Información de la junta de propietarios: ')
    self.__junta_propietarios.obtener_info()

  
#Crear objetos
administrador = Administrador(1,'Luis')

propietario1 = Propietario(1,'Manuel')
propietario2 = Propietario(2,'Kevin')
propietario3 = Propietario(3,'Ana')

junta_propietarios = JuntaPropietarios(1,'2025-07-12')
junta_propietarios.agregar_propietario(propietario1)
junta_propietarios.agregar_propietario(propietario2)
junta_propietarios.agregar_propietario(propietario3)

departamento1 = Departamento(1,4)
departamento2 = Departamento(2,3)
departamento3 = Departamento(3,5)

edificio = Edificio(1,'Calle 123')
edificio.agregar_departamento(departamento1)
edificio.agregar_departamento(departamento2)
edificio.agregar_departamento(departamento3)
edificio.asignar_administrador(administrador)
edificio.asignar_junta_propietarios(junta_propietarios)

edificio.obtener_info()
