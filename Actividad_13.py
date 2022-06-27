# Actividad 13
# Función que devuelva la suma de las combinaciones posibles de los números generados
# por la función genrnd tomados de a dos.

import random
lista = []

def genrnd ():
    """
    Funcion que, importando el modulo random, nos da como resultado una lista
    de 50 valores aleatores de una distribución normal. Cada valor aleatorio
    generado se añadido a una lista. 
    """
    for x in range(50):
        aleatorio = random.random()
        lista.append(aleatorio)
    return (lista)

genrnd()


def sum_2_genrnd(nr):
    """
    Devuelve la suma de cada uno de los pares de valores de la lista 
    anterior generada de forma aleatoria. Cada una de las sumas se 
    añaden a una lista.
    """
    lista_suma = []
    for i in nr:
        for j in nr:
            suma = i + j
            lista_suma.append(suma)
    return lista_suma

y = sum_2_genrnd(lista)  #Se almacena la lista que puede ser usada luego. 
print(y) # Para ver la lista
