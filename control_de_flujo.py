salida = "No"
while(salida in ["No"]):
    seleccion = input("Ingresa una opción: ")
    if seleccion == 'a':
        print("Elegiste la opcion a")
        print("Que es tambien una vocal")
    elif seleccion == 'b':
        print("Elegiste la opcion b")
    elif seleccion in ['a', 'e', 'i', 'o', 'u']:
        print("Elegiste una vocal")
    else:
        print("Elegiste otra opcion")
    salida = input("Desea salir?: ")