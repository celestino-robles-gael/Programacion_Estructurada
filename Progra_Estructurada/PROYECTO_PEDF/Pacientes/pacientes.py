import funciones
from Pacientes import crud


def menuPrincipal():
    print("\033[92m")
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║                                                              ║")
    print("║                    G E S T I Ó N    D E                      ║")
    print("║                    P A C I E N T E S 👥                      ║")
    print("║                                                              ║")
    print("╠══════════════════════════════════════════════════════════════╣")
    print("║                                                              ║")
    print("║   [1]  ➕  Agregar paciente                                  ║")
    print("║   [2]  ➖  Borrar paciente                                   ║")
    print("║   [3]  🔁  Modificar paciente                                ║")
    print("║   [4]  📄  Mostrar pacientes                                 ║")
    print("║   [5]  🔎  Buscar paciente                                   ║")
    print("║   [6]  ⚠️  Limpiar pacientes                                  ║")
    print("║   [7]  ↩️   Regresar al menú principal                        ║")
    print("║                                                              ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print("\033[0m")

    opcion = input("\033[93mSelecciona una opción: \033[0m").strip()

    return opcion


def agregarPacientes(conexionBD):
    resp = "si"

    while resp == "si":
        print("\033[92m")
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║                                                              ║")
        print("║                    ➕  AGREGAR PACIENTE                      ║")
        print("║                                                              ║")
        print("╚══════════════════════════════════════════════════════════════╝")
        print("\033[0m")

        print("📋 Ingresa la siguiente información:\n")

        nombre = input("👤 Nombre      : ").upper().strip()

        while not funciones.validarNombre(nombre):
            print("\033[91m⚠ Nombre inválido. Solo se permiten letras y espacios.\033[0m")
            nombre = input("👤 Nombre      : ").upper().strip()


        edad = input("🔢 Edad        : ").strip()

        while not funciones.validarEdad(edad):
            print("\033[91m⚠ Edad inválida. Solo se permiten números.\033[0m")
            edad = input("🔢 Edad        : ").strip()


        sexo = input("🚻 Sexo        : ").upper().strip()

        while not funciones.validarSexo(sexo):
            print("\033[91m⚠ Sexo inválido. Escribe MASCULINO o FEMENINO.\033[0m")
            sexo = input("🚻 Sexo        : ").upper().strip()


        direccion = input("🏠 Dirección   : ").upper().strip()


        telefono = input("📞 Teléfono    : ").strip()

        while not funciones.validarTelefono(telefono):
            print("\033[91m⚠ Teléfono inválido. Debe contener 10 números.\033[0m")
            telefono = input("📞 Teléfono    : ").strip()

        respuesta = crud.insertar(
            nombre,
            edad,
            sexo,
            direccion,
            telefono,
            conexionBD
        )

        if respuesta:
            funciones.accionExitosa()
        else:
            funciones.accionNoExitosa()

        resp = ""

        while resp != "si" and resp != "no":
            resp = input(
                "\n¿Deseas registrar otro paciente? (Si/No): "
            ).lower().strip()

        funciones.borrarPantalla()


def mostrarPacientes(conexionBD):
    print("\033[94m")
    print("╔═════════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("║                                                                                                     ║")
    print("║                                        📋  MOSTRAR PACIENTES                                        ║")
    print("║                                                                                                     ║")
    print("╚═════════════════════════════════════════════════════════════════════════════════════════════════════╝")
    print("\033[0m")

    pacientes = crud.consultar(conexionBD)

    if len(pacientes) > 0:

        print(
            f"\n"
            f"{'ID':<5}"
            f"{'NOMBRE':<25}"
            f"{'EDAD':<8}"
            f"{'SEXO':<15}"
            f"{'DIRECCIÓN':<35}"
            f"{'TELÉFONO':<15}"
        )

        print("─" * 103)

        contadorPacientes = 0

        for i in pacientes:
            print(
                f"{i[0]:<5}"
                f"{i[1][:25]:<25}"
                f"{i[2]:<8}"
                f"{i[3][:15]:<15}"
                f"{i[4][:35]:<35}"
                f"{i[5]:<15}"
            )

            contadorPacientes += 1

        print("─" * 103)

        print(
            f"\n\033[92m"
            f"Total de pacientes registrados: {contadorPacientes}"
            f"\033[0m"
        )

    else:
        print(
            "\n\033[93m"
            "⚠ No existen pacientes registrados."
            "\033[0m\n"
        )

    funciones.esperarTecla()


def limpiarPacientes(conexionBD):
    print("\033[91m")
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║                                                              ║")
    print("║                    ⚠️  LIMPIAR PACIENTES                      ║")
    print("║                                                              ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print("\033[0m")

    print("\033[91m⚠ Esta acción eliminará TODOS los pacientes registrados.")
    print("⚠ Esta operación no se puede deshacer.\033[0m\n")

    opc = ""

    while opc != "si" and opc != "no":
        opc = input(
            "¿Estás seguro que deseas borrar TODOS los pacientes? (Si/No): "
        ).lower().strip()

    if opc == "si":
        respuesta = crud.vaciar(conexionBD)

        if respuesta:
            funciones.accionExitosa()
        else:
            funciones.accionNoExitosa()

    else:
        print("\n\033[93mOperación cancelada.\033[0m")

    funciones.esperarTecla()


def buscarPacientes(conexionBD):

    resp = "si"

    while resp == "si":

        opcion = ""

        while opcion not in ["1", "2", "3", "4", "5", "6"]:

            funciones.borrarPantalla()

            print("\033[94m")
            print("╔══════════════════════════════════════════════════════════════╗")
            print("║                                                              ║")
            print("║                      🔎  BUSCAR PACIENTE                     ║")
            print("║                                                              ║")
            print("╚══════════════════════════════════════════════════════════════╝")
            print("\033[0m")

            print("¿Cómo deseas realizar la búsqueda?\n")
            print("\t[1] Buscar por ID")
            print("\t[2] Buscar por nombre")
            print("\t[3] Buscar por edad")
            print("\t[4] Buscar por sexo")
            print("\t[5] Buscar por dirección")
            print("\t[6] Buscar por teléfono")

            opcion = input(
                "\n\033[93mSelecciona una opción: \033[0m"
            ).strip()

            if opcion not in ["1", "2", "3", "4", "5", "6"]:
                funciones.opcionInvalida()
                funciones.esperarTecla()

        dato = ""

        match opcion:
            case "1":
                dato = input("\nEscribe el ID del paciente: ").strip()

            case "2":
                dato = input(
                    "\nEscribe el nombre del paciente: "
                ).upper().strip()

            case "3":
                dato = input("\nEscribe la edad del paciente: ").strip()

            case "4":
                dato = input(
                    "\nEscribe el sexo del paciente: "
                ).upper().strip()

            case "5":
                dato = input(
                    "\nEscribe la dirección del paciente: "
                ).upper().strip()

            case "6":
                dato = input(
                    "\nEscribe el teléfono del paciente: "
                ).strip()

        funciones.borrarPantalla()

        print("\033[94m")
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║                                                              ║")
        print("║                      🔎  BUSCAR PACIENTE                     ║")
        print("║                                                              ║")
        print("╚══════════════════════════════════════════════════════════════╝")
        print("\033[0m")

        pacientes = crud.buscar(conexionBD, opcion, dato)

        if len(pacientes) > 0:

            print(
                f"\n{'ID':<5}"
                f"{'NOMBRE':<25}"
                f"{'EDAD':<8}"
                f"{'SEXO':<15}"
                f"{'DIRECCIÓN':<35}"
                f"{'TELÉFONO':<15}"
            )

            print("─" * 103)

            for i in pacientes:
                print(
                    f"{i[0]:<5}"
                    f"{i[1][:25]:<25}"
                    f"{i[2]:<8}"
                    f"{i[3][:15]:<15}"
                    f"{i[4][:35]:<35}"
                    f"{i[5]:<15}"
                )

            print("─" * 103)

        else:
            print("\n⚠ No se encontró ningún paciente con ese dato.\n")

        opc = ""

        while opc not in ["si", "no"]:
            opc = input(
                "\n¿Deseas buscar otro paciente? (Si/No): "
            ).lower().strip()

        resp = opc

    funciones.esperarTecla()


def borrarPacientes(conexionBD):

    funciones.borrarPantalla()

    print("\033[91m")
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║                                                              ║")
    print("║                     ➖  BORRAR PACIENTE                      ║")
    print("║                                                              ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print("\033[0m")

    nombreBuscar = input(
        "Escribe el nombre del paciente a borrar: "
    ).upper().strip()

    pacientes = crud.buscar(
        conexionBD,
        "2",
        nombreBuscar
    )

    if len(pacientes) > 0:

        print(
            f"\n{'ID':<5}"
            f"{'NOMBRE':<25}"
            f"{'EDAD':<8}"
            f"{'SEXO':<15}"
            f"{'DIRECCIÓN':<35}"
            f"{'TELÉFONO':<15}"
        )

        print("─" * 103)

        for i in pacientes:
            print(
                f"{i[0]:<5}"
                f"{i[1][:25]:<25}"
                f"{i[2]:<8}"
                f"{i[3][:15]:<15}"
                f"{i[4][:35]:<35}"
                f"{i[5]:<15}"
            )

        print("─" * 103)

        idsPacientes = []

        for i in pacientes:
            idsPacientes.append(str(i[0]))

        idPaciente = ""

        while idPaciente not in idsPacientes:

            idPaciente = input(
                "\nEscribe el ID del paciente que deseas borrar: "
            ).strip()

            if idPaciente not in idsPacientes:
                funciones.opcionInvalida()

        opc = ""

        while opc not in ["si", "no"]:
            opc = input(
                "\n¿Estás seguro de borrar este paciente? (Si/No): "
            ).lower().strip()

        if opc == "si":

            respuesta = crud.borrar(
                conexionBD,
                "1",
                idPaciente
            )

            if respuesta:
                funciones.accionExitosa()
            else:
                funciones.accionNoExitosa()

        else:
            print("\nOperación cancelada.")

    else:
        print(
            "\n⚠ No existe ningún paciente con ese nombre.\n"
        )

    funciones.esperarTecla()


def modificarPacientes(conexionBD):

    funciones.borrarPantalla()

    print("\033[93m")
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║                                                              ║")
    print("║                   🔁  MODIFICAR PACIENTE                     ║")
    print("║                                                              ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print("\033[0m")

    nombreBuscar = input(
        "Escribe el nombre del paciente a modificar: "
    ).upper().strip()

    # La opción 2 corresponde a buscar por nombre
    pacientes = crud.buscar(
        conexionBD,
        "2",
        nombreBuscar
    )

    if len(pacientes) > 0:

        print(
            f"\n{'ID':<5}"
            f"{'NOMBRE':<25}"
            f"{'EDAD':<8}"
            f"{'SEXO':<15}"
            f"{'DIRECCIÓN':<35}"
            f"{'TELÉFONO':<15}"
        )

        print("─" * 103)

        for i in pacientes:
            print(
                f"{i[0]:<5}"
                f"{i[1][:25]:<25}"
                f"{i[2]:<8}"
                f"{i[3][:15]:<15}"
                f"{i[4][:35]:<35}"
                f"{i[5]:<15}"
            )

        print("─" * 103)

        # Guardamos los IDs que realmente aparecieron
        idsPacientes = []

        for i in pacientes:
            idsPacientes.append(str(i[0]))

        idPaciente = ""

        while idPaciente not in idsPacientes:

            idPaciente = input(
                "\nEscribe el ID del paciente que deseas modificar: "
            ).strip()

            if idPaciente not in idsPacientes:
                funciones.opcionInvalida()

        opc = ""

        while opc not in ["si", "no"]:
            opc = input(
                "\n¿Estás seguro de modificar este paciente? (Si/No): "
            ).lower().strip()

        if opc == "si":

            print("\nIngresa los nuevos datos del paciente:\n")

            nombre = input(
                "👤 Nuevo nombre      : "
            ).upper().strip()

            edad = input(
                "🔢 Nueva edad        : "
            ).strip()

            sexo = input(
                "🚻 Nuevo sexo        : "
            ).upper().strip()

            direccion = input(
                "🏠 Nueva dirección   : "
            ).upper().strip()

            telefono = input(
                "📞 Nuevo teléfono    : "
            ).strip()

            respuesta = crud.modificar(
                conexionBD,
                "1",
                idPaciente,
                nombre,
                edad,
                sexo,
                direccion,
                telefono
            )

            if respuesta:
                funciones.accionExitosa()
            else:
                funciones.accionNoExitosa()

        else:
            print("\nOperación cancelada.")

    else:
        print(
            "\n⚠ No existe ningún paciente con ese nombre.\n"
        )

    funciones.esperarTecla()