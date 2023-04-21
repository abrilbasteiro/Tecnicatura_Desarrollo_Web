# Sexto desafío
# Alumna: Abril Basteiro
# Fecha: 20/04/2023

#  Se necesita calcular el salario semanal de un trabajador de la construcción, dada la tarifa horaria y la cantidad de horas trabajadas diariamente

tarifa_horaria = float(input('Ingrese la tarifa horaria: '))
horas_trabajadas = float(input('Ingrese la cantidad de horas trabajadas: '))

salario_semanal = tarifa_horaria * horas_trabajadas * 5

print('El salario semanal de un trabajador de la construcción es de', salario_semanal, 'pesos')