def insertar(idPaciente, idDoctor, fecha, hora, motivo, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()

            cursor.execute(
                """
                INSERT INTO citas
                VALUES (NULL, %s, %s, %s, %s, %s)
                """,
                (
                    idPaciente,
                    idDoctor,
                    fecha,
                    hora,
                    motivo
                )
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

            cursor.execute(
                """
                SELECT
                    citas.id,
                    pacientes.Nombre,
                    doctores.Nombre,
                    doctores.Especialidad,
                    citas.Fecha,
                    citas.Hora,
                    citas.Motivo
                FROM citas
                INNER JOIN pacientes
                    ON citas.idPaciente = pacientes.id
                INNER JOIN doctores
                    ON citas.idDoctor = doctores.id
                ORDER BY citas.Fecha, citas.Hora
                """
            )

            return cursor.fetchall()

        else:
            return []

    except:
        return []


def buscarPaciente(conexionBD, idPaciente):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()

            cursor.execute(
                "SELECT * FROM pacientes WHERE id=%s",
                (idPaciente,)
            )

            return cursor.fetchone()

        else:
            return None

    except:
        return None


def buscarDoctor(conexionBD, idDoctor):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()

            cursor.execute(
                "SELECT * FROM doctores WHERE id=%s",
                (idDoctor,)
            )

            return cursor.fetchone()

        else:
            return None

    except:
        return None


def buscarPacientePorNombre(conexionBD, nombre):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()

            cursor.execute(
                """
                SELECT *
                FROM pacientes
                WHERE Nombre=%s
                """,
                (nombre,)
            )

            return cursor.fetchall()

        else:
            return []

    except:
        return []


def buscarDoctorPorNombre(conexionBD, nombre):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()

            cursor.execute(
                """
                SELECT *
                FROM doctores
                WHERE Nombre=%s
                """,
                (nombre,)
            )

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
                "1": "citas.id",
                "2": "pacientes.Nombre",
                "3": "doctores.Nombre",
                "4": "doctores.Especialidad",
                "5": "citas.Fecha",
                "6": "citas.Hora",
                "7": "citas.Motivo"
            }

            if opcion in campos:
                campo = campos[opcion]

                consulta = f"""
                    SELECT
                        citas.id,
                        pacientes.Nombre,
                        doctores.Nombre,
                        doctores.Especialidad,
                        citas.Fecha,
                        citas.Hora,
                        citas.Motivo
                    FROM citas
                    INNER JOIN pacientes
                        ON citas.idPaciente = pacientes.id
                    INNER JOIN doctores
                        ON citas.idDoctor = doctores.id
                    WHERE {campo}=%s
                    ORDER BY citas.Fecha, citas.Hora
                """

                cursor.execute(
                    consulta,
                    (dato,)
                )

                return cursor.fetchall()

            else:
                return []

        else:
            return []

    except:
        return []


def buscarCitaPorId(conexionBD, idCita):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()

            cursor.execute(
                """
                SELECT *
                FROM citas
                WHERE id=%s
                """,
                (idCita,)
            )

            return cursor.fetchone()

        else:
            return None

    except:
        return None


def borrar(conexionBD, idCita):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()

            cursor.execute(
                """
                DELETE FROM citas
                WHERE id=%s
                """,
                (idCita,)
            )

            conexionBD.commit()
            return True

        else:
            return False

    except:
        return False


def modificar(
    conexionBD,
    idCita,
    idPaciente,
    idDoctor,
    fecha,
    hora,
    motivo
):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()

            cursor.execute(
                """
                UPDATE citas
                SET idPaciente=%s,
                    idDoctor=%s,
                    Fecha=%s,
                    Hora=%s,
                    Motivo=%s
                WHERE id=%s
                """,
                (
                    idPaciente,
                    idDoctor,
                    fecha,
                    hora,
                    motivo,
                    idCita
                )
            )

            conexionBD.commit()
            return True

        else:
            return False

    except:
        return False


def vaciar(conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()

            cursor.execute(
                "DELETE FROM citas"
            )

            cursor.execute(
                "ALTER TABLE citas AUTO_INCREMENT=1"
            )

            conexionBD.commit()
            return True

        else:
            return False

    except:
        return False


def obtenerCitaPDF(conexionBD, idCita):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()

            cursor.execute(
                """
                SELECT
                    citas.id,
                    pacientes.Nombre,
                    doctores.Nombre,
                    doctores.Especialidad,
                    doctores.Consultorio,
                    citas.Fecha,
                    citas.Hora,
                    citas.Motivo
                FROM citas
                INNER JOIN pacientes
                    ON citas.idPaciente = pacientes.id
                INNER JOIN doctores
                    ON citas.idDoctor = doctores.id
                WHERE citas.id=%s
                """,
                (idCita,)
            )

            return cursor.fetchone()

        else:
            return None

    except:
        return None