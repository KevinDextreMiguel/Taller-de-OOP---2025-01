from abc import ABC, abstractmethod
import pandas as pd

class Volumen(ABC):# Clase Base (Padre)
  def __init__(self,id,name):
    self.__id = id
    self.__name = name
  
  @property
  def id(self):
    return self.__id
  @property
  def name(self):
    return self.__name
  
  @abstractmethod
  def __str__(self):
    pass


class Book(Volumen): #Clase hija (Subclase) (Derivada)
  def __init__(self,id,name,isbn):
    super().__init__(id,name)
    self.isbn = isbn
  
  def __str__(self):
    return f'Id: {self.id}, Name: {self.name}, ISBN: {self.isbn}'



class Newpaper(Volumen): #Clase hija (Subclase) (Derivada)
  def __init__(self,id,name,issn):
    super().__init__(id,name)
    self.issn = issn
  
  def __str__(self):
    return f'Id: {self.id}, Name: {self.name}, ISSN: {self.issn}'



class Library:
  def __init__(self,name,address):
    self.name = name
    self.address = address
    self.volumens = []
  
  def add_volumen(self,volumen):
    if not self.existes_volumen(volumen):
      self.volumens.append(volumen)
    else:
      print("Ya existe un volumen con ese identificador")
  
  def existes_volumen(self,objeto):
    for volumen in self.volumens:
      if volumen.id == objeto.id:
        return True
    return False
  
  def remove_volumen(self,id):
    for volumen in self.volumens:
      if id == volumen.id:
        self.volumens.remove(volumen) #volumens.pop(id)   (cuando se elimian por índice)
        print('Eliminado')
        return
    print("No exite")
  
  def guardar_excel(self):
    lista_id = []
    lista_name = []
    for volumen in self.volumens:
      lista_id.append(volumen.id)
      lista_name.append(volumen.name)

    df = pd.DataFrame({'id':lista_id,'name':lista_name})
    df.to_excel('tallerSemana11.xlsx',sheet_name="ejercicio2",index=False)
    print('Guardado')
  
  def mostrar(self):
    print(f'Name: {self.name}, Address: {self.address}')
    for volumen in self.volumens:
      print(volumen)


objeto_book1 = Book(1,"libro 1","1234567890")
objeto_book2 = Book(2,"libro 2","2234567890")
objeto_book3 = Book(3,"libro 3","8234567890")

objeto_newpaper = Newpaper(4,"newpaper 1","1234567890")
objeto_newpaper2 = Newpaper(5,"newpaper 1","2234567890")
objeto_newpaper3 = Newpaper(6,"newpaper 1","8234567890")

objeto_library = Library("Biblioteca 1","Dirección 1")
objeto_library.add_volumen(objeto_book1)
objeto_library.add_volumen(objeto_book2)
objeto_library.add_volumen(objeto_book3)
objeto_library.add_volumen(objeto_newpaper)
objeto_library.add_volumen(objeto_newpaper2)
objeto_library.add_volumen(objeto_newpaper3)

objeto_library.mostrar()
objeto_library.remove_volumen(6)
objeto_library.mostrar()

objeto_library.guardar_excel()
