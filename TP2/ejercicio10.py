# Que el usuario ingrese un número entero positivo y muestre por pantalla lo siguiente:
# a. Todos los números impares desde 1 hasta ese número separados por comas.
# b. La cuenta atrás desde ese número hasta cero separados por comas.
# c. Que indique si es primo o no.
# d. Por último, su factorial.

numero = int(input('Ingrese un numero: '))

def ejercicio (numero):
    rango = range(1, numero + 1)
    impares = '' 
    
    # a. Todos los números impares desde 1 hasta ese número separados por comas.
    for i in rango:
        if i % 2 != 0:
            impares += str(i) + ', '

    print('Los numeros impares entre el 1 y', numero, 'son:', impares[:-2])
    
    # b. La cuenta atrás desde ese número hasta cero separados por comas.
    cuenta_regresiva = list(rango)
    cuenta_regresiva.reverse()
    print('La cuenta regresiva desde', numero, 'hasta 1 es:', ', '.join(map(str, cuenta_regresiva)))
    
    # c. Que indique si es primo o no.
    def es_primo(numero):
        if numero < 2 or numero % 2 == 0:
            return False
        for i in range(3, numero, 2):
            if numero % i == 0:
                return False
        return True

    print('El numero', numero, 'es primo') if es_primo(numero) else print('El numero', numero, 'no es primo')
    
    # d. Por último, su factorial.
    factorial = numero
    contador = numero
    
    while contador > 1:
        factorial = factorial * (contador - 1)
        contador -= 1
        
    print('El factorial de', numero, 'es', factorial)
    
ejercicio(numero)