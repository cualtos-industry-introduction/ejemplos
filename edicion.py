from busqueda import obtenerIndice

def editarContacto(lista, nombre):
    indice = obtenerIndice(lista, nombre)
    lista[indice].nombre = input("Ingresa nuevo nombre: ")
    lista[indice].correo = input("Ingresa nuevo correo: ")
    lista[indice].empresa = input("Ingresa nueva empresa: ")
