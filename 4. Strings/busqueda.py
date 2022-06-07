titulo_curso = 'Curso profesional de Python, donde aprenderemos Python'

#retorna las coincidencias que tenga la palabra dentro del string
print(titulo_curso.count('Python'))
print(titulo_curso.count('o'))
print(titulo_curso.count('x'))

print('Python' in titulo_curso)
print('python' in titulo_curso)
#podemos pasar el string
#a minusculas .lower()
#a mayusculas .upper()
print('python' in titulo_curso.lower())

#podemos validar si un string esta al inicio o al final
print(titulo_curso.startswith('Curso'))
print(titulo_curso.endswith('Python'))
