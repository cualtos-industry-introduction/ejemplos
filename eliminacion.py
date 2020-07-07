from busqueda import obtenerIndice

def eliminarElemento(lista, nombre):
    indice = obtenerIndice(lista, nombre)
    del lista[indice]
