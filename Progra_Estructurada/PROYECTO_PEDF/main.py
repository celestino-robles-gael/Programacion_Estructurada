import funciones
from Pacientes import pacientes
from Citas import citas
from Doctores import doctores

conexionBD = funciones.conectar()
opc = "1"

while opc != "4":
    funciones.borrarPantalla()

    print("\033[96m")
    print("╔════════════════════════════════════════════════════╗")
    print("║                                                    ║")
    print("║                S I S T E M A   D E                 ║")
    print("║                C L Í N I C A  ✝️ ⚕️                  ║")
    print("║                                                    ║")
    print("╠════════════════════════════════════════════════════╣")
    print("║                                                    ║")
    print("║        [1] 👥 Gestión de pacientes                 ║")
    print("║                                                    ║")
    print("║        [2] 📄 Gestión de citas                     ║")
    print("║                                                    ║")
    print("║        [3] 💉 Gestión de doctores                  ║")
    print("║                                                    ║")
    print("║        [4] ↩️  Salir del sistema                    ║")
    print("║                                                    ║")
    print("╚════════════════════════════════════════════════════╝")
    print("\033[0m")

    opc = input("\n\033[93mSelecciona una opción: \033[0m").strip()

    match opc:
        case "1":
            opcionPacientes = "1"

            while opcionPacientes != "7":
                funciones.borrarPantalla()
                opcionPacientes = pacientes.menuPrincipal()

                match opcionPacientes:
                    case "1":
                        funciones.borrarPantalla()
                        pacientes.agregarPacientes(conexionBD)
                    case "2":
                        funciones.borrarPantalla()
                        pacientes.borrarPacientes(conexionBD)
                    case "3":
                        funciones.borrarPantalla()
                        pacientes.modificarPacientes(conexionBD)
                    case "4":
                        funciones.borrarPantalla()
                        pacientes.mostrarPacientes(conexionBD)
                    case "5":
                        funciones.borrarPantalla()
                        pacientes.buscarPacientes(conexionBD)
                    case "6":
                        funciones.borrarPantalla()
                        pacientes.limpiarPacientes(conexionBD)
                    case "7":
                        funciones.borrarPantalla()
                    case _:
                        funciones.opcionInvalida()

        case "2":
            opcionCitas = "1"

            while opcionCitas != "8":
                funciones.borrarPantalla()
                opcionCitas = citas.menuPrincipal()

                match opcionCitas:
                    case "1":
                        funciones.borrarPantalla()
                        citas.agregarCitas(conexionBD)
                    case "2":
                        funciones.borrarPantalla()
                        citas.borrarCitas(conexionBD)
                    case "3":
                        funciones.borrarPantalla()
                        citas.modificarCitas(conexionBD)
                    case "4":
                        funciones.borrarPantalla()
                        citas.mostrarCitas(conexionBD)
                    case "5":
                        funciones.borrarPantalla()
                        citas.buscarCitas(conexionBD)
                    case "6":
                        funciones.borrarPantalla()
                        citas.limpiarCitas(conexionBD)
                    case "7":
                        funciones.borrarPantalla()
                        citas.generarPDF(conexionBD)
                    case "8":
                        funciones.borrarPantalla()
                    case _:
                        funciones.opcionInvalida()

        case "3":
            opcionDoctores = "1"

            while opcionDoctores != "7":
                funciones.borrarPantalla()
                opcionDoctores = doctores.menuPrincipal()

                match opcionDoctores:
                    case "1":
                        funciones.borrarPantalla()
                        doctores.agregarDoctores(conexionBD)
                    case "2":
                        funciones.borrarPantalla()
                        doctores.borrarDoctores(conexionBD)
                    case "3":
                        funciones.borrarPantalla()
                        doctores.modificarDoctores(conexionBD)
                    case "4":
                        funciones.borrarPantalla()
                        doctores.mostrarDoctores(conexionBD)
                    case "5":
                        funciones.borrarPantalla()
                        doctores.buscarDoctores(conexionBD)
                    case "6":
                        funciones.borrarPantalla()
                        doctores.limpiarDoctores(conexionBD)
                    case "7":
                        funciones.borrarPantalla()
                    case _:
                        funciones.opcionInvalida()

        case "4":
            funciones.borrarPantalla()
            funciones.terminar()

        case _:
            funciones.opcionInvalida()