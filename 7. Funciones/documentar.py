#Docstring
#es un comentario que se coloca en la primera 
#linea de funcion
#lo objetos documentables son (Modulos, Clases, Metodos y Funciones)
#se guarda en una variable __doc__


def suma(numero_1, numero_2):
    """
    La funcion suma 2 numeros
    Argumentos:
    numero_1 (int)
    numero_2 (int)

    Se retorna la suma de los parametros

    #test
    >>> suma(10, 20)
    30

    >>> suma(100, 200)
    300
    """
    return numero_1 + numero_2

# para imprimir la documentacion de la funcion
# podemos llamar a __doc__ o con la funcion help
#print(suma.__doc__)
#print(help(suma))

#para ejecutar las pruebas colocamos en la terminal
#python -m doctest archivo_testear.py
#si no tenemos un error no se muestra nada si tenemos un error se vera en consola