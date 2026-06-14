# Un módulo es simplemente un archivo con extensión .py que contiene código de Python (funciones, clases, variables, etc.).

def borrarPantalla():
    print("\033c")

def funcion2():
    borrarPantalla()
    nombre = input("Escribe el Nombre: ").strip().upper()
    apellido = input("Escribe el Apellido: ").strip().upper()
    return nombre,apellido