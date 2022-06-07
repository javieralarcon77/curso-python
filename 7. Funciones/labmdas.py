"""
def centrigrados_a_farenheit(grados):
    return grados * 1.8 + 32

mi_funcion = centrigrados_a_farenheit

print(mi_funcion(10))
print(mi_funcion(-1))
print(mi_funcion(8))
"""
#esta es una funcion anonima
#debe ser de una linea y retorna el resultado del cuerpo de la funcion
#lambda <parametros> : <cuerpo de la funcion>

funcion_grados = lambda grados: grados * 1.8 + 32

print(funcion_grados(10))