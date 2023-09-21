import json

# Leer recetas del json
def leer_json_recetas():
    with open('recetas.json') as json_file:
        return json.load(json_file)

# Agregar receta al json
def escribir_json_recetas(recetas):
    with open('recetas.json', "w") as file:
        json.dump(recetas, file, indent=4)

# Mostrar recetas del json
def lista_recetas(recetas):
    contador = 1
    print("\nLas recetas guardadas son:")
    for receta in recetas:
        print(str(contador)+") "+receta['nombre'])
        contador += 1

# Mostrar una receta segun id
def mostrar_receta(recetas):
    lista_recetas(recetas)

    try:
        id_receta = int(input("\nIndique qué receta quiere cocinar: "))

        receta = recetas[id_receta-1]

        if receta == "":
            print("ID no encontrado")

        detalle_receta(receta)

    except:
        print("ID no encontrado")

# Mostrar detalle de la receta seleccionada
def detalle_receta(receta):
    print("\nNecesitará", receta['tiempo'], "minutos para realizar esta receta")
    
    print("Los ingredientes a usar son:")
    for ingrediente in receta['ingredientes']:
        print("\t-", ingrediente.capitalize())
    
    print("Los pasos a seguir son:")
    for paso in receta['procedimiento']:
        print("\t-", paso)

# Solicitar al usuario los pasos a seguir para elaborar la nueva receta
def solicitar_procedimiento():
    fin = False
    contador = 1
    procedimiento = []
    while not fin:
        paso = input('Ingrese el paso numero '+str(contador)+' si ya ha terminado ingrese "fin": ')
        if paso != 'fin':
            procedimiento.append(paso)
            contador += 1
        else:
            fin = True
    return procedimiento

# Solicitar al usuario los detalles para agregar una nueva receta a la lista
def agregar_receta(recetas):
    id = len(recetas) + 1
    nombre = input('Nombre del plato: ')
    ingredientes = input('Ingresa los ingredientes separados con coma: ').lower().replace(', ', ',').split(",")
    procedimiento = solicitar_procedimiento()
    tiempo = int(input('Ingrese el tiempo de elaboracion en minutos: '))

    nueva_receta = {
        'id': id,
        'nombre': nombre,
        'ingredientes': ingredientes,
        'procedimiento': procedimiento,
        'tiempo': tiempo
    }    

    recetas.append(nueva_receta)
    escribir_json_recetas(recetas)

# Eliminar una receta de la lista
def borrar_receta(recetas):
    lista_recetas(recetas)
    receta_a_eliminar = int(input('Ingrese el numero de la receta que quiere eliminar: '))
    recetas.remove(recetas[receta_a_eliminar-1])
    print('La receta se ha eliminado')
    escribir_json_recetas(recetas)

# Modificar una receta
def modificar_receta(recetas):
    lista_recetas(recetas)
    elementos = {1: 'nombre', 2: 'ingredientes', 3: 'procedimiento', 4: 'tiempo'}
    receta_a_modificar = int(input('Ingrese el numero de la receta que quiere modificar: '))

    print("Los elementos de la receta son:")
    print("1) Titulo")
    print("2) Ingredientes")
    print("3) Preparacion")
    print("4) Tiempo de elaboracion")

    opcion = int(input('\nIngrese el numero de la opcion elegida: '))

    print("\nEl valor actual es: ", recetas[receta_a_modificar-1][elementos[opcion]])

    if opcion in (2, 3):
        nuevo_valor = input('\nIngrese el nuevo valor separado con comas para {}: '.format(elementos[opcion])).lower()
        nuevo_valor = nuevo_valor.replace(', ', ',').split(",")
    else:
        nuevo_valor = input('\nIngrese el nuevo valor para {}: '.format(elementos[opcion]))      

    recetas[receta_a_modificar-1][elementos[opcion]] = nuevo_valor
    escribir_json_recetas(recetas)
    
    print('Se modifico la receta')

# Muestra la lista de recetas segun ingrediente
def recetas_por_ingrediente(recetas):
    ingredientes = input('\nIngrese los ingredientes separados por coma: ').lower().replace(', ', ',').split(',')
    
    recetas_filtradas = []
    
    for receta in recetas:
        if all(value in receta['ingredientes'] for value in ingredientes):
            recetas_filtradas.append(receta)

    if recetas_filtradas == []:
        print("\nNo hay ninguna receta con los ingredientes: ", ingredientes)
    else:
        print("\nLas recetas que usan los ingredientes ", ingredientes, " son:")
        for receta in recetas_filtradas:
            print("- ", receta['nombre'])
    

# Mostrar el menu principal
def mostrar_opciones():
    recetas = leer_json_recetas()
    print("\n--------------------------------------------")
    print("Elija una de las siguientes opciones:")
    print("1) Mostrar recetas")
    print("2) Ver una receta")
    print("3) Buscar recetas por ingredientes")
    print("4) Agregar receta")
    print("5) Modificar receta")
    print("6) Borrar receta")
    print("0) SALIR")
    print("--------------------------------------------")
    opcion = int(input("\nOpcion elegida: "))

    try:
        if opcion == 1:
            lista_recetas(recetas)
        elif opcion == 2:
            mostrar_receta(recetas)
        elif opcion == 3:
            recetas_por_ingrediente(recetas)
        elif opcion == 4:
            agregar_receta(recetas)
        elif opcion == 5:
            modificar_receta(recetas)
        elif opcion == 6:
            borrar_receta(recetas)
        elif opcion == 0:
            return True
        else:
            print("Ingrese una opcion de las anteriores")
    except:
        print("Ingrese una opcion de las anteriores")

    print("\n")
    input("Presione cualquier tecla para volver al menu... ")
    return False


# Main
recetas = []
fin = False
while not fin:
    fin = mostrar_opciones()

print("El programa finalizó")
