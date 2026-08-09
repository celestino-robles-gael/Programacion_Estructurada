import os
import funciones
from Citas import crud

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


def menuPrincipal():
    print("\033[95m")
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║                                                              ║")
    print("║                    G E S T I Ó N   D E                       ║")
    print("║                    C  I  T  A  S    📄                       ║")
    print("║                                                              ║")
    print("╠══════════════════════════════════════════════════════════════╣")
    print("║                                                              ║")
    print("║   [1]  ➕  Agregar cita                                      ║")
    print("║   [2]  ➖  Borrar cita                                       ║")
    print("║   [3]  🔁  Modificar cita                                    ║")
    print("║   [4]  📋  Mostrar citas                                     ║")
    print("║   [5]  🔎  Buscar cita                                       ║")
    print("║   [6]  ⚠️  Limpiar citas                                      ║")
    print("║   [7]  📄  Generar comprobante PDF                           ║")
    print("║   [8]  ↩️   Regresar al menú principal                        ║")
    print("║                                                              ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print("\033[0m")

    opcion = input(
        "\033[93mSelecciona una opción: \033[0m"
    ).strip()

    return opcion


def agregarCitas(conexionBD):
    resp = "si"

    while resp == "si":
        funciones.borrarPantalla()

        print("\033[95m")
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║                                                              ║")
        print("║                       ➕  AGREGAR CITA                       ║")
        print("║                                                              ║")
        print("╚══════════════════════════════════════════════════════════════╝")
        print("\033[0m")

        print("Ingresa la siguiente información:\n")

        # -------------------------
        # BUSCAR PACIENTE
        # -------------------------

        pacientes = []

        while len(pacientes) == 0:

            nombrePaciente = input(
                "Nombre del paciente : "
            ).upper().strip()

            while not funciones.validarNombre(nombrePaciente):
                print(
                    "\033[91m"
                    "⚠ Nombre inválido. Solo se permiten letras y espacios."
                    "\033[0m"
                )

                nombrePaciente = input(
                    "Nombre del paciente : "
                ).upper().strip()

            pacientes = crud.buscarPacientePorNombre(
                conexionBD,
                nombrePaciente
            )

            if len(pacientes) == 0:
                print(
                    "\n\033[91m"
                    "⚠ No existe un paciente con ese nombre."
                    "\033[0m\n"
                )

        print("\nPacientes encontrados:\n")

        print(
            f"{'ID':<5}"
            f"{'NOMBRE':<25}"
            f"{'EDAD':<8}"
            f"{'SEXO':<15}"
            f"{'TELÉFONO':<15}"
        )

        print("─" * 68)

        for paciente in pacientes:
            print(
                f"{paciente[0]:<5}"
                f"{paciente[1][:25]:<25}"
                f"{paciente[2]:<8}"
                f"{paciente[3][:15]:<15}"
                f"{paciente[5]:<15}"
            )

        print("─" * 68)

        idsPacientes = []

        for paciente in pacientes:
            idsPacientes.append(str(paciente[0]))

        idPaciente = ""

        while idPaciente not in idsPacientes:

            idPaciente = input(
                "\nSelecciona el ID correcto del paciente: "
            ).strip()

            if idPaciente not in idsPacientes:
                funciones.opcionInvalida()

        # -------------------------
        # BUSCAR DOCTOR
        # -------------------------

        doctores = []

        while len(doctores) == 0:

            nombreDoctor = input(
                "\nNombre del doctor   : "
            ).upper().strip()

            while not funciones.validarNombre(nombreDoctor):
                print(
                    "\033[91m"
                    "⚠ Nombre inválido. Solo se permiten letras y espacios."
                    "\033[0m"
                )

                nombreDoctor = input(
                    "\nNombre del doctor   : "
                ).upper().strip()

            doctores = crud.buscarDoctorPorNombre(
                conexionBD,
                nombreDoctor
            )

            if len(doctores) == 0:
                print(
                    "\n\033[91m"
                    "⚠ No existe un doctor con ese nombre."
                    "\033[0m\n"
                )

        print("\nDoctores encontrados:\n")

        print(
            f"{'ID':<5}"
            f"{'NOMBRE':<28}"
            f"{'ESPECIALIDAD':<25}"
            f"{'CONSULTORIO':<15}"
        )

        print("─" * 73)

        for doctor in doctores:
            print(
                f"{doctor[0]:<5}"
                f"{doctor[1][:28]:<28}"
                f"{doctor[2][:25]:<25}"
                f"{doctor[4][:15]:<15}"
            )

        print("─" * 73)

        idsDoctores = []

        for doctor in doctores:
            idsDoctores.append(str(doctor[0]))

        idDoctor = ""

        while idDoctor not in idsDoctores:

            idDoctor = input(
                "\nSelecciona el ID correcto del doctor: "
            ).strip()

            if idDoctor not in idsDoctores:
                funciones.opcionInvalida()

        funciones.borrarPantalla()

        print("\033[95m")
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║                                                              ║")
        print("║                       ➕  AGREGAR CITA                       ║")
        print("║                                                              ║")
        print("╚══════════════════════════════════════════════════════════════╝")
        print("\033[0m")

        # -------------------------
        # FECHA CON REGEX
        # -------------------------

        fecha = input(
            "\nFecha (AAAA-MM-DD) : "
        ).strip()

        while not funciones.validarFecha(fecha):
            print(
                "\033[91m"
                "⚠ Fecha inválida. Usa el formato AAAA-MM-DD."
                "\033[0m"
            )

            fecha = input(
                "Fecha (AAAA-MM-DD) : "
            ).strip()

        # -------------------------
        # HORA CON REGEX
        # -------------------------

        hora = input(
            "Hora (HH:MM)       : "
        ).strip()

        while not funciones.validarHora(hora):
            print(
                "\033[91m"
                "⚠ Hora inválida. Usa el formato HH:MM."
                "\033[0m"
            )

            hora = input(
                "Hora (HH:MM)       : "
            ).strip()

        motivo = input(
            "Motivo             : "
        ).upper().strip()

        respuesta = crud.insertar(
            idPaciente,
            idDoctor,
            fecha,
            hora,
            motivo,
            conexionBD
        )

        if respuesta:
            funciones.accionExitosa()
        else:
            funciones.accionNoExitosa()

        resp = ""

        while resp not in ["si", "no"]:
            resp = input(
                "\n¿Deseas registrar otra cita? (Si/No): "
            ).lower().strip()

    funciones.esperarTecla()


def mostrarCitas(conexionBD):
    funciones.borrarPantalla()

    print("\033[95m")
    print("╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("║                                                                                                                            ║")
    print("║                                                     📋  MOSTRAR CITAS                                                      ║")
    print("║                                                                                                                            ║")
    print("╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝")
    print("\033[0m")

    citas = crud.consultar(conexionBD)

    if len(citas) > 0:

        print(
            f"\n{'ID':<5}"
            f"{'PACIENTE':<25}"
            f"{'DOCTOR':<25}"
            f"{'ESPECIALIDAD':<22}"
            f"{'FECHA':<13}"
            f"{'HORA':<12}"
            f"{'MOTIVO':<30}"
        )

        print("─" * 132)

        for cita in citas:
            print(
                f"{cita[0]:<5}"
                f"{str(cita[1])[:25]:<25}"
                f"{str(cita[2])[:25]:<25}"
                f"{str(cita[3])[:22]:<22}"
                f"{str(cita[4]):<13}"
                f"{str(cita[5]):<12}"
                f"{str(cita[6])[:30]:<30}"
            )

        print("─" * 132)
        print(
            f"\nTotal de citas registradas: {len(citas)}"
        )

    else:
        print("\n⚠ No existen citas registradas.\n")

    funciones.esperarTecla()


def buscarCitas(conexionBD):
    resp = "si"

    while resp == "si":

        opcion = ""

        while opcion not in [
            "1", "2", "3", "4", "5", "6", "7"
        ]:

            funciones.borrarPantalla()

            print("\033[95m")
            print("╔══════════════════════════════════════════════════════════════╗")
            print("║                                                              ║")
            print("║                        🔎  BUSCAR CITA                       ║")
            print("║                                                              ║")
            print("╚══════════════════════════════════════════════════════════════╝")
            print("\033[0m")

            print("¿Cómo deseas realizar la búsqueda?\n")
            print("\t[1] Buscar por ID")
            print("\t[2] Buscar por paciente")
            print("\t[3] Buscar por doctor")
            print("\t[4] Buscar por especialidad")
            print("\t[5] Buscar por fecha")
            print("\t[6] Buscar por hora")
            print("\t[7] Buscar por motivo")

            opcion = input(
                "\n\033[93mSelecciona una opción: \033[0m"
            ).strip()

            if opcion not in [
                "1", "2", "3", "4", "5", "6", "7"
            ]:
                funciones.opcionInvalida()
                funciones.esperarTecla()

        dato = ""

        match opcion:

            case "1":
                dato = input(
                    "\nEscribe el ID de la cita: "
                ).strip()

            case "2":
                dato = input(
                    "\nEscribe el nombre del paciente: "
                ).upper().strip()

                while not funciones.validarNombre(dato):
                    print(
                        "\033[91m"
                        "⚠ Nombre inválido. Solo se permiten letras y espacios."
                        "\033[0m"
                    )

                    dato = input(
                        "Escribe el nombre del paciente: "
                    ).upper().strip()

            case "3":
                dato = input(
                    "\nEscribe el nombre del doctor: "
                ).upper().strip()

                while not funciones.validarNombre(dato):
                    print(
                        "\033[91m"
                        "⚠ Nombre inválido. Solo se permiten letras y espacios."
                        "\033[0m"
                    )

                    dato = input(
                        "Escribe el nombre del doctor: "
                    ).upper().strip()

            case "4":
                dato = input(
                    "\nEscribe la especialidad: "
                ).upper().strip()

                while not funciones.validarNombre(dato):
                    print(
                        "\033[91m"
                        "⚠ Especialidad inválida. "
                        "Solo se permiten letras y espacios."
                        "\033[0m"
                    )

                    dato = input(
                        "Escribe la especialidad: "
                    ).upper().strip()

            case "5":
                dato = input(
                    "\nEscribe la fecha (AAAA-MM-DD): "
                ).strip()

                while not funciones.validarFecha(dato):
                    print(
                        "\033[91m"
                        "⚠ Fecha inválida. Usa el formato AAAA-MM-DD."
                        "\033[0m"
                    )

                    dato = input(
                        "Escribe la fecha (AAAA-MM-DD): "
                    ).strip()

            case "6":
                dato = input(
                    "\nEscribe la hora (HH:MM): "
                ).strip()

                while not funciones.validarHora(dato):
                    print(
                        "\033[91m"
                        "⚠ Hora inválida. Usa el formato HH:MM."
                        "\033[0m"
                    )

                    dato = input(
                        "Escribe la hora (HH:MM): "
                    ).strip()

            case "7":
                dato = input(
                    "\nEscribe el motivo: "
                ).upper().strip()

        funciones.borrarPantalla()

        print("\033[95m")
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║                                                              ║")
        print("║                        🔎  BUSCAR CITA                       ║")
        print("║                                                              ║")
        print("╚══════════════════════════════════════════════════════════════╝")
        print("\033[0m")

        citas = crud.buscar(
            conexionBD,
            opcion,
            dato
        )

        if len(citas) > 0:

            print(
                f"\n{'ID':<5}"
                f"{'PACIENTE':<25}"
                f"{'DOCTOR':<25}"
                f"{'ESPECIALIDAD':<22}"
                f"{'FECHA':<13}"
                f"{'HORA':<12}"
                f"{'MOTIVO':<30}"
            )

            print("─" * 132)

            for cita in citas:
                print(
                    f"{cita[0]:<5}"
                    f"{str(cita[1])[:25]:<25}"
                    f"{str(cita[2])[:25]:<25}"
                    f"{str(cita[3])[:22]:<22}"
                    f"{str(cita[4]):<13}"
                    f"{str(cita[5]):<12}"
                    f"{str(cita[6])[:30]:<30}"
                )

            print("─" * 132)

        else:
            print(
                "\n⚠ No se encontró ninguna cita con ese dato.\n"
            )

        opc = ""

        while opc not in ["si", "no"]:
            opc = input(
                "\n¿Deseas buscar otra cita? (Si/No): "
            ).lower().strip()

        resp = opc

    funciones.esperarTecla()


def borrarCitas(conexionBD):

    funciones.borrarPantalla()

    print("\033[91m")
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║                                                              ║")
    print("║                        ➖  BORRAR CITA                       ║")
    print("║                                                              ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print("\033[0m")

    nombrePaciente = input(
        "Escribe el nombre del paciente de la cita: "
    ).upper().strip()

    while not funciones.validarNombre(nombrePaciente):
        print(
            "\033[91m"
            "⚠ Nombre inválido. Solo se permiten letras y espacios."
            "\033[0m"
        )

        nombrePaciente = input(
            "Escribe el nombre del paciente de la cita: "
        ).upper().strip()

    citas = crud.buscar(
        conexionBD,
        "2",
        nombrePaciente
    )

    if len(citas) > 0:

        print(
            f"\n{'ID':<5}"
            f"{'PACIENTE':<25}"
            f"{'DOCTOR':<25}"
            f"{'ESPECIALIDAD':<22}"
            f"{'FECHA':<13}"
            f"{'HORA':<12}"
            f"{'MOTIVO':<30}"
        )

        print("─" * 132)

        for i in citas:
            print(
                f"{i[0]:<5}"
                f"{str(i[1])[:25]:<25}"
                f"{str(i[2])[:25]:<25}"
                f"{str(i[3])[:22]:<22}"
                f"{str(i[4]):<13}"
                f"{str(i[5]):<12}"
                f"{str(i[6])[:30]:<30}"
            )

        print("─" * 132)

        idsCitas = []

        for i in citas:
            idsCitas.append(str(i[0]))

        idCita = ""

        while idCita not in idsCitas:

            idCita = input(
                "\nEscribe el ID de la cita que deseas borrar: "
            ).strip()

            if idCita not in idsCitas:
                funciones.opcionInvalida()

        opc = ""

        while opc not in ["si", "no"]:
            opc = input(
                "\n¿Estás seguro de borrar esta cita? (Si/No): "
            ).lower().strip()

        if opc == "si":

            respuesta = crud.borrar(
                conexionBD,
                idCita
            )

            if respuesta:
                funciones.accionExitosa()
            else:
                funciones.accionNoExitosa()

        else:
            print("\nOperación cancelada.")

    else:
        print(
            "\n⚠ No existen citas registradas para ese paciente.\n"
        )

    funciones.esperarTecla()


def modificarCitas(conexionBD):

    funciones.borrarPantalla()

    print("\033[93m")
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║                                                              ║")
    print("║                      🔁  MODIFICAR CITA                      ║")
    print("║                                                              ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print("\033[0m")

    nombrePaciente = input(
        "Escribe el nombre del paciente de la cita: "
    ).upper().strip()

    while not funciones.validarNombre(nombrePaciente):
        print(
            "\033[91m"
            "⚠ Nombre inválido. Solo se permiten letras y espacios."
            "\033[0m"
        )

        nombrePaciente = input(
            "Escribe el nombre del paciente de la cita: "
        ).upper().strip()

    citas = crud.buscar(
        conexionBD,
        "2",
        nombrePaciente
    )

    if len(citas) > 0:

        print(
            f"\n{'ID':<5}"
            f"{'PACIENTE':<25}"
            f"{'DOCTOR':<25}"
            f"{'ESPECIALIDAD':<22}"
            f"{'FECHA':<13}"
            f"{'HORA':<12}"
            f"{'MOTIVO':<30}"
        )

        print("─" * 132)

        for i in citas:
            print(
                f"{i[0]:<5}"
                f"{str(i[1])[:25]:<25}"
                f"{str(i[2])[:25]:<25}"
                f"{str(i[3])[:22]:<22}"
                f"{str(i[4]):<13}"
                f"{str(i[5]):<12}"
                f"{str(i[6])[:30]:<30}"
            )

        print("─" * 132)

        idsCitas = []

        for i in citas:
            idsCitas.append(str(i[0]))

        idCita = ""

        while idCita not in idsCitas:

            idCita = input(
                "\nEscribe el ID de la cita que deseas modificar: "
            ).strip()

            if idCita not in idsCitas:
                funciones.opcionInvalida()

        opc = ""

        while opc not in ["si", "no"]:
            opc = input(
                "\n¿Estás seguro de modificar esta cita? (Si/No): "
            ).lower().strip()

        funciones.borrarPantalla()

        print("\033[93m")
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║                                                              ║")
        print("║                      🔁  MODIFICAR CITA                      ║")
        print("║                                                              ║")
        print("╚══════════════════════════════════════════════════════════════╝")
        print("\033[0m")

        if opc == "si":

            print("\nIngresa los nuevos datos de la cita:\n")

            # -------------------------
            # NUEVO PACIENTE
            # -------------------------

            pacientes = []

            while len(pacientes) == 0:

                nuevoNombrePaciente = input(
                    "Nombre del nuevo paciente : "
                ).upper().strip()

                while not funciones.validarNombre(
                    nuevoNombrePaciente
                ):
                    print(
                        "\033[91m"
                        "⚠ Nombre inválido. "
                        "Solo se permiten letras y espacios."
                        "\033[0m"
                    )

                    nuevoNombrePaciente = input(
                        "Nombre del nuevo paciente : "
                    ).upper().strip()

                pacientes = crud.buscarPacientePorNombre(
                    conexionBD,
                    nuevoNombrePaciente
                )

                if len(pacientes) == 0:
                    print(
                        "\n⚠ No existe un paciente con ese nombre.\n"
                    )

            print("\nPacientes encontrados:\n")

            print(
                f"{'ID':<5}"
                f"{'NOMBRE':<25}"
                f"{'EDAD':<8}"
                f"{'SEXO':<15}"
                f"{'TELÉFONO':<15}"
            )

            print("─" * 68)

            for paciente in pacientes:
                print(
                    f"{paciente[0]:<5}"
                    f"{paciente[1][:25]:<25}"
                    f"{paciente[2]:<8}"
                    f"{paciente[3][:15]:<15}"
                    f"{paciente[5]:<15}"
                )

            print("─" * 68)

            idsPacientes = []

            for paciente in pacientes:
                idsPacientes.append(
                    str(paciente[0])
                )

            idPaciente = ""

            while idPaciente not in idsPacientes:

                idPaciente = input(
                    "\nSelecciona el ID correcto del paciente: "
                ).strip()

                if idPaciente not in idsPacientes:
                    funciones.opcionInvalida()

            # -------------------------
            # NUEVO DOCTOR
            # -------------------------

            doctores = []

            while len(doctores) == 0:

                nuevoNombreDoctor = input(
                    "\nNombre del nuevo doctor : "
                ).upper().strip()

                while not funciones.validarNombre(
                    nuevoNombreDoctor
                ):
                    print(
                        "\033[91m"
                        "⚠ Nombre inválido. "
                        "Solo se permiten letras y espacios."
                        "\033[0m"
                    )

                    nuevoNombreDoctor = input(
                        "\nNombre del nuevo doctor : "
                    ).upper().strip()

                doctores = crud.buscarDoctorPorNombre(
                    conexionBD,
                    nuevoNombreDoctor
                )

                if len(doctores) == 0:
                    print(
                        "\n⚠ No existe un doctor con ese nombre.\n"
                    )

            print("\nDoctores encontrados:\n")

            print(
                f"{'ID':<5}"
                f"{'NOMBRE':<28}"
                f"{'ESPECIALIDAD':<25}"
                f"{'CONSULTORIO':<15}"
            )

            print("─" * 73)

            for doctor in doctores:
                print(
                    f"{doctor[0]:<5}"
                    f"{doctor[1][:28]:<28}"
                    f"{doctor[2][:25]:<25}"
                    f"{doctor[4][:15]:<15}"
                )

            print("─" * 73)

            idsDoctores = []

            for doctor in doctores:
                idsDoctores.append(
                    str(doctor[0])
                )

            idDoctor = ""

            while idDoctor not in idsDoctores:

                idDoctor = input(
                    "\nSelecciona el ID correcto del doctor: "
                ).strip()

                if idDoctor not in idsDoctores:
                    funciones.opcionInvalida()

            funciones.borrarPantalla()

            print("\033[93m")
            print("╔══════════════════════════════════════════════════════════════╗")
            print("║                                                              ║")
            print("║                      🔁  MODIFICAR CITA                      ║")
            print("║                                                              ║")
            print("╚══════════════════════════════════════════════════════════════╝")
            print("\033[0m")

            # -------------------------
            # NUEVA FECHA CON REGEX
            # -------------------------

            fecha = input(
                "\nNueva fecha (AAAA-MM-DD): "
            ).strip()

            while not funciones.validarFecha(fecha):
                print(
                    "\033[91m"
                    "⚠ Fecha inválida. Usa el formato AAAA-MM-DD."
                    "\033[0m"
                )

                fecha = input(
                    "Nueva fecha (AAAA-MM-DD): "
                ).strip()

            # -------------------------
            # NUEVA HORA CON REGEX
            # -------------------------

            hora = input(
                "Nueva hora (HH:MM): "
            ).strip()

            while not funciones.validarHora(hora):
                print(
                    "\033[91m"
                    "⚠ Hora inválida. Usa el formato HH:MM."
                    "\033[0m"
                )

                hora = input(
                    "Nueva hora (HH:MM): "
                ).strip()

            motivo = input(
                "Nuevo motivo: "
            ).upper().strip()

            respuesta = crud.modificar(
                conexionBD,
                idCita,
                idPaciente,
                idDoctor,
                fecha,
                hora,
                motivo
            )

            if respuesta:
                funciones.accionExitosa()
            else:
                funciones.accionNoExitosa()

        else:
            print("\nOperación cancelada.")

    else:
        print(
            "\n⚠ No existen citas registradas para ese paciente.\n"
        )

    funciones.esperarTecla()


def limpiarCitas(conexionBD):
    funciones.borrarPantalla()

    print("\033[91m")
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║                                                              ║")
    print("║                       ⚠️  LIMPIAR CITAS                       ║")
    print("║                                                              ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print("\033[0m")

    print(
        "\033[91m"
        "⚠ Esta acción eliminará TODAS las citas registradas."
    )

    print(
        "⚠ Esta operación no se puede deshacer."
        "\033[0m\n"
    )

    opc = ""

    while opc not in ["si", "no"]:
        opc = input(
            "¿Estás seguro que deseas borrar TODAS las citas? (Si/No): "
        ).lower().strip()

    if opc == "si":

        respuesta = crud.vaciar(
            conexionBD
        )

        if respuesta:
            funciones.accionExitosa()
        else:
            funciones.accionNoExitosa()

    else:
        print("\nOperación cancelada.")

    funciones.esperarTecla()


def generarPDF(conexionBD):

    funciones.borrarPantalla()

    print("\033[95m")
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║                                                              ║")
    print("║                  📄  GENERAR COMPROBANTE                     ║")
    print("║                                                              ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print("\033[0m")

    nombrePaciente = input(
        "Escribe el nombre del paciente: "
    ).upper().strip()

    while not funciones.validarNombre(nombrePaciente):
        print(
            "\033[91m"
            "⚠ Nombre inválido. Solo se permiten letras y espacios."
            "\033[0m"
        )

        nombrePaciente = input(
            "Escribe el nombre del paciente: "
        ).upper().strip()

    citas = crud.buscar(
        conexionBD,
        "2",
        nombrePaciente
    )

    if len(citas) > 0:

        print(
            f"\n{'ID':<5}"
            f"{'PACIENTE':<25}"
            f"{'DOCTOR':<25}"
            f"{'ESPECIALIDAD':<22}"
            f"{'FECHA':<13}"
            f"{'HORA':<12}"
            f"{'MOTIVO':<30}"
        )

        print("─" * 132)

        for i in citas:
            print(
                f"{i[0]:<5}"
                f"{str(i[1])[:25]:<25}"
                f"{str(i[2])[:25]:<25}"
                f"{str(i[3])[:22]:<22}"
                f"{str(i[4]):<13}"
                f"{str(i[5]):<12}"
                f"{str(i[6])[:30]:<30}"
            )

        print("─" * 132)

        idsCitas = []

        for i in citas:
            idsCitas.append(
                str(i[0])
            )

        idCita = ""

        while idCita not in idsCitas:

            idCita = input(
                "\nEscribe el ID de la cita para generar el PDF: "
            ).strip()

            if idCita not in idsCitas:
                funciones.opcionInvalida()

        cita = crud.obtenerCitaPDF(
            conexionBD,
            idCita
        )

        if cita != None:

            os.makedirs(
                "Comprobantes",
                exist_ok=True
            )

            nombreArchivo = (
                "Comprobantes/"
                + "Cita_"
                + str(cita[0])
                + "_"
                + cita[1].replace(" ", "_")
                + ".pdf"
            )

            pdf = canvas.Canvas(
                nombreArchivo,
                pagesize=letter
            )

            ancho, alto = letter

            pdf.setTitle(
                "Comprobante de cita"
            )

            pdf.setFont(
                "Helvetica-Bold",
                20
            )

            pdf.drawCentredString(
                ancho / 2,
                alto - 70,
                "SISTEMA DE CLINICA"
            )

            pdf.setFont(
                "Helvetica-Bold",
                15
            )

            pdf.drawCentredString(
                ancho / 2,
                alto - 100,
                "COMPROBANTE DE CITA"
            )

            pdf.line(
                60,
                alto - 120,
                ancho - 60,
                alto - 120
            )

            pdf.setFont(
                "Helvetica",
                12
            )

            y = alto - 160

            pdf.drawString(
                80,
                y,
                f"Folio de cita: {cita[0]}"
            )

            y -= 35

            pdf.drawString(
                80,
                y,
                f"Paciente: {cita[1]}"
            )

            y -= 30

            pdf.drawString(
                80,
                y,
                f"Doctor: {cita[2]}"
            )

            y -= 30

            pdf.drawString(
                80,
                y,
                f"Especialidad: {cita[3]}"
            )

            y -= 30

            pdf.drawString(
                80,
                y,
                f"Consultorio: {cita[4]}"
            )

            y -= 45

            pdf.drawString(
                80,
                y,
                f"Fecha: {cita[5]}"
            )

            y -= 30

            pdf.drawString(
                80,
                y,
                f"Hora: {cita[6]}"
            )

            y -= 45

            pdf.drawString(
                80,
                y,
                f"Motivo: {cita[7]}"
            )

            y -= 60

            pdf.line(
                60,
                y,
                ancho - 60,
                y
            )

            pdf.setFont(
                "Helvetica",
                10
            )

            pdf.drawCentredString(
                ancho / 2,
                y - 30,
                "Favor de presentarse con anticipacion a su cita."
            )

            pdf.save()

            print(
                "\n\033[92m"
                "✓ Comprobante PDF generado correctamente."
                "\033[0m"
            )

            print(
                f"\nArchivo generado: {nombreArchivo}"
            )

        else:
            funciones.accionNoExitosa()

    else:
        print(
            "\n⚠ No existen citas registradas "
            "para ese paciente.\n"
        )

    funciones.esperarTecla()