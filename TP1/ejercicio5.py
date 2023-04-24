# Escriba un programa que pida al usuario que ingrese 3 números. Sume los dos primeros y luego multiplique este total por el tercero. Mostrar la respuesta en pantalla de la siguiente forma: “La respuesta es XX”

numero_1 = int(input('Ingrese el primer número: '))
numero_2 = int(input('Ingrese el segundo número: '))
numero_3 = int(input('Ingrese el tercer número: '))

calculo = (numero_1 + numero_2) * numero_3

print('La respuesta es', calculo)