lista = [1, 2, 3, 4, 5]
tupla = (10, 20, 30, 40, 50)
tupla_2 = (100, 200, 300, 400, 500, 600, 700)

resultado = zip(lista, tupla, tupla_2)
resultado = tuple(resultado)

print(resultado)