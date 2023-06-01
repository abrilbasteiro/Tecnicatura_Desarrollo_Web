# Crear un programa que almacene en una lista las materias de esta u otra carrera y que las muestre por pantalla. (La lista debe ser predefinida, no debe ser ingresada por el usuario).

materias = [
    'Introducción a la informática',
    'Programación I',
    'Diseño Gráfico',
    'Arquitectura de Computadoras',
    'Programación II',
    'Sistemas Operativos',
    'Introducción al Desarrollo Web',
    'Bases de Datos',
    'Redes de Datos',
    'Programación III',
    'Ingeniería de Software',
    'Desarrollo de Aplicaciones Web',
    'Desarrollo para Móviles',
    'Multimedia y Juegos en Web'
]

print('Las materias de la Tecnicatura en Desarrollo Web son: \n\t - ' + '\n\t - '.join(materias))