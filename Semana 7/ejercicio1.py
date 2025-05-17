import random 

def validar_contrasenia(contrasenia):
  if len(contrasenia) < 8:
    return False
  
  cont_numero = 0
  cont_mayus = 0
  cont_minus = 0
  cont_especial = 0
  for caracter in contrasenia:
    if caracter.isdigit():
        cont_numero += 1
    elif caracter.isupper():
        cont_mayus += 1
    elif caracter.islower():
        cont_minus += 1
    elif caracter in '@_$':
        cont_especial += 1
  
  if cont_numero > 0 and cont_mayus > 0 and cont_minus > 0 and cont_especial > 0:
    return True
  else:
    return False


def registrar():
  correo = ''
  dominio = ''
  while '@' not in correo or '.' not in dominio:
    correo = input("correo: ") #kevin@gmail.com
    lista = correo.split("@")
    usuario = lista[0]
    dominio = "@" + lista[1]

  while True:
    contrasenia = input("contraseña: ")
    if validar_contrasenia(contrasenia):
      break
  pin = random.randint(100,999)

  tupla = (usuario,dominio,contrasenia,pin)

  dicionario[correo] = tupla

def eliminar():
  correo = input("correo: ")
  pin = int(input("pin: "))
  if dicionario[correo][-1] == pin:
    dicionario.pop(correo)
    print("usuario eliminado")
  else:
    print("pin incorrecto")

def mostrar():
  for clave,valor in dicionario.items():
    print(clave,valor)


def opciones():
  print('1: registrar')
  print('2: eliminar')
  print('3: mostrar')
  print('4: salir')
  opcion = -1
  while opcion < 1 or opcion > 4:
    try:
      opcion = int(input("opcion: "))
    except:
      print("opcion incorrecta")
  return opcion

def main():
  while True:
    opcion = opciones()
    if opcion == 1:
      registrar()
    elif opcion == 2:
      eliminar()
    elif opcion == 3:
      mostrar()
    elif opcion == 4:
      break

dicionario = {}
main()
