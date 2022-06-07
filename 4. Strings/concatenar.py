nombre = 'Javier'
apellido = 'Alarcon'

#1era forma
# nombre_completo = 'Mr. ' + nombre + ' ' + apellido

#2da forma
# nombre_completo = 'Mr. %s %s' %(nombre, apellido)

#3era forma
# nombre_completo = 'Mr. {} {}'.format(nombre, apellido)

#3era forma con parametros
#nombre_completo = 'Mr. {primer_nombre} {primer_apellido}'.format(
#    primer_apellido=apellido,
#    primer_nombre=nombre,
#)

#4ta forma
nombre_completo = f'Mr. {nombre} {apellido}'

print(nombre_completo)