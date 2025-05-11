import math

class TroncoCono:
  def __init__(self, r1,r2, altura):
    self.__r1 = r1
    self.__r2 = r2
    self.__altura = altura

  def calcularGeneratriz(self):
    return math.sqrt(math.pow(self.__altura,2) + math.pow(self.__r1 - self.__r2,2))
  
  def calcularVolumen(self):
    volumen = (math.pi * self.__altura) / 3 * (self.__r1 ** 2 + self.__r2 ** 2 + self.__r1 * self.__r2)
    return volumen

  def calcularArea(self):
    generatriz = self.calcularGeneratriz()
    area = math.pi * (self.__r1 ** 2 + self.__r2 ** 2 + generatriz * (self.__r1 + self.__r2) )
    return area
  
  def __str__(self):
    print('=====================================')
    return (f"r1: {self.__r1}\nr2: {self.__r2}\naltura: {self.__altura}\n"
          f'Volumen: {self.calcularVolumen():.2f}\nArea: {self.calcularArea():.2f}')



objeto1 = TroncoCono(2,3,4)
objeto2 = TroncoCono(6,8,4)
objeto3 = TroncoCono(10,13,4)

print(objeto1)
print(objeto2)
print(objeto3)
