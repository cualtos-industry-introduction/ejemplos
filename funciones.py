lista = []
salida = "No"

def agregarContacto():
    nuevo_contacto = {}
    nuevo_contacto['nombre'] = input("Ingresa el nombre del contacto: ")
    nuevo_contacto['correo'] = input("Ingresa el correo del contacto: ")
    nuevo_contacto['direccion'] = input("Ingresa la direccion del contacto")
    lista.append(nuevo_contacto)

while(salida == "No"):
    entrada = input("Escribe la accion a efectuar: ")
    if entrada == "nuevo":
        agregarContacto()
        print("Contacto agregado")
    elif entrada == "mostrar":
        print(lista[:])
    elif entrada == "salir":
        exit()
    else:
        print("Opcion no válida")