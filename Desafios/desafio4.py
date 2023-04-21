# Cuarto desafío
# Alumna: Abril Basteiro
# Fecha: 20/04/2023

# Elaborar un algoritmo que permita ingresar el número de partidos Ganados, Perdidos y Empatados, por un equipo en el torneo apertura, se debe de mostrar su puntaje total. (Teniendo en cuenta que por cada partido ganado obtendrá 3 puntos, empatado 1 punto y perdido 0 puntos.)

partidos_ganados = int(input('Ingrese cuántos partidos ganaron: '))
partidos_perdidos = int(input('Ingrese cuántos partidos perdieron: '))
partidos_empatados = int(input('Ingrese cuántos partidos empataron: '))

puntaje_ganado = partidos_ganados * 3
puntaje_perdido = partidos_perdidos * 0
puntaje_empatado = partidos_empatados * 1

puntaje_total = puntaje_ganado + puntaje_perdido + puntaje_empatado

print('El puntaje total del equipo en el torneo apertura es:', puntaje_total)