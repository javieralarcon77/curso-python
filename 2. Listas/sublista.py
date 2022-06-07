lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java', 'Rust']

#[start:end]
#primer dato indice inicial
#segundo dato indice final
#sin embargo el indice final no se toma
sub_lista = lista_cursos[0:3]

print(sub_lista)

#[start:] -> obtenemos los ultimos elemento de la lista
#[:end] -> obtenemos los primero elementos de la lista
print(lista_cursos[:4])

#[start:end:skip]
print(lista_cursos[1:5:2])

#para listas invertidas se omiten los dos primros valores
#y se colocan los saltos como -1
print(lista_cursos[::-1])