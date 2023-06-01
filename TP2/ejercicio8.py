# Pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no

def es_mayor(edad):
    print('Es mayor de edad') if edad >= 18 else print('No es mayor de edad')

edad = int(input('Ingrese su edad: '))

es_mayor(edad)