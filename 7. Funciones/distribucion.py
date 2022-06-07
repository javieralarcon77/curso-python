def pares(): #generador
    for numero in range(0, 12, 2):
        yield numero #la funcion suspende su ejecucion
        print('Se reanuda')


generador = pares()

while True:
    try:
        par = next(generador)
        print(par)
    except StopIteration:
        print('El generador finalizo')
        break
