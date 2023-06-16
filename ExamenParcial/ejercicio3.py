# EJERCICIOS 3)
# Dada la siguiente lista de mes del año:
# año=[“enero”,”febrero”,”marzo”,”abril”,”mayo”,”junio”,”julio”]
# Escriba un programa Python que permita al usuario:
# a) Ingresar los seis meses restantes e incluirlos en la lista.
# b) Mostrar la lista con los meses del primer cuatrimestre del año.
# c) Mostrar la lista con los meses del segundo semestre del año.
# d) Mostrar la lista a la inversa, desde diciembre a enero.
# e) Por último, vaciar la lista.

print('Las opciones son: \n\t1) Agregar los meses restantes a la lista \n\t2) Mostrar el primer cuatrimestre del año \n\t3) Mostrar el segundo cuatrimestre del año \n\t4) Mostrar la lista de meses invertida \n\t5) Vaciar la lista \n\t6) Salir')

def completar_año(año):
    restantes = ['agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
    if len(año) != 12:
        año += restantes
    
def ejecutar_accion():
    fin = False
    año = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio']
    
    while fin == False: 
        opcion = int(input('Ingrese el numero de opcion elegida: '))
        match opcion:
            case 1:
                completar_año(año)
                print('Se agregaron los meses restantes y la lista quedo asi:', año)
            case 2:
                primer_cuatrimestre = año[:4]
                print('Los meses del primer cuatrimestre son:', primer_cuatrimestre)
            case 3:
                completar_año(año)
                segundo_cuatrimestre = año[4:8]
                print('Los meses del segundo cuatrimestre son:', segundo_cuatrimestre)
            case 4:
                completar_año(año)
                año.reverse()
                print('La lista de meses invertida es la siguiente:', año)
            case 5:
                año.clear()
                print('La lista fue vaciada y el programa finalizara. Lista:', año)
                fin = True
            case 6:
                fin = True
            case _:
                print('La opcion no existe')

ejecutar_accion()