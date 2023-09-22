# Construya un programa, utilizando la clase proveedora MonstersInc que, a partir de la entrada del usuario permita:
# a. Llamar a los métodos agregarMonstruo y agregarHumano.
# b. Filtrar a los monstruos con un nivel de energía específico por debajo de algún valor.
# c. Filtrar a los humanos por sus dos posibles estados: asustado y no asustado.
# Para la construcción de dicho programa crear una clase de nombre TesterMonstersInc que actúe como cliente de la clase proveedora MonstersInc, cuyo único servicio sea de nombre main, sin parámetros, que ejecute los puntos descriptos anteriormente. A continuación, un ejemplo de como dicho programa puede ser construido:
# class TesterMonstersInc:
# def main():
# Solución de los puntos 6.a., 6.b, 6.c, ...
# if __name__ == ‘__main__’:
# testerMonstersInc = TesterMonstersInc()
# testerMonstersInc.main()

from ejercicio5 import MonstersInc
from ejercicio1 import Monstruo
from ejercicio2 import Humano

class TesterMonstersInc:
    def main(self):
        salir = False
        monstersIncInstance = MonstersInc()            
        monstruos = monstersIncInstance.obtenerMonstruos()
        humanos = monstersIncInstance.obtenerHumanos()
        while(not salir):
            print('\n----------------------------------------------------')
            print('Usted puede: \n\t 1) Agregar un Monstruo \n\t 2) Agregar un humano \n\t 3) Filtrar monstruos con un nivel de energia por debajo de un valor \n\t 4) Filtrar humanos asustados \n\t 5) Filtrar humanos no asustados \n\t 6) Salir \n\t')
            opcion_elegida = int(input('Ingrese el numero de opcion elegida: '))
            print('\n')
            match opcion_elegida:
                case 1:
                    nombre = str(input('Ingrese el nombre del monstruo: '))
                    especie = str(input('Ingrese la especie del monstruo: '))
              
                    monstersIncInstance.agregarMonstruo(Monstruo(nombre, especie))
                    monstruos = []
                    for monstruo in monstersIncInstance.obtenerMonstruos():
                        monstruos.append(str(monstruo))
                    print('Se agrego el monstruo', nombre, 'y la lista quedo asi:\n', "\n".join(monstruos))
                    
                case 2:
                    humano = str(input('Ingrese el nombre del humano que quiere agregar: '))
                    monstersIncInstance.agregarHumano(Humano(humano))
                    humanos = []
                    for humano in monstersIncInstance.obtenerHumanos():
                        humanos.append(str(humano))
                    print('Se agrego el humano', humano.nombre, 'y la lista quedo asi:\n', "\n".join(humanos))
                    
                case 3:
                    energia = int(input('Ingrese nivel de energia: '))
                    monstruosFiltrados = [mon for mon in monstruos if mon.energia < energia]
                    print('Los monstruos con nivel de energia por debajo de', energia, 'son', monstruosFiltrados)
                    
                case 4:
                    humanosAsustados = ", ".join([hum for hum in humanos if hum.estadoAsustado])
                    print('Los humanos asustados son:', humanosAsustados)
                    
                case 5:
                    humanosNoAsustados = ", ".join([hum.nombre for hum in humanos if hum.estadoAsustado == False])
                    print('Los humanos no asustados son:', humanosNoAsustados)
                    
                case 6:
                    salir = True
                    
                case _:
                    print('La opcion no existe')
                    
if __name__ == '__main__':
    testerMonstersInc = TesterMonstersInc()
    testerMonstersInc.main()