class Laptop:
  def __init__(self, marca, chip, precioBase,pantalla='Normal'):
    self.marca = marca
    self.chip = chip
    self.precioBase = precioBase
    self.pantalla = pantalla
    self.precioFinal = 0

  def calcularPrecioChip(self):
    if self.chip == 'i5':
      return self.precioBase * 0.1
    elif self.chip == 'i7':
      return self.precioBase * 0.15
    return 0
  
  def calcularPrecioPantalla(self):
    if self.pantalla == 'táctil':
      return self.precioBase * 0.05
    return 0

  def calcularPrecioFinal(self):
    self.precioFinal = self.precioBase + self.calcularPrecioChip() + self.calcularPrecioPantalla()
    return self.precioFinal

  def __str__(self):

    return (f"\n=====================================\n"
        f"Marca: {self.marca}\nChip: {self.chip}\nPantalla: {self.pantalla}"
            f"\nPrecio base: ${self.precioBase}\n"
            f"Precio final: ${self.calcularPrecioFinal()}")
    

obj1 = Laptop('HP','i3',2000,'táctil')
obj2 = Laptop('HP','i5',2000)
obj3 = Laptop('HP','i7',2000,'táctil')

print(obj1)
print(obj2)
print(obj3)
