# Escriba un programa Python que cuente con dos listas, la primera de ellas almacenará strings con tareas pendientes y la segunda almacenará strings con tareas terminadas. Permita al usuario:
#   a. Agregar nuevas tareas pendientes.
#   b. Marcar las tareas pendientes como terminadas. Al hacer esto, la tarea deberá pasar de la lista de pendientes a la de terminadas.
# Nota: posterior a cada operación deberá mostrar por pantalla el estado actual de ambas listas.

tareas_pendientes = ['Cocinar', 'Planchar']
tareas_terminadas = []

def agregar_tarea():
    tarea = input('Ingrese la tarea que desea agregar: ')
    tareas_pendientes.append(tarea)
    print('Tareas pendientes: ', tareas_pendientes, '\nTareas terminadas: ', tareas_terminadas)
    
def pasar_tarea():
    print('Las tareas pendientes son: ')
        
    for tarea in tareas_pendientes:
        print(tareas_pendientes.index(tarea), '-',  tarea)
        
    tarea = int(input('Ingrese el numero de la tarea que desea marcar como terminada: '))
    
    if tarea not in range(0,len(tareas_pendientes)):
        print('Debe seleccionar una opcion correcta (1 o 2)')
        tarea = int(input('Ingrese el numero de la tarea que desea marcar como terminada: '))
        
    tareas_terminadas.append(tareas_pendientes[tarea])
    tareas_pendientes.pop(tarea)
    
    print('Tareas pendientes: ', tareas_pendientes, '\nTareas terminadas: ', tareas_terminadas)
    
    
def manejar_tareas():
    salir = False
    
    while(not salir):
        print('Usted puede: \n\t 1) Agregar nueva tarea pendiente \n\t 2) Marcar tarea pendiente como terminada \n\t 3) Salir')
        opcion_elegida = int(input('Ingrese el numero de opcion elegida: '))
            
        if opcion_elegida == 1:
            agregar_tarea()
        elif opcion_elegida == 2:
            pasar_tarea()
        elif opcion_elegida == 3:
            salir = True
        else:
            print('Debe seleccionar una opcion correcta (1, 2 o 3)')


manejar_tareas()