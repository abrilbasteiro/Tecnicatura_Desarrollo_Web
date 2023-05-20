# Que el usuario ingrese dos números y muestre cuál de los dos es menor. Considerar el caso en que ambos números son iguales.
    
numero1 = float(input('Ingrese el primer numero: '))
numero2 = float(input('Ingrese el segundo numero: '))

def mostrar_menor(numero1, numero2):
    if numero1 < numero2:
        print('El numero', numero1, 'es menor')
    elif numero1 > numero2:
        print('El numero', numero2, 'es menor')
    else:
        print('Ambos numeros son iguales')

mostrar_menor(numero1, numero2)