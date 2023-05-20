# Que solicite al usuario ingresar una frase. Luego, que imprima la cantidad de vocales que se encuentran en dicha frase.

def contar_vocales(frase):
    cantidad_de_vocales = 0
    vocales = ['a', 'e', 'i', 'o', 'u']
    for i in frase.lower():
        if i in vocales:
            cantidad_de_vocales += 1
    print('En la frase hay', cantidad_de_vocales, 'vocales')
    
frase = input('Ingrese una frase: ')

contar_vocales(frase)