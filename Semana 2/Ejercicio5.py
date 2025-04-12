codigo4 = input('Còdigo: ')
cantidad = int(input('Cantidad: '))

precio_unidad = 0
codigo = codigo4[-1]

if codigo == '1':
  precio_unidad = 15.75
elif codigo == '2':
  precio_unidad = 21
elif codigo == '3':
  precio_unidad = 8.5
elif codigo == '4':
  precio_unidad = 25
else:
  precio_unidad = 13.25

total = precio_unidad * cantidad

print(f'Total: {total}')
