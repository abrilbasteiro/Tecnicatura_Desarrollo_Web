# Que dada la base y altura de un triángulo nos calcule su área.

def calcular_area (base, altura):
    area = base * altura / 2
    print('El area del triangulo es de ', area, 'cm.' )

base = float(input('Ingrese la base del triangulo en cm: '))
altura = float(input('Ingrese la altura del triangulo en cm: '))

calcular_area(base, altura)