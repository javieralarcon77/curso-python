diccionario = {}

diccionario = dict()

diccionario = {
    "total": 55,
    10: "curso de Python",
    "tupla": (5, 10)
}

#creaccion del diccionario
dicc = dict()
#agregar nuevo valor mediante una llave
dicc['usuario'] = 'javier'
#modificar el valor mediante una llave
dicc['usuario'] = 'javier77'
#obtener el valor mediante una llave
#si no existe no da error
print(dicc['usuario'])
#para obtener el valor o uno por defecto en caso de no existir usamos get
print(dicc.get('nombre', ''))

#obtener todas las llaves
print(diccionario.keys())

#obtener todos los valores de un diccionario
print(diccionario.values())

#antes de trabajar con las llaves o los valores se recomienda convertirlas en tupla
print(tuple(diccionario.keys()))

#recorrer los valores
for key, value in diccionario.items():
    print(key, value)