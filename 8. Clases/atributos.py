#Attrs de clase
#son atributos que le pertenece a la clase
#se accede directamente desde la clase
#sin embargo si creamos un objeto de la clase por defecto toma los atributos de la clase
class Usuario:
    username = 'Username por default'
    email = ''

print(Usuario.username)
Usuario.username = 'User 1'
print(Usuario.username)

user1 = Usuario()
print(user1.username)

user1.password = '1234' #Atributo de instancia
#los atributos de intancia se crean en tiempo de ejecucion
#y son modificables para ver los atributos de instancia 
#lo podemos hacer mediante le atributo __dict__

print(user1.__dict__)
user1.password= 'Password'

print(user1.__dict__)