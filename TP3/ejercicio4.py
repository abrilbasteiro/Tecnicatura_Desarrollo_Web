# Dada la siguiente lista: países = [“Argentina,”Brasil”, “Bolivia”,”Paraguay”,”Venezuela”], realizar lo siguiente:
#   a. Imprimir la cantidad de elementos que tiene la lista.
#   b. Imprimir el primer y último elemento.
#   c. Imprimir el resto.
#   d. Permitir que el usuario ingrese un país e imprimir el índice si el país se encuentra en la lista. Si no se encuentra, imprimir un mensaje advirtiendo al usuario.
#   e. Permitir al usuario ingresar un número igual o menor a la cantidad de elementos de la lista. Quitar el elemento correspondiente de esa posición.
#   f. Imprimir la lista en orden inverso.
#   g. Vaciar la lista.

paises = ['Argentina', 'Brasil', 'Bolivia', 'Paraguay', 'Venezuela']


# a. Imprimir la cantidad de elementos que tiene la lista.
print('La lista tiene', len(paises), 'elementos')


#   b. Imprimir el primer y último elemento.
print('El primer elemento es', paises[0], 'y el último es', paises[-1])


#   c. Imprimir el resto.
print('Los elementos restantes son:', paises[1:-1] )


#   d. Permitir que el usuario ingrese un país e imprimir el índice si el país se encuentra en la lista. Si no se encuentra, imprimir un mensaje advirtiendo al usuario.
pais = str(input('Ingrese un país: ')).capitalize()

if pais in paises:
    print('Su país se encuentra en el índice', paises.index(pais))
else:
    print('El país ingresado no se encuentra en la lista.')

#   e. Permitir al usuario ingresar un número igual o menor a la cantidad de elementos de la lista. Quitar el elemento correspondiente de esa posición.
numero = int(input('Ingrese un numero del 0 al ' + str(len(paises)) + ': '))

if numero > len(paises) or numero < 0:
    print('El numero debe estar entre 0 y', len(paises))
    numero = int(input('Ingrese un numero del 0 al ' + str(len(paises)) + ': '))
else:
    paises.pop(numero)
    print('Ahora los países son:', paises)
    
    
#   f. Imprimir la lista en orden inverso.
print('La lista invertida quedaría asi:', list(reversed(paises)))


#   g. Vaciar la lista.
paises.clear()
print('Si vaciamos la lista quedaría así:', paises)