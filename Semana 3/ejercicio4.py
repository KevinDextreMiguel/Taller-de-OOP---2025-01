import random

def ingresa_numero():
  n = -1
  while n < 1 or n > 40:
    try:
      n = int(input('N: '))
    except:
      print('debe ingresar un número entero')
  return n

def generar(n):
  for i in range(n):
    numero = random.randint(1,9)
    lista.append(numero)

def mostrar(lista):
  for numero in lista:
    print(numero, end=' ')
  print()

def contar_apariciones(lista):
  numero = 9
  for i in range(1,numero+1):
    print(f'El número {i} aparece {lista.count(i)} veces')

def incrementar_primo(lista):
  primos = [2,3,5,7]
  for i in range(len(lista)):
    if lista[i] in primos:
      lista[i] = lista[i] + 1
    

lista = [] # lista = list()
n = ingresa_numero()
generar(n)
mostrar(lista)
contar_apariciones(lista)
incrementar_primo(lista)
mostrar(lista)
