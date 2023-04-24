# Programe una aplicación de consola que pregunte el precio total de la cuenta, luego pregunte cuántos comensales hay. A continuación deberá dividir la cuenta total por el número de comensales y mostrar cuánto debe pagar cada persona.

precio_total = int(input('¿Cuál es el total de la cuenta? '))
cantidad_comensales = int(input('¿Cuántos comensales hay? '))

precio_por_persona = precio_total / cantidad_comensales

print('Cada persona debe pagar $' + str(precio_por_persona))