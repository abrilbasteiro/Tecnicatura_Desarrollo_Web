# Se agrega el siguiente diagrama, que intenta representar a los humanos del referenciado universo:
# Humano
# <<Atributos de clase>>
# especie: string
# <<Atributos de instancia>>
# nombre: string
# estadoAsustado: boolean
# <<Constructores>>
# Humano(nom: string)
# <<Comandos>>
# establecerNombre(nom: string)
# establecerEstadoAsustado(est: boolean)
# <<Consultas>>
# obtenerNombre(): string
# obtenerEstadoAsustado(): boolean
# Habiendo analizado el diagrama, genere la clase Humano con los atributos y servicios
# mencionados en dicho diagrama.
# a. El atributo de clase especie debe tener valor “humano”.
# b. El valor inicial de estadoAsustado debe ser False.

class Humano:
    especie = 'Humano'
    estadoAsustado = False
    
    def __init__(self, nombre):
        self.establecerNombre(nombre)
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Esta asustado?: {self.estadoAsustado}"
    
    def establecerNombre(self, nom):
        self.nombre = nom
    
    def establecerEstadoAsustado(self, est):
        self.estadoAsustado = est
    
    def obtenerNombre(self):
        return self.nombre
    
    def obtenerEstadoAsustado(self):
        return self.estadoAsustado    

# TEST:
# humano1 = Humano('Abril')
# print(humano1.nombre, humano1.estadoAsustado)
# humano1.establecerEstadoAsustado(True)
# humano1.establecerNombre('Celeste')
# print(humano1.nombre, humano1.estadoAsustado)