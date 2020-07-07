def obtenerIndice(lista, nombre):
    posicion = 0
    for elemento in lista:
        if elemento.nombre == nombre:
            return posicion
        else:
            posicion += 1
    return -1
