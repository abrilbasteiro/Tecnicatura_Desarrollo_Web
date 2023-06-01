# Que reciba un número entero positivo y una potencia a elevar y que nos devuelva el resultado

def potenciar (base, exponente):
    print( base ** exponente)

numero_base = int(input('Ingrese un número base: '))
numero_exponente = int(input('Ingrese un exponente: '))

potenciar(numero_base, numero_exponente)