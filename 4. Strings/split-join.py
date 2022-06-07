lenguajes = "Python Ruby-Java-Rust C++ C"

#por defecto divide por espacios
#si se desea dividir por un dato especifico
#se agrega como parametro
print(lenguajes.split())
print(lenguajes.split('-'))
print(lenguajes.split('*'))
print(lenguajes.split(' ', 2))

listado_lenguajes = ['Javascript', 'React', 'Angular']
string_lenguajes = ' '.join(listado_lenguajes)
print(string_lenguajes)