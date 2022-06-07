lista_cursos = ['Python', 'Django', 'Flask']
print(lista_cursos)

#las listas son modificables se puede actualizar cualquier elemento
#atravez de su indice
lista_cursos[0] = 'Java'
print(lista_cursos)

#para agregar al final se usa la funcion append
lista_cursos.append('Mongodb')
print(lista_cursos)

#para agregar en cualquier indice
lista_cursos.insert(1, "Rails")
print(lista_cursos)

cursos_adicionales = ['C', 'C++', 'Docker']
#para concatenar dos listas se usa extend
lista_cursos.extend(cursos_adicionales)
print(lista_cursos)

#para eliminar se puede hacer con el metodo
#remove sin embargo se debe enviar el dato
#a eliminar
lista_cursos.remove('Mongodb')
print(lista_cursos)

#para eliminar por indice se usa del
del lista_cursos[3]
print(lista_cursos)

#para limpiar la lista se usa clear
lista_cursos.clear()
print(lista_cursos)

#para obtener la longitud se usa la funcion len
print(len(lista_cursos))