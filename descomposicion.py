"""  3) [Avanzado] Crea un script llamado descomposicion.py que realice las siguientes tareas:

Debe tomar 1 argumento que será un número entero positivo.
En caso de no recibir un argumento, debe mostrar información acerca de cómo utilizar el script.
** El objetivo del script es descomponer el número en unidades, decenas, centenas, miles... tal que por ejemplo si se introduce el número:**

> 3647
** El programa deberá devolver una descomposición línea a línea como la siguiente utilizando las técnicas de formateo: **

> 0007
  0040
  0600
  3000
Pista: Que el valor sea un número no significa necesariamente que deba serlo para formatearlo. Necesitarás jugar muy bien con los índices y realizar muchas conversiones entre tipos cadenas, números y viceversa 
"""

import sys


def notificacion_valor():
    return print("Necesitamos 1 argumento entero positivo mayor a 0")


if len(sys.argv) == 2:
    num = int(sys.argv[1])
    if num <= 0:
        notificacion_valor()
        sys.exit()

    num_str = sys.argv[1]
    longitud = len(num_str)
    cad = f"{0:0{longitud}d}"
    for position in range(
        longitud - 1, -1, -1
    ):  # Recorrer desde el último hasta el primero
        new_cad = cad[:position] + num_str[position] + cad[position + 1 :]
        print(new_cad)


else:
    notificacion_valor()


