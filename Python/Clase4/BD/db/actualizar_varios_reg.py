import psycopg2 # Esto es para poder conectarnos a Postgre

conexion = psycopg2.connect(    user = 'postgres',    password = 'admin',    host = '127.0.0.1',    port = '5432',    database = 'test_db')
# print (conexion)
try:
    with (conexion):
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = (
                ('juan carlos','Roldan', 'rcarlos.mail@com',1),
                ('juan carlos', 'Roldan', 'rcarlos.mail@com',2),
                ('juan carlos', 'Roldan', 'rcarlos.mail@com',3)
            ) # Es una tupla
            cursor.executemany(sentencia, valores)  # De esta manera ejecutamos la sentencia
            registros_actualizados = cursor.rowcount
            print(f'Los registros actualizados son: {registros_actualizados}')


except Exception as e:
        print(f'Ocurrió un error: {e}')
finally:
    conexion.close()