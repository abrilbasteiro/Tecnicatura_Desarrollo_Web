# Pida al usuario un número x de días y luego mostrar por pantalla cuántas horas, minutos y segundos son esos números de días

cantidad_de_dias = int(input('Ingrese la cantidad de días: '))

horas = cantidad_de_dias * 24
minutos = horas * 60
segundos = minutos * 60

print(cantidad_de_dias, 'días equivalen a:\n', '-', horas, 'horas\n', '-', minutos, 'minutos \n', '-', segundos, 'segundos')