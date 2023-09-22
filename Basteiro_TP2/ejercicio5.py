# Construya una clase MonstersInc como la especificada en el siguiente diagrama de clases:
# MonstersInc
# <<Atributos de clase>>
# <<Atributos de instancia>>
# monstruos: Monstruo[]
# humanos: Humano[]
# <<Constructores>>
# MonstersInc()
# <<Comandos>>
# agregarMonstruo(mon: Monstruo)
# agregarHumano(hum: Humano)
# eliminarMonstruo(mon: Monstruo)
# eliminarHumano(hum: Humano)
# <<Consultas>>
# obtenerMonstruos(): Monstruo[]
# obtenerHumanos(): Humano[]
# a. Los comandos agregarMonstruo y agregarHumano deben agregar un objeto de tipo Monstruo o un objeto de tipo Humano a las listas monstruos y humanos de dicho objeto, respectivamente.
# b. Los comandos eliminarMonstruo y eliminarHumano deben eliminar un objeto de tipo Monstruo o un objeto de tipo Humano de las listas monstruos y humanos de dicho objeto, respectivamente.

from ejercicio1 import Monstruo
from ejercicio2 import Humano

class MonstersInc:

    def __init__(self):
        self.monstruos = []
        self.humanos = []
    
    def agregarMonstruo(self, mon : Monstruo):
        if isinstance(mon, Monstruo):
            self.monstruos.append(mon)
        else:
            print('El objeto que quiere agregar no es un monstruo')
    
    def agregarHumano(self, hum : Humano):
        if isinstance(hum, Humano):
            self.humanos.append(hum)
        else:
            print('El objeto que quiere agregar no es un humano')
    
    def eliminarMonstruo(self, mon : Monstruo):
        if isinstance(mon, Monstruo):
            self.monstruos.remove(mon)
        else:
            print('El objeto que quiere eliminar no es un monstruo')
    
    def eliminarHumano(self, hum : Humano):
        if isinstance(hum, Humano):
            self.humanos.remove(hum)
        else:
            print('El objeto que quiere eliminar no es un humano')
    
    def obtenerMonstruos(self):
        return self.monstruos
    
    def obtenerHumanos(self):
        return self.humanos