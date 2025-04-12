Salario_mensual = float(input("Ingrese su salario mensual: "))
numPersonas = int(input("Ingrese el número de personas que trabajan en la empresa: "))

linea = ''
if numPersonas == 1:
  if Salario_mensual <= 500:
    linea = 'P'
  else:
    linea = 'O'
elif numPersonas <= 4: #else if -> elif
  if Salario_mensual <= 750:
    linea = 'P'
  else:
    linea = 'O'
else:
  if Salario_mensual <= 1000:
    linea = 'P'
  else:
    linea = 'O'

print(f'Tipo de línea al que puede acceder: {linea}')
