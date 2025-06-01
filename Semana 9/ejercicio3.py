class Pasajero:
  def __init__(self,numeroPasaporte,nombre,edad,tipoAsiento):
    self.__numeroPasaporte = numeroPasaporte
    self.__nombre = nombre
    self.__edad = edad
    self.__tipoAsiento = tipoAsiento
  
  def imprimir(self):
    print(self.__numeroPasaporte)
    print(self.__nombre)
    print(self.__edad)
    print(self.__tipoAsiento)
  
  @property
  def tipoAsiento(self):
    return self.__tipoAsiento
  @property
  def tipoAsiento(self):
    return self.__tipoAsiento
  @tipoAsiento.setter
  def tipoAsiento(self, tipoAsiento):
    self.__tipoAsiento = tipoAsiento





class Vuelo:
  def __init__(self,horaSalida,horaLlegada,ciudadPartida,ciudadLlegada,precio):
    self.__horaSalida = horaSalida
    self.__horaLlegada = horaLlegada
    self.__ciudadPartida = ciudadPartida
    self.__ciudadLlegada = ciudadLlegada
    self.__precio = precio

    self.__listaPrimeraClase = []
    self.__listaTurista = []
  
  def imprimir(self):
    print(self.__horaSalida)
    print(self.__horaLlegada)
    print(self.__ciudadPartida)
    print(self.__ciudadLlegada)
  
  def agregar(self,pasajero):
    if pasajero.tipoAsiento == "Primera Clase":
      if len(self.__listaPrimeraClase) < 8:
        self.__listaPrimeraClase.append(pasajero)
      else:
        print("No hay asientos disponibles")
    else:
      if len(self.__listaTurista) < 92:
        self.__listaTurista.append(pasajero)
      else:
        print("No hay asientos disponibles")
  
  def mostrarTuristas(self):
    print("=====================")
    self.imprimir()
    for pasajero in self.__listaTurista:
      pasajero.imprimir()
  def mostrarPrimeraClase(self):
    print("=====================")
    self.imprimir()
    for pasajero in self.__listaPrimeraClase:
      pasajero.imprimir()




pasajero1 = Pasajero("1234","Kevin",24,"Primera Clase")
pasajero2 = Pasajero("2234","Cosner",24,"Turista")
pasajero3 = Pasajero("1234","Juan",28,"Primera Clase")
pasajero4 = Pasajero("2233","Daniel",20,"Turista")

vuelo1 = Vuelo("12:30","1:30","Lima","Piura",300)
vuelo1.agregar(pasajero1)
vuelo1.agregar(pasajero3)

vuelo2 = Vuelo("11:30","1:30","Lima","Tacna",300)
vuelo2.agregar(pasajero2)
vuelo2.agregar(pasajero4)

vuelo1.mostrarPrimeraClase()
vuelo2.mostrarTuristas()
