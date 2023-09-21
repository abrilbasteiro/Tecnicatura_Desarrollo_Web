from calendar import isleap

def anio_bisiesto(anio):
    return isleap(anio)

def calcular_dias_mes(mes, anio_bisiesto):
    mesesCon31 = [1, 3, 5, 7, 8, 10, 12]
    mesesCon30 = [4, 6, 9, 11]
    if mes in mesesCon31:
        return 31
    elif mes in mesesCon30:
        return 30
    elif mes == 2 and anio_bisiesto == True:
        return 29
    elif mes == 2 and anio_bisiesto == False:
        return 28

def edadEnDias(hora_local, anio_comienzo, anio_fin):
    dias = 0
    for a in range(anio_comienzo, anio_fin):
        if (anio_bisiesto(a)): dias = dias + 366
        else: dias = dias + 365
    for m in range(1, hora_local.tm_mon):
        dias = dias + calcular_dias_mes(m, anio_bisiesto(hora_local.tm_year))
        dias = dias + hora_local.tm_mday
    return dias