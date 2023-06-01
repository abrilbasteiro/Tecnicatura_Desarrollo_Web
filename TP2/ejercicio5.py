# Que dado tres números ingresados por el usuario nos devuelva el promedio.

def calcular_promedio (numero1, numero2, numero3):
    promedio = (numero1 + numero2 + numero3) / 3
    print('El promedio de los numeros ingresados es de ', round(promedio,2) )

numero1 = float(input('Ingrese el primer numero: '))
numero2 = float(input('Ingrese el segundo numero: '))
numero3 = float(input('Ingrese el tercer numero: '))

calcular_promedio(numero1, numero2, numero3)