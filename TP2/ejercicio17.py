# Que muestre todos los números primos entre 0 y 100 e imprima cuántos números primos hay.

numeros = range(0,101)
contador_numeros_primos = 0
numeros_primos = []

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    numeros_primos.append(numero)
    return True

for numero in numeros:
    if es_primo(numero):
        contador_numeros_primos += 1
        
print("Entre el 0 y el 100 hay", contador_numeros_primos, 'numeros primos.')
print("Los numeros primos entre el 0 y el 100 son:", numeros_primos)