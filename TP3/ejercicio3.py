# Dada la siguiente lista de frutas [“banana”, “manzana”, “pera”], permitir al usuario ingresar 3 frutas más para agregarlas al final de lista. Luego, mostrar por pantalla la lista completa y debajo la misma lista pero sólo con las frutas que añadió el usuario

frutas = ['banana', 'manzana', 'pera']
frutas_usuario = []

for i in range(1,4):
    i = str(input('Ingrese la ' + str(1) + '°' + ' fruta: '))
    frutas.append(i)
    frutas_usuario.append(i)

print('Todas las frutas son:', ', '.join(frutas), '\n Las frutas ingresadas por el usuario son:', ', '.join(frutas_usuario))