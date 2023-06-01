# Programe una aplicación de consola Python que brinde al usuario la posibilidad de a partir de una lista vacía:
#   a. Agregar un elemento al final.
#   b. Agregar un elemento al principio.
#   c. Quitar un elemento al final.
#   d. Quitar un elemento al principio.

lista = []

print('Las opciones son: \n\t1) Agregar un elemento al final de la lista \n\t2) Agregar un elemento al principio de la lista \n\t3) Quitar un elemento al final de la lista \n\t4) Agregar un elemento al principio de la lista \n')

opcion_elegida = int(input('Ingrese el numero de opcion elegida: '))

def ejecutar_accion(opcion):
    match opcion:
        case 1:
            elemento = input('Ingrese el elemento que quiere agregar al final: ')
            lista.append(elemento)
            print('Se agrego un elemento al final y la lista quedo asi:', lista)
        case 2:
            elemento = input('Ingrese el elemento que quiere agregar al inicio: ')
            lista.insert(0, elemento)
            print('Se agrego un elemento al principio  y la lista quedo asi:', lista)
        case 3:
            if len(lista) < 1:
                print('La tabla esta vacia y no se pueden eliminar elementos')
            else:
                lista.pop()
                print('Se quito el ultimo elemento y la lista quedo asi:', lista)
        case 4:
            if len(lista) < 1:
                print('La tabla esta vacia y no se pueden eliminar elementos')
            else:
                lista.pop(0)
                print('Se quito el primer elemento y la lista quedo asi:', lista)
        case _:
            print('La opcion no existe')

ejecutar_accion(opcion_elegida)