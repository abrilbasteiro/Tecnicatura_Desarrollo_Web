# Un portal web requiere un formulario de alta de usuario donde se ingrese, mínimamente, un usuario y su correspondiente contraseña. Escriba, en Python, una función contrasena_valida(contrasena) que devuelva True en caso de superar las siguientes validaciones sobre la contraseña proporcionada por el usuario:
# i. Longitud entre 6 y 20 caracteres.
# ii. Debe contener al menos un número.
# iii. Debe contener al menos dos mayúsculas.
# iv. Debe contener al menos un carácter especial.
# v. No puede contener espacios.
# La salida esperada es la siguiente:
# abc.123 es válida: False
# Abc.123 es válida: False
# AbC.123 es válida: True
# AbC.1 23 es válida: False
# ÁbC.123 es válida: False

import re

contrasena = input('Ingrese una constraseña: ')

def tieneLongitudValida (contrasena):
    if len(contrasena) >= 6 and len(contrasena) <= 20:
        print('tiene leng')
        return True
    else:
        
        print('no tiene leng')
        
        return False

def tieneNumero (contrasena):
    if re.search(r'\d', contrasena):
        print('tiene numero')
        return True
    else:
        print('no tiene numero')
        return False
 
def tiene2Mayusculas (contrasena):
    if len(re.findall(r'[A-Z]', contrasena)) >= 2:
        print('tiene mayus')
        return True
    else:
        print('no tiene mayus')
        return False
    
def tieneCaracteresEspeciales (contrasena):
    if len(re.findall(r'[$&+,:;=?@#|<>.^*()%!-]', contrasena)):
        print('tiene especial')
        return True
    else:
        print('no tiene especial')
        return False

def noTieneEspacios (contrasena):
    if " " not in contrasena:
        print('no tiene espacio')
        return True
    else:
        print('tiene especio')
        return False

def contrasena_valida(contrasena):
    if tieneLongitudValida(contrasena) and tieneNumero(contrasena) and tiene2Mayusculas(contrasena) and tieneCaracteresEspeciales(contrasena) and noTieneEspacios(contrasena):
        return True
    
print('Es valida?', contrasena_valida(contrasena))