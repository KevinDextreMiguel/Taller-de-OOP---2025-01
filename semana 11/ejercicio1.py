class Accionar:
  def prender(self):
    print('Encendido')
  def apagar(self):
    print('Apagado')


from abc import ABC, abstractmethod

class Electrodomestico():
  def __init__(self, potencia_kw, marca):
    self.potencia_kw = potencia_kw
    self.marca = marca
  
  def encender(self,objetoAccionar):
    objetoAccionar.prender()
  
  def apagar(self,objetoAccionar):
    objetoAccionar.apagar()
  
  def __str__(self):
    return f'Potencia: {self.potencia_kw}, Marca: {self.marca}'

  @abstractmethod
  def consumoEnergetico(self):
    pass


class Coccion(Electrodomestico):
  def __init__(self, potencia_kw, marca, programable):
    super().__init__(potencia_kw, marca)
    self.programable = programable
  
  def consumoEnergetico(self):
    return self.potencia_kw * 10
  
  def __str__(self):
    return f'{super().__str__()}, Programable: {self.programable}'


class Cocina(Coccion):
  def __init__(self, potencia_kw, marca, programable, hornillas):
    super().__init__(potencia_kw, marca, programable)
    self.hornillas = hornillas
  
  def consumoEnergetico(self):
    return self.potencia_kw * 10 + self.hornillas * 20
  
  def __str__(self):
    return f'{super().__str__()}, Hornillas: {self.hornillas}'



class Horno(Coccion):
  def __init__(self, potencia_kw, marca, programable, capacidad):
    super().__init__(potencia_kw, marca, programable)
    self.capacidad = capacidad
  
  def consumoEnergetico(self):
    return self.potencia_kw * 10 + self.capacidad * 20
  
  def __str__(self):
    return f'{super().__str__()}, Capacidad: {self.capacidad}'


objetoAccionar = Accionar()
objetoHorno = Horno(10,'Horno 1',True,10)
objetoHorno.encender(objetoAccionar)
objetoHorno.apagar(objetoAccionar)
print(objetoHorno)
objetoHorno.consumoEnergetico()
