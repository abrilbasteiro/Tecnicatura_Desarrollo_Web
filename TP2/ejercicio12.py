# Pedir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día ingresado no es ninguno de esos, imprimir otro mensaje

def imprimir_mensaje(dia):
    mensaje = ''
    
    match dia.lower():
        case 'lunes':
            mensaje = 'Hoy es lunes :('
        case 'viernes':
            mensaje = 'Por suerte es viernes!'
        case 'sabado' | 'domingo':
            mensaje = 'A disfrutar el finde!'
        case _:
            mensaje = 'Es un dia cualquiera'
    
    print(mensaje)

dia = input('Ingrese un dia de la semana: ')

imprimir_mensaje(dia)