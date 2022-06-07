numero = 1237543
contador = 0

#permite ejecutar un bloque de codigo
#siempre y cuando la condicion se cumpla
#en el while podemos usar el else opcional
#y se ejecuta al finalizar el while

while numero >= 1:
    #contador = contador + 1
    contador += 1
    numero = numero / 10
else:
    print(contador)
