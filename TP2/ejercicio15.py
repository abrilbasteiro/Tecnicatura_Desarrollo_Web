# Que solicite al usuario una letra y, si es una vocal, muestre el mensaje “es vocal”. Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter, informarle que no se puede procesar el dato.

letra = input('Ingrese una letra: ')
vocales = ['a', 'e', 'i', 'o', 'u']
       
while len(letra) > 1 or letra == '':
    print('Debe ingresar solo una letra')
    letra = input('Ingrese una letra: ')
    
if letra in vocales:
    print('Es vocal')
else:
    print('Es consonante')