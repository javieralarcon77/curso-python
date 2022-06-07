#con doble astericos obtenemos un elevado

#para colocar un valor por defecto lo asignamos
#con un igual se recomienda no usar espacios al usar
#valores por default y deben estar al final de los parametros
def area_circulo(radio, pi=3.14):
    return pi * (radio ** 2)

resultado = area_circulo(20)
print(resultado)

resultado = area_circulo(10, 3.141592)
print(resultado)

#asignacion de parametros por nombre
resultado = area_circulo(pi=3.1415, radio=15)
print(resultado)