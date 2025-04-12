n = -1

#validar
while n < 1 or n > 5:
  try:
    n = int(input('N: '))
  except:
    print('debe ingresar un número')


for i in range(n):
  #validar
  numero = -1
  while numero < 1 or numero > 1000:
    try:
      numero = int(input('Número: '))
    except:
      print('debe ingresar un número')
  
  if numero % 2:
    print('Es impar')
  else:
    print('Es par')

print('Fin, nos vemos')
