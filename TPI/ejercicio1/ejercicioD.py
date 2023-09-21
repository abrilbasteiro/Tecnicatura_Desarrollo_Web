# Dadas dos listas, lista1 y lista2, escribir un método listas_diferencia(lista1, lista2) que tome ambas como parámetros e imprima dos listas, cada una con: 
# i. Los elementos en común, en orden inverso.
# ii. Los elementos no comunes, en orden alfabético.
# El programa debería arrojar el siguiente resultado:
# listas(['b', 'a', 'c'], ['e', 'b', 'd', 'c'])
# ['c', 'b']
# ['a', 'e', 'd']

lista1 = ['e', 'b', 'd', 'c']
lista2 = ['b', 'a', 'c']

def listas_diferencia(lista1, lista2):
    elementosEnComun = list(set(lista1) & set(lista2))
    elementosEnComun.reverse()
    elementosNoComunes = sorted(set(lista1) ^ set(lista2))
    print('Elementos en comun: ', elementosEnComun)
    print('Elementos no comunes: ', elementosNoComunes)
    
listas_diferencia(lista1, lista2)