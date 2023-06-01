# Pedir al usuario que ingrese 5 números para luego almacenarlos en una lista y ordenarlos. Imprimir por pantalla el resultado

lista_numeros = []

for numero in range(1,6):
    numero = int(input('Ingrese el ' + str(numero) + '°' + ' numero: '))
    lista_numeros.append(numero)

lista_numeros.sort()

for i in range(len(lista_numeros)):
    lista_numeros[i] = str(lista_numeros[i])

print('Los números ordenados son:', ', '.join(lista_numeros))