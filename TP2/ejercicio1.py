# Que al pasarle una cadena <nombre> nos muestre por pantalla el saludo ¡Hola <nombre>!

nombre = str(input('Ingrese su nombre: '))

def saludar (nombre):
    print('¡Hola, '+ nombre + "!")

saludar(nombre)