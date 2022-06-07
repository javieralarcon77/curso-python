"""
a -> la funcion principal (decorador)
b -> la funcion a decorar
c -> la funcion decorada

a(b) -> c
"""

def funcion_a(funcion_b):

    def funcion_c():
        print('>>>> Antes del llamado')
        funcion_b()
        print('<<<< Despues del llamado')

    return funcion_c

@funcion_a
def saludar():
    print('Hola, nos encontramos en una funcion')


@funcion_a
def suma():
    print(10 + 20)

saludar()
suma()