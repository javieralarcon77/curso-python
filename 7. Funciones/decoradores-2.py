"""
para pasar argumentos
usamos los args y kwargs en la funcion_c
y los pasamos a la funcion b

recordar que al llamar la funcion decorada suma()
se ejecuta la funcion_c que es el decorador
"""

def funcion_a(funcion_b):

    def funcion_c(*args, **kwargs):
        print('>>>> Antes del llamado')
        resultado = funcion_b(*args, **kwargs)
        print('<<<< Despues del llamado')
        return resultado

    return funcion_c


@funcion_a
def suma(a, b):
    return a + b

resultado = suma(10, 20)
print(resultado)