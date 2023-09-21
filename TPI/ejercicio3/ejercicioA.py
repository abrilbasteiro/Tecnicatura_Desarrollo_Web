# Escribir una función suma(numero) que resuelva la siguiente suma, asumiendo que numero = 10:
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
# En el programa que invoque dicha función:
# i. El usuario debe poder ingresar el valor del parámetro numero.
# ii. Debe validarse que el dato ingresado por el usuario corresponda a un dígito, y no a otro tipo de dato como un carácter.
# iii. El cálculo debe realizarse utilizando algún tipo de bucle (ej: for, while).

def suma(numero):
    suma = 0
    for numero in range (1, numero + 1):
        suma += numero    
    return suma

while True:
    numero = input('Ingrese un numero: ')
    if numero.isdigit():
        numero = int(numero)
        suma = suma(numero)
        print('La suma de los numeros entre el 1 y el', numero, 'es:', suma)
        break
    else:
        print('ERROR. Ingrese un numero')


# BONUS: Luego, codificar una función equivalente que utilice recursividad.

# def sumaRecursiva(numero):
#     if numero == 1 : return 1
#     else: return numero + sumaRecursiva(numero - 1)

# while True:
#     numero = input('Ingrese un numero: ')
#     if numero.isdigit():
#         numero = int(numero)
#         suma = sumaRecursiva(numero)
#         print('La suma de los numeros entre el 1 y el', numero, 'es:', suma)
#         break
#     else:
#         print('ERROR. Ingrese un numero')
            
