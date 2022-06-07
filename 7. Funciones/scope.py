animal = 'Leon' # variable global
tipo = 'mamifero'

def imprimir_animal():
    global tipo #se usa primero como global para poder modificar el valor global
    tipo = 'Mamifero'
    animal = 'Ballena' #variable local
    print(animal)
    print(tipo)
    
imprimir_animal()
print(animal)
print(tipo)