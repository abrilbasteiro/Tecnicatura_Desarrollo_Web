# Que pida un año y que escriba si es bisiesto o no. Les recordamos que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí. Algunos ejemplos de posibles respuestas: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900 no es bisiesto.

año = int(input('Ingrese un año: '))

def es_biciesto(año):
    if año % 4 == 0:
        if año % 100 == 0:
            if año % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

if es_biciesto(año):  
    print('El año es biciesto')
else:
    print('El año no es biciesto')