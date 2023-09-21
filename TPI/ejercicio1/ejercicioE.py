# Escribir un procedimiento numeros_par_impar(entrada) que, dada una lisa de números, eleve cada elemento impar en ella al cuadrado y los mueva a otra lista e imprima ambas. La lista de números la ingresa el usuario en forma de números separados por coma.
# Suponiendo que el usuario ingresa la siguiente lista: 
# 1,2,3,4,5,6,7,8,9
# Entonces, la salida del programa debería ser: 
# 2,4,6,8 
# 1,9,25,49,81

listaDeNumeros = input('Ingrese una lista de numeros: ')

def numeros_par_impar(entrada):
    numerosPares = []
    numerosImpares = []
    listaDeNumeros = entrada.split(',')
    for numero in listaDeNumeros:
        numero = int(numero)
        if numero % 2 == 0:
            numerosPares.append(numero)
        else:
            numero = numero ** 2
            numerosImpares.append(numero)
    print('Numeros pares:',  ','.join(map(str, numerosPares)))
    print('Numeros impares al cuadrado:', ','.join(map(str, numerosImpares)))
    
numeros_par_impar(listaDeNumeros)