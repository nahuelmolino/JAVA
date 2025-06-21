import psycopg2 as bd # Esto es para poder conectarnos a Postgre
from psycopg2.errorcodes import CONNECTION_EXCEPTION

conexion = bd.connect(user = 'postgres', password = 'admin', host = '127.0.0.1', port = '5432', database = 'test_db')

try:
    conexion.autocommit = False # no se guarda de forma automatica # esto directamente no debería estar, inicia la transaccion
    cursor = conexion.cursor()

    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s,%s,%s)'
    valores = ('María', 'Esparza', 'mesparza@mail.com')
    cursor.execute(sentencia, valores)
    conexion.commit() # hacemos el commit manuanlamente
    print('Termina la transacción')
except Exception as e:
    conexion.rollback()
    print(f'Ocurrió un error, se hizo un rollback : {e}')
finally:
    conexion.close()