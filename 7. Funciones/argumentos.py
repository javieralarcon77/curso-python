#recibiendo un parametro con astericos
#nos convierte los argumentos no recibidos como una tupla
#como convencion se debe llamar args

"""
def promedio(*args):
    return sum(args) / len(args)

resultado = promedio(10, 10, 5, 7, 10)
print(resultado)

def combinacion(p1, p2, *args):
    print(p1)
    print(p2)
    print(args)

combinacion(1, 2, 3, 4, 5, 6)

"""
#al agregar doble asterico se reciben los argumentos como un diccionario
#siendo el nombre del parametro la llave y el valor la asignacion del parametro
def usuarios(**kwards):
    print(kwards)


usuarios(javier=[10, 10, 10], eduardo=[20, 5, 20])
