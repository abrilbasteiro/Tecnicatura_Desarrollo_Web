# Que nos calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

def calcular_precio (precio, porcentaje_iva):
    if porcentaje_iva == '':
        porcentaje_iva = 21
    
    iva = precio * porcentaje_iva / 100
    precio_total = precio + iva
    
    print('El total de la factura es de $' + str(precio_total))

precio_base = float(input('Ingrese el precio sin IVA: '))
iva_ingresado = float(input('Ingrese el porcentaje de IVA a aplicar: '))

calcular_precio(precio_base, iva_ingresado)