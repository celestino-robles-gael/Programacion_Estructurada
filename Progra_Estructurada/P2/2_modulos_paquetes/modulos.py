# Un módulo es simplemente un archivo con extensión .py que contiene código de Python (funciones, clases, variables, etc.).
# borrar pantalla 
def borrarPantalla():
    print("\033c")
#1.- Funcion que no recibe parametros y no regresa valor
def funcion1():
    borrarPantalla()
    nombre = input("Escribe el Nombre: ").strip().upper()
    apellido = input("Escribe el Apellido: ").strip().upper()
    print(f"EL nombre completo del alumno es: {nombre} {apellido}")

#3.- Funcion que recibe parametros y no regresa valor 
def funcion3(nombre,apellido):
    borrarPantalla()
    print(f"EL nombre completo del alumno es: {nombre} {apellido}")

#2.- Funcion que no recibe parametros y regresa valor
def funcion2():
    borrarPantalla()
    nombre = input("Escribe el Nombre: ").strip().upper()
    apellido = input("Escribe el Apellido: ").strip().upper()
    return nombre,apellido

#4.- Funcion que recibe parametros y regresa valor
def funcion4(nombre,apellido):
    borrarPantalla()
    return nombre,apellido

nom,ape=funcion4("Raul","flores")
print(f"EL nombre completo del alumno es: {nom} {ape}")
#Invocar las funciones

