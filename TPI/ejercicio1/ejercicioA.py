# a. Escribir una función de nombre palabra_no_tiene_letras(palabra, letras_prohibidas), la cual retorne True si es que los caracteres que componen una palabra no se encuentran en una lista de caracteres prohibidos.

letras_prohibidas = ['x', 'y', 'z']
inputPalabra = input(str('Ingrese una palabra: '))

def palabra_no_tiene_letras(palabra, letras_prohibidas):
    for letra in palabra:
        if letra in letras_prohibidas:
            return True
    return False
            
tieneLetrasProhibidas = palabra_no_tiene_letras(inputPalabra, letras_prohibidas)
print(tieneLetrasProhibidas)