import funciones

def insertar(Nombre, Edad, Sexo, Direccion, Telefono, conexionBD):
    try:
        if conexionBD!=None:
            cursor=conexionBD.cursor()
            cursor.execute("insert into pacientes values(null,%s,%s,%s,%s,%s)",(Nombre, Edad, Sexo, Direccion, Telefono))
            conexionBD.commit()
            return True
        else:
            return False
    except:
        return False
    
def consultar(conexionBD):
    try:
        if conexionBD!=None:
            cursor=conexionBD.cursor()
            cursor.execute("select * from pacientes")
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
                "2": "nombre",
                "3": "edad",
                "4": "sexo",
                "5": "direccion",
                "6": "telefono"
            }

            if opcion in campos:
                campo = campos[opcion]

                consulta = f"select * from pacientes where {campo}=%s"
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
        if conexionBD!=None:
            cursor=conexionBD.cursor()
            cursor.execute("delete from pacientes")
            cursor.execute("ALTER TABLE pacientes AUTO_INCREMENT=0")
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
                consulta = "delete from pacientes where id=%s"

            elif opcion == "2":
                consulta = "delete from pacientes where nombre=%s"

            else:
                return False

            cursor.execute(consulta, (dato,))
            conexionBD.commit()

            return True

        else:
            return False

    except:
        return False

def modificar(conexionBD, opcion, dato, nombre, edad, sexo, direccion, telefono):
    try:
        if conexionBD != None:

            cursor = conexionBD.cursor()

            if opcion == "1":
                consulta = """
                UPDATE pacientes
                SET nombre=%s, edad=%s, sexo=%s, direccion=%s, telefono=%s
                WHERE id=%s
                """
                valores = (nombre, edad, sexo, direccion, telefono, dato)

            elif opcion == "2":
                consulta = """
                UPDATE pacientes
                SET nombre=%s, edad=%s, sexo=%s, direccion=%s, telefono=%s
                WHERE nombre=%s
                """
                valores = (nombre, edad, sexo, direccion, telefono, dato)

            else:
                return False

            cursor.execute(consulta, valores)
            conexionBD.commit()

            return True

        else:
            return False

    except:
        return False
