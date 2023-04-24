# Escriba un programa que permita al usuario ingresar la base y altura de un triángulo para luego imprimir por pantalla la superficie total.

base = float(input('¿Cuántos centímetros mide la base del triángulo?: '))
altura = float(input('¿Cuánto centímetros mide la altura del triángulo?: '))

superficie = base * altura / 2

print('La superficie total del triángulo es de', superficie, 'centímetros')