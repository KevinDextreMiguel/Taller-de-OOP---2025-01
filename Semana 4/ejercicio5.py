def menu():
  print("1: Añadir")
  print("2: Actualizar el puesto y salario ")
  print("3: Calcular el salario anual de un empleado")
  print("4: Mostrar la lista de empleados")
  print("5: Salir")
  opcion = -1
  while opcion < 1 or opcion > 5:
    try:
      opcion = int(input("Ingrese una opción: "))
    except:
      print("Opción inválida")
  return opcion

def agregar():
  dni = input("Ingrese el DNI del empleado: ")
  nombre = input("Ingrese el nombre del empleado: ")
  edad = int(input("Ingrese la edad del empleado: "))
  puesto = input("Ingrese el puesto del empleado: ")
  salario = float(input("Ingrese el salario del empleado: "))

  diccionario_empleados[dni] = {"nombre": nombre, "edad": edad, "puesto": puesto, "salario": salario}

def actualizarPuestoSalario():
  dni = input("Ingrese el DNI del empleado: ")
  if dni in diccionario_empleados.keys():
    puesto = input("Ingrese el nuevo puesto del empleado: ")
    salario = float(input("Ingrese el nuevo salario del empleado: "))
    diccionario_empleados[dni]["puesto"] = puesto
    diccionario_empleados[dni]["salario"] = salario
  else:
    print("Empleado no encontrado")

def calcularSalarioAnual():
  dni = input("Ingrese el DNI del empleado: ")
  if dni in diccionario_empleados.keys():
    salario = diccionario_empleados[dni]["salario"]
    salarioAnual = salario * 12
    if diccionario_empleados[dni]["edad"] > 50:
      salarioAnual *= 50
    print(f"El salario anual del empleado es: {salarioAnual}")
  else:
    print("Empleado no encontrado")

def listar():
  for clave,valor in diccionario_empleados.items():
    print(clave,valor)

def listarOrdenado():
  lista = list()
  for clave,valor in diccionario_empleados.items():
    aux = [valor["nombre"],valor["salario"],"Sin Bono"]
    if valor["edad"] > 50:
      aux[-1] = "Con Bono"
    lista.append(aux)# añadiendo una lista

  lista.sort()
  for l in lista:
    print(l)


def main():
  opcion = -1
  while opcion != 5:
    opcion = menu()
    if opcion == 1:
      agregar()
    elif opcion == 2:
      actualizarPuestoSalario()
    elif opcion == 3:
      calcularSalarioAnual()
    elif opcion == 4:
      listar()



diccionario_empleados = {}
opcion = -1
main()
listarOrdenado()
