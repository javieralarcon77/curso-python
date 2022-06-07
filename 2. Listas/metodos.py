lista = [8, 90, 1, 5, 44, 132, 600, 3, 4]

#metodo de ordenamiento
#el sort por defecto ordena de mayor a menor
lista.sort()
print(lista)

#para ordenar de formar inversa enviamos reverse
lista.sort(reverse=True)
print(lista)

#forma rapida de obtener el mayor y el menor
print(min(lista))
print(max(lista))

#validar si existe un dato dentro del listado
print(10 in lista)
print(5 in lista)

#para obtener el indice de un elemento usamos el metodo index
#obtiene el primer indice donde esta
#si no existe el elemento da error
print(lista.index(5))