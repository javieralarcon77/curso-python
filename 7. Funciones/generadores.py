"""
con la palabra reservada yield
pausamos la ejecucion de la funcion hasta
ser llamada de nuevo
esto se conoce como lazy iterator
"""
def pares():
    for numero in range(0, 100, 2):
        yield numero

#for par in pares():
#    print(par)

generador = pares()

print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))