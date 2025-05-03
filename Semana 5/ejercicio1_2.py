class Articulo:
  def __init__(self, nombre, precio, talla):
    self.nombre = nombre # Camisa
    self.precio = precio # 100
    self.talla = talla # M

  def imprimir(self):
    print(f"Nombre: {self.nombre}")
    print(f"Precio: {self.precio}")
    print(f"Talla: {self.talla}")

  #get
  def get_nombre(self):
    return self.nombre
  def get_precio(self):
    return self.precio
  def get_talla(self):
    return self.talla
  #set
  def set_nombre(self,valor):
    self.nombre = valor
  def set_precio(self,valor):
    self.precio= valor
  def set_talla(self,valor):
    self.talla= valor



objeto_articulo = Articulo("Camisa", 100, "M")
#objeto_articulo.imprimir()

print(objeto_articulo.get_nombre())
print(objeto_articulo.get_precio())
print(objeto_articulo.get_talla())

objeto_articulo.set_nombre("Pantalon")
objeto_articulo.set_precio(200)
objeto_articulo.set_talla("L")
print('Despuès de modificar')
print(objeto_articulo.get_nombre())
print(objeto_articulo.get_precio())
print(objeto_articulo.get_talla())
