import psycopg2 as bd # Esto es para poder conectarnos a Postgre
from psycopg2.errorcodes import CONNECTION_EXCEPTION

conexion = bd.connect(user = 'postgres', password = 'admin', host = '127.0.0.1', port = '5432', database = 'test_db')

try:
    conexion.autocommit = False # no se guarda de forma automatica # esto directamente no debería estar, inicia la transaccion
    cursor = conexion.cursor()

    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s,%s,%s)'
    valores = ('Carlos', 'Lara', 'clara@gmail.com')
    cursor.execute(sentencia, valores)
    sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
    valores = ('Juan', 'Juarez', 'jcjuarez@mail.com',7)
    cursor.execute(sentencia, valores)

    conexion.commit() # hacemos el commit manuanlamente , se cierra la transaccion
    print('Termina la transacción')
except Exception as e:
    conexion.rollback() # agrego el rollback
    print(f'Ocurrió un error, se hizo un rollback : {e}')
finally:
    conexion.close()