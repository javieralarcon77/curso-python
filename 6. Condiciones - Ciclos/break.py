titulo_curso = 'Curso profesional de Python'

#break rompe el ciclo
#continue hace que el ciclo pase a la siguiente iteracion

for caracter in titulo_curso:
    if caracter == 'P':
        break

    if caracter == ' ':
        continue

    print(caracter)