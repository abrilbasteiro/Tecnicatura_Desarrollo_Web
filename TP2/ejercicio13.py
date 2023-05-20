# Que resuelva el siguiente problema: los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo y muestre por pantalla el grupo que le corresponde.

nombre = (input('Ingrese su nombre: ')).lower()
sexo = (input('Ingrese su sexo (F / M): ')).lower()
grupo = ''

def asignar_grupo(nombre, sexo):
    if (sexo == 'f' and nombre[0] < 'm') or (sexo == 'm' and nombre[0] > 'n'):
        grupo = 'A'
    else:
        grupo = 'B'

    print("Le corresponde el grupo", grupo)

asignar_grupo(nombre, sexo)

