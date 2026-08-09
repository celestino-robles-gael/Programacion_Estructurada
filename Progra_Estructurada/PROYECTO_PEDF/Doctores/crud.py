import funciones


def insertar(Nombre, Especialidad, Telefono, Consultorio, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()

            cursor.execute(
                "insert into doctores values(null,%s,%s,%s,%s)",
                (Nombre, Especialidad, Telefono, Consultorio)
            )

            conexionBD.commit()
            return True

        else:
            return False

    except:
        return False


def consultar(conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()

            cursor.execute("select * from doctores")

            return cursor.fetchall()

        else:
            return []

    except:
        return []


def buscar(conexionBD, opcion, dato):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()

            campos = {
                "1": "id",
                "2": "Nombre",
                "3": "Especialidad",
                "4": "Telefono",
                "5": "Consultorio"
            }

            if opcion in campos:
                campo = campos[opcion]

                consulta = f"select * from doctores where {campo}=%s"

                cursor.execute(consulta, (dato,))

                return cursor.fetchall()

            else:
                return []

        else:
            return []

    except:
        return []


def vaciar(conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()

            cursor.execute("delete from doctores")
            cursor.execute("alter table doctores auto_increment=1")

            conexionBD.commit()
            return True

        else:
            return False

    except:
        return False


def borrar(conexionBD, opcion, dato):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()

            if opcion == "1":
                consulta = "delete from doctores where id=%s"

            elif opcion == "2":
                consulta = "delete from doctores where Nombre=%s"

            else:
                return False

            cursor.execute(consulta, (dato,))

            conexionBD.commit()
            return True

        else:
            return False

    except:
        return False


def modificar(
    conexionBD,
    opcion,
    dato,
    nombre,
    especialidad,
    telefono,
    consultorio
):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()

            if opcion == "1":
                consulta = """
                update doctores
                set Nombre=%s,
                    Especialidad=%s,
                    Telefono=%s,
                    Consultorio=%s
                where id=%s
                """

                valores = (
                    nombre,
                    especialidad,
                    telefono,
                    consultorio,
                    dato
                )

            elif opcion == "2":
                consulta = """
                update doctores
                set Nombre=%s,
                    Especialidad=%s,
                    Telefono=%s,
                    Consultorio=%s
                where Nombre=%s
                """

                valores = (
                    nombre,
                    especialidad,
                    telefono,
                    consultorio,
                    dato
                )

            else:
                return False

            cursor.execute(consulta, valores)

            conexionBD.commit()
            return True

        else:
            return False

    except:
        return False