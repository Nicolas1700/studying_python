# Completa el ejercicio aquí
texto = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

texto_separado = texto.split("#")

texto_final = texto_separado[0].capitalize() + "..."
for texto in texto_separado[1:]:
    texto_final = texto_final + "\n- " + texto.capitalize() + "."

# print(texto_final)

# 2) Crea una función modificar() que a partir de una lista de números realice las siguientes tareas sin modificar la original:

# Borrar los elementos duplicados
# Ordenar la lista de mayor a menor
# Eliminar todos los números impares
# Realizar una suma de todos los números que quedan
# Añadir como primer elemento de la lista la suma realizada
# Devolver la lista modificada
# Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, concuerda con el primer número de la lista, tal que así:
# nueva_lista = modificar(lista)
# print( nueva_lista[0] == sum(nueva_lista[1:]) )
# > True
# Nota: La función sum(lista) devuelve una suma de los elementos de una lista

lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]


def modificar(lista):
    lista_modificada = list(set(lista))
    lista_modificada.sort(reverse=True)
    for v, _ in enumerate(lista_modificada):
        if v % 2 != 0:
            del lista_modificada[v]
    return lista_modificada


print("Lista resultado: ", modificar(lista))
