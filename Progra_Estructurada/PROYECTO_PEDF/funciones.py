import mysql.connector
import re

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="clinica"
        )

        return conexion

    except:
        borrarPantalla()
        input(
            "⚠ ¡Por el momento no es posible establecer conexión "
            "entre el sistema y la base de datos, por favor "
            "inténtelo más tarde! ⚠"
        )

        return None

def borrarPantalla():
    print("\033c")


# COLORES
VERDE = "\033[92m"
ROJO = "\033[91m"
AMARILLO = "\033[93m"
CYAN = "\033[96m"
NEGRITA = "\033[1m"
RESET = "\033[0m"

NOMBRE_SISTEMA = "SISTEMA DE CLÍNICA"
LONGITUD_TELEFONO = 10

def accionExitosa():
    print(
        f"\n{VERDE}{NEGRITA}"
        "✔ OPERACIÓN REALIZADA CORRECTAMENTE"
        f"{RESET}\n"
    )

def accionNoExitosa():
    print(
        f"\n{ROJO}{NEGRITA}"
        "✘ NO SE PUDO REALIZAR LA OPERACIÓN"
        f"{RESET}\n"
    )


def opcionInvalida():
    print(
        f"\n{AMARILLO}{NEGRITA}"
        "⚠ OPCIÓN INVÁLIDA, INTENTA DE NUEVO"
        f"{RESET}\n"
    )

def esperarTecla():
    input(
        f"\n{CYAN}"
        "Presiona ENTER para continuar..."
        f"{RESET}"
    )

def terminar():
    print(f"\n{CYAN}{NEGRITA}")
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║                                                              ║")
    print(f"║{NOMBRE_SISTEMA:^62}║")
    print("║                                                              ║")
    print("║                    SISTEMA FINALIZADO                        ║")
    print("║                                                              ║")
    print("║             Gracias por utilizar el sistema.                 ║")
    print("║                                                              ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print(RESET)

# VALIDACIONES CON REGEX
def validarNombre(nombre):
    return re.fullmatch(
        r"[A-ZÁÉÍÓÚÜÑ ]+",
        nombre
    )

def validarEdad(edad):
    return re.fullmatch(
        r"\d{1,3}",
        edad
    )


def validarSexo(sexo):
    return re.fullmatch(
        r"(MASCULINO|FEMENINO)",
        sexo
    )


def validarTelefono(telefono):
    return re.fullmatch(
        rf"\d{{{LONGITUD_TELEFONO}}}",
        telefono
    )

def validarFecha(fecha):
    return re.fullmatch(
        r"\d{4}-\d{2}-\d{2}",
        fecha
    )


def validarHora(hora):
    return re.fullmatch(
        r"([01]\d|2[0-3]):[0-5]\d",
        hora
    )