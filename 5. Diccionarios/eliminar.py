diccionario = { 'a': 1, 'b': 2, 'c': 3, 'd': 4 }
print(diccionario)

#antes de eliminar por cualquiera de las 2 formas se debe validar que exista
#el elemento de lo contrario daria un keyerror

#1era forma
del diccionario['a']
print(diccionario)

#2da forma
eliminado = diccionario.pop('b')
print(diccionario)
print(eliminado)

#limpiar el diccionario
diccionario.clear()
print(diccionario)