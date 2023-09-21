# Escribir un programa que resuelva la secuencia de Fibonacci a pedido del usuario. Deberá codificar una función fibonacci(numero), cuyo parámetro numero debe ser ingresado por el usuario y su tipo, al igual que en el ejercicio anterior, validado. La función debe encargarse de calcular la secuencia para dicho número. A continuación, una descripción matemática de la famosa secuencia:

def fibonacci(numero):
    secuenciaFibonacci = [1, 1]
    while len(secuenciaFibonacci) < numero:
        proximoNumero = secuenciaFibonacci[-1] + secuenciaFibonacci[-2]
        secuenciaFibonacci.append(proximoNumero)
    return secuenciaFibonacci
5
while True:
    numero = input('Ingrese un numero: ')
    if numero.isdigit():
        numero = int(numero)
        secuenciaFibonacci = fibonacci(numero)
        print('El resultado es:', secuenciaFibonacci)
        break
    else:
        print('ERROR. Ingrese un numero')