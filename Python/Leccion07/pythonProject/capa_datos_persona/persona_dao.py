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