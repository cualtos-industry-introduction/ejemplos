tupla = 1, 2, 3, 4, 'Hola', 3.2
print(tupla[:])
#tupla[0] = 3
diccionario = {'nombre': 'Juan', 'apellido': 'Lopez'}
usuario = {'nombre': 'Pedro', 'apellido': 'Sanchez'}
lista = [diccionario, usuario]
#print(diccionario['nombre'])
#print(lista[1:2])
#for registro in lista:
#    print(registro)

usuario['correo'] = "abc@correo.com"

#for registro in lista:
    #registro['nombre'] = input("Ingresa el nuevo nombre")

#print(lista[:])

dato = {}
dato['nombre'] = input("Ingresa un nuevo nombre: ")
dato['direccion'] = input("ingresa la direccion: ")
dato['correo'] = input("ingresa el correo: ")

print(lista[0]['nombre'])
for llave, valor in usuario.items():
    print(llave, valor)