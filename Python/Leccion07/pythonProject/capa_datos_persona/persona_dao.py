from capa_datos_persona.Persona import Persona
from capa_datos_persona.conexion import Conexion
from logger_base import log


class PersonaDAO:
    """
        DAO significa : DATA ACCSS OBJECT
        CRUD significa:
            CREATE  --> Insertar
            READ --> Seleccionar
            UPDATE --> Actualizacion
            DELETE --> Eliminar
    """
    _SELECCIONAR = "SELECT * from persona ORDER BY id_persona"
    _INSERTAR = "INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)"
    _ACTUALIZAR = "UPDATE persona SET nombre = %s, apellido = %s, email = %s where id_persona = %s"
    _eliminar = "DELETE FROM persona WHERE id_persona = %s"

    #Definimos metodos de clase
    @classmethod
    def seleccionar(cls):
        #Armar conexiones automaticas
        with    Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                # lista
                personas = []
                for registro in registros:
                    persona = Persona(registro[0],registro[1],registro[2],registro[3])
                    personas.append(persona)
                return personas

if __name__ == '__main__' :
    personas = PersonaDAO.seleccionar()
    for persona in personas:
       log.debug(persona)