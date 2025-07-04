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
    _INSERTAR = "INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)"
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

    @classmethod
    def insertar(cls,persona):
        with Conexion.obtenerConexion():
              with Conexion.obtenerCursor() as cursor:
                 valores = (persona.nombre, persona.apellido, persona.email)
                 cursor.execute(cls._INSERTAR,valores)
                 log.debug(f'Persona Insertada: {persona}')
                 return cursor.rowcount

    @classmethod
    def actualziar(cls,persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre,persona.apellido, persona.email, persona.id_persona)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f'Persona actualizada: {persona}')
                return cursor.rowcount
    @classmethod
    def eliminar(cls,persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.id_persona,) #la coma va porque es una tupla de valores
                cursor.execute(cls._eliminar, valores)
                log.debug(f'Los objetos eliminados son: {persona}')
                return cursor.rowcount

if __name__ == '__main__' :
   #eliminar un registro
   #persona1 = Persona(id_persona=2)
   #persona_eliminada = PersonaDAO.eliminar(persona1)
   #log.debug(f'Persona eliminada: {persona_eliminada}')


    # Actualizar un registro
    #persona1 = Persona(id_persona=2,nombre='Juan Jose', apellido='pena', email='jjpena@mail.com')
    #persona_actualizada = PersonaDAO.actualziar(persona1)
    #log.debug(f'Persona actualizada: {persona_actualizada}')

    # Insertar un registro
    #persona1 = Persona(nombre='omero', apellido='simpson', email='osimpson@mail.com')
    #personas_insertadas = PersonaDAO.insertar(persona1)
    #log.debug(f'Personas insertadas: {personas_insertadas} ')


    # Selecionar objetos
   personas = PersonaDAO.seleccionar()
   for persona in personas:
        log.debug(persona)

