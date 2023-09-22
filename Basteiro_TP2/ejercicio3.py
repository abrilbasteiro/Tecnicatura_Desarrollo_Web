# 3. Una vez codificadas en Python las Clases de los puntos anteriores, instancie los objetos tal como sucede en las siguientes instrucciones:
# sullivan = Monstruo(‘James P. Sullivan’, ‘leon’)
# mike = Monstruo(‘Mike Wazowski’, ‘ciclope’)
# boo = Humano(‘Boo’)

from ejercicio1 import Monstruo
from ejercicio2 import Humano

sullivan = Monstruo('James P. Sullivan', 'leon')
mike = Monstruo('Mike Wazowski', 'ciclope')
boo = Humano('Boo')

# # a. Describa el estado interno de los objetos asociados a las variables sullivan, mike y boo, detallando los valores de sus atributos de instancia.
# print('El nombre del primer monstruo es ' + sullivan.nombre + ', su especie es '+ sullivan.especie + ' y su energia es', sullivan.energia)
# print('El nombre del segundo monstruo es ' + mike.nombre + ', su especie es ' + mike.especie, 'y su energia es', mike.energia)
# print('El nombre del humano es ' + boo.nombre + ' y su estado de asustado es', boo.estadoAsustado)

# # b. ¿Cuál es el valor del atributo de clase especie asociado al objeto referenciado por el identificador boo?
# print('El valor del atributo de clase especie asociado al objeto referenciado por el identificador boo es', boo.especie)

# c. Si se instanciase un segundo objeto como el siguiente: sullivan2 = Monstruo(‘James P. Sullivan’, ‘leon’)
#   i. ¿Los identificadores sullivan y sullivan2 hacen referencia al mismo objeto? ¿o son objetos idénticos completamente distintos?
#   No, son dos objetos independientes.

#   ii. ¿Son objetos equivalentes? Explique que significa que dos objetos lo sean.
#   No, sullivan1 y sullivan2 no son objetos equivalentes porque no son el mismo objeto y no se le ha asignado el metodo __eq__ a la clase Monstruo para comparar sus valores.

#   iii. ¿Los objetos ligados a sullivan y sullivan2 comparten la misma posición de memoria?
#   No, ambos objetos son independientes y ocupan un lugar especifico de memoria.