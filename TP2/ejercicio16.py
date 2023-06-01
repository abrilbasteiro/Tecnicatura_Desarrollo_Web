#  Que imprima el siguiente patrón:
#  5 4 3 2 1
#  4 3 2 1
#  3 2 1
#  2 1
#  1

numeros = list(range(5, 0, -1))

for indice in numeros:
    for numero in range(indice, 0, -1):
        print(numero, end=' ')
    print()