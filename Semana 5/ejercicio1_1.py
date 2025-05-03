class Articulo:
  def __init__(self, nombre, precio, talla):
    self.nombre = nombre # Camisa
    self.precio = precio # 100
    self.talla = talla # M

  def imprimir(self):
    print(f"Nombre: {self.nombre}")
    print(f"Precio: {self.precio}")
    print(f"Talla: {self.talla}")

  def descuento(self,porcentaje):
    print(f"Descuento: {porcentaje/100 * self.precio}")

  def actualizar_precio(self,precio_nuevo): # set_precio
    self.precio = precio_nuevo #200

# set -> (actualizar, modificar)
# get -> (obtener, retornar)


objeto_articulo = Articulo("Camisa", 100, "M")
objeto_articulo.imprimir()
objeto_articulo.descuento(10)

objeto_articulo.actualizar_precio(200)
objeto_articulo.imprimir()



