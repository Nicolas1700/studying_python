import sys


def convertir_str_a_int(cadena=str):
    try:
        return int(cadena)
    except ValueError:
        return None


if len(sys.argv) == 3:
    if (
        convertir_str_a_int(sys.argv[1]) == None
        or convertir_str_a_int(sys.argv[2]) == None
    ):
        sys.exit()
    filas = int(sys.argv[1])
    columnas = int(sys.argv[2])
    print(f"Cantidad de filas {filas} y cantidad de columnas {columnas}")

    for fil in range(filas):
        for col in range(columnas):
            print(" * ", end="")
        print("")
else:
    print(
        """
    Necesitamos 2 argumentos, donde:
    1. Será el número de filas
    2. Será el número de columnas
            """
    )
