# . Escriba un programa que indique si un texto es palíndromo, es decir, se escribe igual al derecho que al revés. Por ejemplo: rayar, kayak, somos.

texto = input('Ingrese el texto que desea invertir: ')

es_palindromo = texto == texto[::-1]

print(es_palindromo)