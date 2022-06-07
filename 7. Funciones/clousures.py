#los clousures son funciones anidadas que 
#recuerdan variables locales de la funcion superior

def saludar(username):
    mensaje = f'Hola {username}'

    def mostrar_mensaje():
        print(mensaje)

    return mostrar_mensaje

username = 'Cody'

respuesta = saludar(username)
respuesta()

username = 'Javier'
respuesta()