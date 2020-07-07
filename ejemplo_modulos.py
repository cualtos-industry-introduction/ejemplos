from contacto import Contacto
from busqueda import obtenerIndice
from edicion import editarContacto
from mostrar_contactos import mostrar_contactos
from eliminacion import eliminarElemento

juan = Contacto("Juan")
lucy = Contacto("Lucy")
contactos = [juan, lucy]

print("Antes de la edicion: ")
mostrar_contactos(contactos)
editarContacto(contactos, "lucy")
print("Despues de la edicion: ")
mostrar_contactos(contactos)
print("Antes del borrado: ")
mostrar_contactos(contactos)
eliminarElemento(contactos, "Juan")
print("Despues del borrado: ")
mostrar_contactos(contactos)
