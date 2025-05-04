import math
class TroncoDeCono:
  def __init__(self, altura, radio_mayor, radio_menor):
    self.__altura = altura
    self.__radio_mayor = radio_mayor
    self.__radio_menor = radio_menor
    self.__generatriz= 0
    self.__area = 0
    self.__volumen = 0

  def calcula_arista(self):
    self.__generatriz = (self.__altura ** 2 + (self.__radio_mayor - self.__radio_menor)**2)**(1/2)

  def calcula_area(self):
    self.__area = math.pi *(self.__radio_mayor**2 + self.__radio_menor**2 + self.__generatriz * (self.__radio_mayor + self.__radio_menor))
    print(f'àrea: {self.__area}')
  def calcula_volumen(self):
    self.__volumen = (self.__altura * math.pi / 3) * (self.__radio_mayor**2 + self.__radio_menor**2 +self.__radio_mayor * self.__radio_menor)
    print(f'volumen: {self.__volumen}')



objeto_cono = TroncoDeCono(10, 5, 3)
objeto_cono.calcula_arista()
objeto_cono.calcula_area()
objeto_cono.calcula_volumen()
