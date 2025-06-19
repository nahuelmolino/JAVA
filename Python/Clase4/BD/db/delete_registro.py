import psycopg2 # Esto es para poder conectarnos a Postgre

conexion = psycopg2.connect(    user = 'postgres',    password = 'admin',    host = '127.0.0.1',    port = '5432',    database = 'test_db')
# print (conexion)
try:
    with (conexion):
        with conexion.cursor() as cursor:
           sentencia = 'DELETE FROM persona where id_persona=%s'
           entrada = input('Digite el numero de registro a eliminar: ')
           valores = (entrada,)
           cursor.execute(sentencia, valores)  # De esta manera ejecutamos la sentencia
           registros_eliminados = cursor.rowcount
           print(f'Cantidad de registros eliminados: {registros_eliminados}')

except Exception as e:
        print(f'Ocurrió un error: {e}')
finally:
    conexion.close()