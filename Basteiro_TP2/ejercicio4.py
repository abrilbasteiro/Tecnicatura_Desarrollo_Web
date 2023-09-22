# Modificar la clase Monstruo de acuerdo a lo especificado al siguiente diagrama:
# 
# Monstruo
# <<Atributos de clase>>
# maxEnergia: int
# <<Atributos de instancia>>
# nombre: string
# especie: string
# energía: int
# <<Constructores>>
# Monstruo(nom, esp: string)
# <<Comandos>>
# establecerNombre(nom: string)
# establecerEspecie(esp: string)
# establecerEnergia(ene: int)
# asustar(hum: Humano)
# divertir(hum: Humano)
# <<Consultas>>
# obtenerNombre(): string
# obtenerEspecie(): string
# obtenerEnergia(): int
# 
# a. El comando asustar debe, además de decrementar la energía del monstruo en 10 unidades, cambiar el valor del atributo estadoAsustado de hum a True.
# b. El comando divertir debe decrementar la energía del monstruo en 20 unidades, cambiando el valor del atributo estadoAsustado de hum a False.
# c. Una vez codificadas las modificaciones sobre la clase del punto anterior, ejecute el siguiente programa Python y verifique que se cumpla la salida esperada.
# 
# El programa:
# sullivan = Monstruo(‘James P. Sullivan’, ‘leon’)
# mike = Monstruo(‘Mike Wazowski’, ‘ciclope’)
# boo = Humano(‘Boo’)
# print(sullivan.obtenerEnergia())
# print(mike.obtenerEnergia())
# print(boo.obtenerEstadoAsustado())
# sullivan.asustar(boo)
# print(sullivan.obtenerEnergia())
# print(mike.obtenerEnergia())
# print(boo.obtenerEstadoAsustado())
# mike.divertir(boo)
# print(sullivan.obtenerEnergia())
# print(mike.obtenerEnergia())
# print(boo.obtenerEstadoAsustado())
# La salida esperada es la siguiente:
# 100
# 100
# False
# 90
# 100
# True
# 90
# 80
# False

from ejercicio1 import Monstruo
from ejercicio2 import Humano  

class MonstruoModificado(Monstruo):
    def asustar(self, hum : Humano):
        hum.estadoAsustado = True
        self.energia -= 10
    def divertir(self, hum : Humano):
        hum.estadoAsustado = False
        self.energia -= 20

Monstruo = MonstruoModificado

# TEST:
sullivan = Monstruo('James P. Sullivan', 'leon')
mike = Monstruo('Mike Wazowski', 'ciclope')
boo = Humano('Boo')
print(sullivan.obtenerEnergia())
print(mike.obtenerEnergia())
print(boo.obtenerEstadoAsustado())
sullivan.asustar(boo)
print(sullivan.obtenerEnergia())
print(mike.obtenerEnergia())
print(boo.obtenerEstadoAsustado())
mike.divertir(boo)
print(sullivan.obtenerEnergia())
print(mike.obtenerEnergia())
print(boo.obtenerEstadoAsustado())