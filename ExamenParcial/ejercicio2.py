# EJERCICIOS 2)
# Escriba un programa Python que permita al usuario ingresar 6 números enteros y que imprima por pantalla 2 listas: una con los números pares y otra con los impares. Ambas deben estar ordenadas.

impares = []
pares = []

for n in range(6):
    numero = int(input('Ingrese un numero: '))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

pares.sort()
impares.sort()

print('Pares:', pares)  
print('Impares:', impares)  