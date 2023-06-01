# Programe una aplicación de consola que solicite al usuario su nombre, después su apellido y a continuación su año de nacimiento. Con esos datos deberá generar una sugerencia de usuario y contraseña. Por ejemplo: nombre: Martín, apellido: Francisconi, Año nacimiento: 1985 -> Usuario: mfrancisconi, Contraseña: mf.1985

nombre = (input('Ingrese su nombre: '))
apellido = (input('Ingrese su apellido: '))
año_de_nacimiento = input('Ingrese su año de nacimiento: ')

usuario_sugerido = (nombre[:1] + apellido).lower()
contraseña_sugerida = (nombre[:1] + apellido [:1]).lower() + '.' + año_de_nacimiento

print('Las credenciales sugeridas son: \n Usuario:', usuario_sugerido, '\n Contraseña:', contraseña_sugerida)