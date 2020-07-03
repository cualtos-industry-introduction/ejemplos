class Contacto:
    correo = "abc@algo.com"
#    diccionario = {}

    def __init__(self, nombre):
        self.nombre = nombre
        self.diccionario = {}

    def mostrar_nombre(self):
        return self.nombre
    
nuevo_contacto = Contacto("Nuevo")
print(nuevo_contacto.mostrar_nombre)