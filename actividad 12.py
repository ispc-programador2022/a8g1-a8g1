import random
lista = []

def genrnd ():
    for x in range(50):
        aleatorio= random.random()
        lista.append(aleatorio)
    return (lista)

genrnd()
