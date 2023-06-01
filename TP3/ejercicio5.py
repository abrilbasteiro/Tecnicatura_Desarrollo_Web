# Escriba un programa Python que solicite al usuario el ingreso de números enteros. Cuando el usuario ingrese la palabra “fin” el programa deberá concluir con la carga de datos. Cada uno de los números ingresados por el usuario deberá ser almacenado en una lista. A continuación, realice las siguientes tareas:
#   a. Determinar el máximo.
#   b. Obtener segundo valor máximo. Es decir el que le sigue al máximo.
#   c. Determinar el mínimo.
#   d. Calcular la multiplicación de todos los números de la lista.
#   e. Contar los valores pares e impares.
#   f. Remover los elementos repetidos.

fin = False
numeros = []

while fin == False:
    numero = input('Ingrese un número entero, para terminar ingrese "fin": ')
    if numero != 'fin':
        numeros.append(int(numero))
    else:
        fin = True
print('La lista inicial de números es:', numeros)

numeros.sort()


#   a. Determinar el máximo.
print('El valor máximo es: ', numeros[-1])


#   b. Obtener segundo valor máximo. Es decir el que le sigue al máximo.
print('El segundo valor máximo es: ', (numeros)[-2])


#   c. Determinar el mínimo.
print('El valor mínimo es: ', (numeros)[0])


#   d. Calcular la multiplicación de todos los números de la lista.
producto = 1
for numero in numeros:
    producto *= numero
print('El producto de todos los números de la lista es: ', producto)


#   e. Contar los valores pares e impares.
impares = 0
pares = 0

for numero in numeros:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
        
print('Hay', impares, 'números impares y', pares, 'números pares')


#   f. Remover los elementos repetidos.
print('La lista sin elementos repetidos quedaría asi: ', list(set(numeros)))