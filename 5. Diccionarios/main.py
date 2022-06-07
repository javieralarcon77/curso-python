usuarios = ['Javier', 'Katery', 'Miguel', 'Tijo']

diccionario = { usuario: position + 1
    for position, usuario in enumerate(usuarios) }

print(diccionario)