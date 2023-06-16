# EJERCICIO 1)
# Escribir un programa que pida al usuario que ingrese nombre, apellido y empresa de un empleado y que imprima por pantalla el correo electrónico sugerido de la siguiente manera:
# Usuario ingresa.
# Nombre: Marcos
# Apellido: Juarez
# Empresa: La porteñita
# Sistema devuelve: mjuarez@laporteñita.com

nombre = str(input('Ingrese su nombre: '))
apellido = str(input('Ingrese su apellido: '))
empresa = str(input('Ingrese su empresa: '))
mail = nombre[0] + apellido + '@' + empresa.replace(' ', '') + '.com'

print(mail.lower())