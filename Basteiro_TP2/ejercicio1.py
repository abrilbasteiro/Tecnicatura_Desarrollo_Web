# 1. Dado el siguiente diagrama de clases:
# Monstruo
#- <<Atributos de clase>>
#--maxEnergia: int
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
# asustar()
# <<Consultas>>
# obtenerNombre(): string
# obtenerEspecie(): string
# obtenerEnergia(): int
# 
# Genere la clase Monstruo, conteniendo los atributos y servicios mencionados en el
# diagrama de clases anterior.

# a. El atributo de clase maxEnergía debe tener un valor de 100.
# b. El valor inicial de energia debe ser igual a maxEnergía.
# c. El método asustar debe decrementar la energía del monstruo en 10 unidades

class Monstruo:
    maxEnergia = 100
    def __init__(self, nombre, especie):
        # SELF O MONSTRUO.MAX?
        self.energia = self.maxEnergia
        self.establecerEspecie(especie)
        self.establecerNombre(nombre)
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Especie: {self.especie}, Energía: {self.energia}"
    
    def establecerNombre(self, nom):
        self.nombre = nom
    
    def establecerEspecie(self, esp):
        self.especie = esp
    
    def establecerEnergia(self, ene):
        if self.energia + ene > Monstruo.maxEnergia:
            self.energia = Monstruo.maxEnergia
        else:
            self.energia = ene
    
    def asustar (self):
        if self.energia >= 10:
            self.energia -= 10
        else:
            self.energia = 0
    
    def obtenerNombre(self):
        return self.nombre
    
    def obtenerEspecie(self):
        return self.especie
    
    def obtenerEnergia(self):
        return self.energia

# TEST:
# monstruo1 = Monstruo('Pancha', 'Perro')
# monstruo2 = Monstruo('Negro', 'Perro')
# monstruo1.asustar()
# monstruo1.asustar()
# monstruo2.establecerEnergia(20)
# print('Monstruo 1', monstruo1.nombre, 'especie', monstruo1.especie, 'energia', monstruo1.energia)
# print('Monstruo 2', monstruo2.nombre, 'especie', monstruo2.especie, 'energia', monstruo2.energia)