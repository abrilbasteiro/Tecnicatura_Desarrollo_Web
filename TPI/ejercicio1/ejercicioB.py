# Escribir una función de nombre es_abc(palabra) la cual retorne True siempre y cuando las letras que componen dicha palabra estén en orden alfabético, y False en caso contrario.

inputPalabra = input(str('Ingrese una palabra: '))

def es_abc(palabra):
    palabraOrdenada = list(palabra)
    palabraOrdenada.sort()
    print('orde', ''.join(palabraOrdenada))
    print('pala',palabra)
    if palabra == ''.join(palabraOrdenada):
        return True
    return False
            
estaOrdenada = es_abc(inputPalabra)
print(estaOrdenada)