numero = int(input('Ingrese código generado: '))

#  6668090219 ->  6668 090219

TTTT = numero // 1000000
residuo_numero = numero % 1000000 #090219

HH = residuo_numero // 10000 #09 0219
residuo2_numero = residuo_numero % 10000 #02 19

MM = residuo2_numero // 100
SS = residuo2_numero % 100

print(f'Código del trabajador: {TTTT}')
print(f'Hora de entrada: {HH}')
print(f'Minuto de entrada: {MM}')
print(f'Segundos de entrada: {SS}')
