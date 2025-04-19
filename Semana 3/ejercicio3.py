def ingresa_numero():
  n = -1
  while n < 2 or n > 9:
    try:
      n = int(input('N: '))
    except:
      print('debe ingresar un número entero')
  return n

def graficar(n):
  for i in range(n):
    letra = 'A'
    # columnas
    for j in range(n-i):
      print(letra, end=' ')
      letra_numero = ord(letra) + 1
      letra = chr(letra_numero)
  
    #espacios
    for e in range(i*2):
      print(end='  ')
  
    letra = 'A'
    # columnas
    for j in range(n-i):
      print(letra, end=' ')
      letra_numero = ord(letra) + 1
      letra = chr(letra_numero)
    print()

def consultar_usurio():
  cont = 0
  while True:
    cont += 1
    n = ingresa_numero()
    graficar(n)
    var = input('Desea continuar? (s/n): ')
    if var.upper() != 'S':
      break
  print(f'Se hicieron {cont} dibujos')

#main
consultar_usurio()
