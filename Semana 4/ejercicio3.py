import re

def imprimir(texto):
  print('============================')
  print(texto)

def eliminarSignoPuntuacion(texto):
  texto = re.sub(r'[^\w\s]', '', texto)
  imprimir(texto)
  return texto

def convertirTodoMinuscula(texto):
  texto = texto.lower()
  imprimir(texto)
  return texto

def contarApariciones():
  diccionario = {}
  lista = texto.split()
  for palabra in lista:
    diccionario[palabra] = diccionario.get(palabra,0)+1
  print(f'Cantidad por palabra: {diccionario}')
  
  return diccionario

def ordenarPoApariciones(diccionario):
  lista = list()
  for clave,valor in diccionario.items():
    if valor > 1:
      lista.append((valor,clave))

  lista.sort(reverse=True)
  for valor,clave in lista:
    print(clave,valor)


texto = """
¡Oh! Que madre tan bella. ¿Será que La madre de Juan es hermana de Pedro? 
Juan va con ella a todos lados; es decir no la deja sola ni para ir al mercado. 
Juan le dice a su madre que compre piña, mango, melón, patilla porque son 
nutritivos. 
La madre de Juan le enseña las vocales: a, e, i, o, u. 
En la casa de Juan hay muchos colores: azul, amarillo, rojo, verde… 
La madre de Juan le enseña que Simón Bolívar dijo: 
"Un ser sin estudio es un ser incompleto".
"""

imprimir(texto)
texto = eliminarSignoPuntuacion(texto)
texto = convertirTodoMinuscula(texto)
diccionario = contarApariciones()
ordenarPoApariciones(diccionario)
