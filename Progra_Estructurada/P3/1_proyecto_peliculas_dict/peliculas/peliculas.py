import funciones

def menuPrincipal():
    print("\n\t\t\t...::: M E N U   P R I N C I P A L :::... \n")
    opcion=input("\n\t 1.- Agregar \n\t 2.- Borrar \n\t 3.- Modificar \n\t 4.- Mostrar \n\t 5.- Buscar \n\t 6.- Limpiar \n\t 7.- Salir \n \t\tElige una Opcion: ").strip()
    return opcion

def agregarPeliculas(pelis):
    print("\n\t\t\t...::: AGREGAR CARACTERIZTICA PELICULAS :::... \n")
    caracteristica=input("Escribir el nombre de la caracteriztica: ").lower().strip()
    valor=input("Ingresa el valor de la caracteristica: ").upper().strip()
    pelis[caracteristica]=valor
    funciones.accionExitosa()
    
def mostrarPeliculas(pelis):
    print("\n\t\t\t...::: MOSTRAR CARACTERISTICAS DE LA PELICULAS :::... \n")
    if len(pelis)>0:
        for i in pelis:
            print(f"{i} = {pelis[i]}")
    else:
        print("... ¡No hay peliculas que Mostrar, verifique! ... ")
    funciones.esperarTecla()
    
def limpiarPeliculas(pelis):
    print("\n\t\t\t...::: BORRAR TODAS LAS CARACTERISTICAS DE LAS PELICULAS :::... \n")
    opc=""
    while opc!="si" and opc!="no":
        opc=input("¿Estas seguro que deseas borrar TODAS las caracteristicas (Si/No)? ").lower().strip()
    if opc=="si":
        pelis.clear()
        funciones.accionExitosa()

def buscarPeliculas(pelis):
    print("\n\t\t\t...::: BUSCAR UNA CARACTERISTICA PELICULAS :::... \n")
    peli=input("Escribe la caracteristica de la pelicula a buscar: ").lower().strip()
    noencontre=True
    for i in pelis:
        if i == peli:
            print(f"La caracteristica es: {peli} y su valor es {pelis[peli]}")
            funciones.esperarTecla()
            noencontre=False
    if noencontre:
        input("n\t\... ¡No existe la caracteristica de la pelicula a buscar, verifique! ...")

def borrarPeliculas(pelis):
    print("\n\t\t\t...::: BORRAR CARACTERISTICA DE LA PELICULAS :::... \n")
    peli=input("Escribe la caracteristica de la pelicula: ").upper().strip()
    noencontre=True
    for i in pelis:
        if i == peli:
            noencontre=False
            opc=""
            while opc!="si" and opc!="no":
                opc=input("¿Estas seguro que deseas borrar la caracteristica?").lower().strip()
            if opc=="si":
                caracteristica=peli
            
    if noencontre:
        input("\n\t... ¡No existe la caracteristica de la pelicula a eliminar, verifique! ...")
    else:
        pelis.pop(caracteristica)
        funciones.accionExitosa()
        
def modificarPeliculas(pelis):
    print("\n\t\t\t...::: MODIFICAR EL VALOR CARACTERISTICA DE LA PELICULAS :::... \n")
    peli=input("Escribe la caracteristica de la pelicula: ").upper().strip()
    noencontre=True
    for i in pelis:
        if i == peli:
            noencontre=False
            print(f"La caracteristica es: {peli} y su valor es {pelis[peli]}")
            opc=""
            while opc!="si" and opc!="no":
                opc=input("¿Estas seguro que deseas modificar la caracteristica?").lower().strip()
            if opc=="si":
                pelis[peli]=input("Escribe el nuevo valor de esta caracteriztica: ").upper().strip()
                funciones.accionExitosa()
    if noencontre:
        input("n\t\... ¡No existe la caracteristica de la pelicula a modificar, verifique! ...")