# Escriba un procedimiento procesar_palabras(entrada) que acepte una secuencia de palabras separadas por coma, las ordene y las imprima. Suponiendo que la entrada provista al programa es la siguiente: te,felicito,que,bien,actuas. La salida esperada es: actuas,bien,felicito,que,te

entrada = "te,felicito,que,bien,actuas"

def procesar_palabras(entrada):
    entradaOrdenada = entrada.split(',')
    entradaOrdenada.sort()
    print('Salida: ', ','.join(entradaOrdenada))
       
procesar_palabras(entrada)