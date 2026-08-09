import funciones
from Doctores import crud


def menuPrincipal():
    print("\033[94m")
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║                                                              ║")
    print("║                    G E S T I Ó N    D E                      ║")
    print("║                    💉   D O C T O R E S                      ║")
    print("║                                                              ║")
    print("╠══════════════════════════════════════════════════════════════╣")
    print("║                                                              ║")
    print("║   [1]  ➕  Agregar doctor                                    ║")
    print("║   [2]  ➖  Borrar doctor                                     ║")
    print("║   [3]  🔁  Modificar doctor                                  ║")
    print("║   [4]  📃  Mostrar doctores                                  ║")
    print("║   [5]  🔍  Buscar doctor                                     ║")
    print("║   [6]  ⚠️  Limpiar doctores                                   ║")
    print("║   [7]  ↩️   Regresar al menú principal                        ║")
    print("║                                                              ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print("\033[0m")

    opcion = input("\033[93mSelecciona una opción: \033[0m").strip()

    return opcion


def agregarDoctores(conexionBD):
    resp = "si"

    while resp == "si":
        funciones.borrarPantalla()

        print("\033[92m")
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║                                                              ║")
        print("║                    ➕  AGREGAR DOCTOR                        ║")
        print("║                                                              ║")
        print("╚══════════════════════════════════════════════════════════════╝")
        print("\033[0m")

        print("📋 Ingresa la siguiente información:\n")

        nombre = input(
            "👤 Nombre         : "
        ).upper().strip()

        while not funciones.validarNombre(nombre):
            print(
                "\033[91m"
                "⚠ Nombre inválido. Solo se permiten letras y espacios."
                "\033[0m"
            )

            nombre = input(
                "👤 Nombre         : "
            ).upper().strip()


        especialidad = input(
            "✝️   Especialidad  : "
        ).upper().strip()

        while not funciones.validarNombre(especialidad):
            print(
                "\033[91m"
                "⚠ Especialidad inválida. "
                "Solo se permiten letras y espacios."
                "\033[0m"
            )

            especialidad = input(
                "✝️   Especialidad  : "
            ).upper().strip()


        telefono = input(
            "☎  Teléfono       : "
        ).strip()

        while not funciones.validarTelefono(telefono):
            print(
                "\033[91m"
                "⚠ Teléfono inválido. Debe contener 10 números."
                "\033[0m"
            )

            telefono = input(
                "☎  Teléfono       : "
            ).strip()


        consultorio = input(
            "▣ Consultorio     : "
        ).upper().strip()


        respuesta = crud.insertar(
            nombre,
            especialidad,
            telefono,
            consultorio,
            conexionBD
        )

        if respuesta:
            funciones.accionExitosa()
        else:
            funciones.accionNoExitosa()

        resp = ""

        while resp != "si" and resp != "no":
            resp = input(
                "\n¿Deseas registrar otro doctor? (Si/No): "
            ).lower().strip()

    funciones.esperarTecla()

def mostrarDoctores(conexionBD):
    funciones.borrarPantalla()

    print("\033[94m")
    print("╔══════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("║                                                                                              ║")
    print("║                                  📃  MOSTRAR DOCTORES                                        ║")
    print("║                                                                                              ║")
    print("╚══════════════════════════════════════════════════════════════════════════════════════════════╝")
    print("\033[0m")

    doctores = crud.consultar(conexionBD)

    if len(doctores) > 0:

        print(
            f"\n{'ID':<5}"
            f"{'NOMBRE':<28}"
            f"{'ESPECIALIDAD':<25}"
            f"{'TELÉFONO':<16}"
            f"{'CONSULTORIO':<15}"
        )

        print("─" * 89)

        contadorDoctores = 0

        for i in doctores:
            print(
                f"{i[0]:<5}"
                f"{i[1][:28]:<28}"
                f"{i[2][:25]:<25}"
                f"{i[3]:<16}"
                f"{i[4][:15]:<15}"
            )

            contadorDoctores += 1

        print("─" * 89)

        print(
            f"\nTotal de doctores registrados: {contadorDoctores}"
        )

    else:
        print("\n⚠ No existen doctores registrados.\n")

    funciones.esperarTecla()


def buscarDoctores(conexionBD):
    resp = "si"

    while resp == "si":

        opcion = ""

        while opcion not in ["1", "2", "3", "4", "5"]:

            funciones.borrarPantalla()

            print("\033[94m")
            print("╔══════════════════════════════════════════════════════════════╗")
            print("║                                                              ║")
            print("║                      🔍  BUSCAR DOCTOR                       ║")
            print("║                                                              ║")
            print("╚══════════════════════════════════════════════════════════════╝")
            print("\033[0m")

            print("¿Cómo deseas realizar la búsqueda?\n")
            print("\t[1] Buscar por ID")
            print("\t[2] Buscar por nombre")
            print("\t[3] Buscar por especialidad")
            print("\t[4] Buscar por teléfono")
            print("\t[5] Buscar por consultorio")

            opcion = input(
                "\n\033[93mSelecciona una opción: \033[0m"
            ).strip()

            if opcion not in ["1", "2", "3", "4", "5"]:
                funciones.opcionInvalida()
                funciones.esperarTecla()

        dato = ""

        match opcion:
            case "1":
                dato = input("\nEscribe el ID del doctor: ").strip()

            case "2":
                dato = input(
                    "\nEscribe el nombre del doctor: "
                ).upper().strip()

            case "3":
                dato = input(
                    "\nEscribe la especialidad del doctor: "
                ).upper().strip()

            case "4":
                dato = input(
                    "\nEscribe el teléfono del doctor: "
                ).strip()

            case "5":
                dato = input(
                    "\nEscribe el consultorio del doctor: "
                ).upper().strip()

        funciones.borrarPantalla()

        print("\033[94m")
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║                                                              ║")
        print("║                      🔍  BUSCAR DOCTOR                       ║")
        print("║                                                              ║")
        print("╚══════════════════════════════════════════════════════════════╝")
        print("\033[0m")

        doctores = crud.buscar(conexionBD, opcion, dato)

        if len(doctores) > 0:

            print(
                f"\n{'ID':<5}"
                f"{'NOMBRE':<28}"
                f"{'ESPECIALIDAD':<25}"
                f"{'TELÉFONO':<16}"
                f"{'CONSULTORIO':<15}"
            )

            print("─" * 89)

            for i in doctores:
                print(
                    f"{i[0]:<5}"
                    f"{i[1][:28]:<28}"
                    f"{i[2][:25]:<25}"
                    f"{i[3]:<16}"
                    f"{i[4][:15]:<15}"
                )

            print("─" * 89)

        else:
            print("\n⚠ No se encontró ningún doctor con ese dato.\n")

        opc = ""

        while opc not in ["si", "no"]:
            opc = input(
                "\n¿Deseas buscar otro doctor? (Si/No): "
            ).lower().strip()

        resp = opc

    funciones.esperarTecla()


def borrarDoctores(conexionBD):

    funciones.borrarPantalla()

    print("\033[91m")
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║                                                              ║")
    print("║                      ➖  BORRAR DOCTOR                       ║")
    print("║                                                              ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print("\033[0m")

    nombreBuscar = input(
        "Escribe el nombre del doctor a borrar: "
    ).upper().strip()

    doctores = crud.buscar(
        conexionBD,
        "2",
        nombreBuscar
    )

    if len(doctores) > 0:

        print(
            f"\n{'ID':<5}"
            f"{'NOMBRE':<28}"
            f"{'ESPECIALIDAD':<25}"
            f"{'TELÉFONO':<16}"
            f"{'CONSULTORIO':<15}"
        )

        print("─" * 89)

        for i in doctores:
            print(
                f"{i[0]:<5}"
                f"{i[1][:28]:<28}"
                f"{i[2][:25]:<25}"
                f"{i[3]:<16}"
                f"{i[4][:15]:<15}"
            )

        print("─" * 89)

        idsDoctores = []

        for i in doctores:
            idsDoctores.append(str(i[0]))

        idDoctor = ""

        while idDoctor not in idsDoctores:

            idDoctor = input(
                "\nEscribe el ID del doctor que deseas borrar: "
            ).strip()

            if idDoctor not in idsDoctores:
                funciones.opcionInvalida()

        opc = ""

        while opc not in ["si", "no"]:
            opc = input(
                "\n¿Estás seguro de borrar este doctor? (Si/No): "
            ).lower().strip()

        if opc == "si":

            respuesta = crud.borrar(
                conexionBD,
                "1",
                idDoctor
            )

            if respuesta:
                funciones.accionExitosa()
            else:
                funciones.accionNoExitosa()

        else:
            print("\nOperación cancelada.")

    else:
        print(
            "\n⚠ No existe ningún doctor con ese nombre.\n"
        )

    funciones.esperarTecla()


def modificarDoctores(conexionBD):

    funciones.borrarPantalla()

    print("\033[93m")
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║                                                              ║")
    print("║                    🔁  MODIFICAR DOCTOR                      ║")
    print("║                                                              ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print("\033[0m")

    nombreBuscar = input(
        "Escribe el nombre del doctor a modificar: "
    ).upper().strip()

    while not funciones.validarNombre(nombreBuscar):
        print(
            "\033[91m"
            "⚠ Nombre inválido. Solo se permiten letras y espacios."
            "\033[0m"
        )

        nombreBuscar = input(
            "Escribe el nombre del doctor a modificar: "
        ).upper().strip()

    doctores = crud.buscar(
        conexionBD,
        "2",
        nombreBuscar
    )

    if len(doctores) > 0:

        print(
            f"\n{'ID':<5}"
            f"{'NOMBRE':<28}"
            f"{'ESPECIALIDAD':<25}"
            f"{'TELÉFONO':<16}"
            f"{'CONSULTORIO':<15}"
        )

        print("─" * 89)

        for i in doctores:
            print(
                f"{i[0]:<5}"
                f"{i[1][:28]:<28}"
                f"{i[2][:25]:<25}"
                f"{i[3]:<16}"
                f"{i[4][:15]:<15}"
            )

        print("─" * 89)

        idsDoctores = []

        for i in doctores:
            idsDoctores.append(str(i[0]))

        idDoctor = ""

        while idDoctor not in idsDoctores:

            idDoctor = input(
                "\nEscribe el ID del doctor que deseas modificar: "
            ).strip()

            if idDoctor not in idsDoctores:
                funciones.opcionInvalida()

        opc = ""

        while opc not in ["si", "no"]:
            opc = input(
                "\n¿Estás seguro de modificar este doctor? (Si/No): "
            ).lower().strip()

        if opc == "si":

            print("\nIngresa los nuevos datos del doctor:\n")

            nombre = input(
                "👤 Nuevo nombre         : "
            ).upper().strip()

            while not funciones.validarNombre(nombre):
                print(
                    "\033[91m"
                    "⚠ Nombre inválido. Solo se permiten letras y espacios."
                    "\033[0m"
                )

                nombre = input(
                    "👤 Nuevo nombre         : "
                ).upper().strip()

            especialidad = input(
                "✚ Nueva especialidad   : "
            ).upper().strip()

            while not funciones.validarNombre(especialidad):
                print(
                    "\033[91m"
                    "⚠ Especialidad inválida. "
                    "Solo se permiten letras y espacios."
                    "\033[0m"
                )

                especialidad = input(
                    "✚ Nueva especialidad   : "
                ).upper().strip()

            telefono = input(
                "☎  Nuevo teléfono       : "
            ).strip()

            while not funciones.validarTelefono(telefono):
                print(
                    "\033[91m"
                    "⚠ Teléfono inválido. Debe contener 10 números."
                    "\033[0m"
                )

                telefono = input(
                    "☎  Nuevo teléfono       : "
                ).strip()

            consultorio = input(
                "▣ Nuevo consultorio    : "
            ).upper().strip()

            respuesta = crud.modificar(
                conexionBD,
                "1",
                idDoctor,
                nombre,
                especialidad,
                telefono,
                consultorio
            )

            if respuesta:
                funciones.accionExitosa()
            else:
                funciones.accionNoExitosa()

        else:
            print("\nOperación cancelada.")

    else:
        print(
            "\n⚠ No existe ningún doctor con ese nombre.\n"
        )

    funciones.esperarTecla()

def limpiarDoctores(conexionBD):
    funciones.borrarPantalla()

    print("\033[91m")
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║                                                              ║")
    print("║                     ⚠️  LIMPIAR DOCTORES                      ║")
    print("║                                                              ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print("\033[0m")

    print("\033[91m⚠ Esta acción eliminará TODOS los doctores registrados.")
    print("⚠ Esta operación no se puede deshacer.\033[0m\n")

    opc = ""

    while opc not in ["si", "no"]:
        opc = input(
            "¿Estás seguro que deseas borrar TODOS los doctores? (Si/No): "
        ).lower().strip()

    if opc == "si":

        respuesta = crud.vaciar(conexionBD)

        if respuesta:
            funciones.accionExitosa()
        else:
            funciones.accionNoExitosa()

    else:
        print("\nOperación cancelada.")

    funciones.esperarTecla()