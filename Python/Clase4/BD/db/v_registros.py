import psycopg2
# Esto es para poder conectarnos a Postgre
conexion = psycopg2.connect(    user = 'postgres',    password = 'admin',    host = '127.0.0.1',    port = '5432',    database = 'test_db')
# print (conexion)
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona where id_persona IN %s' # Placeholder
            entrada = input('Digite los id_persona a buscar (separados por coma): ')
            # tupla de tuplas
            llaves_primarias = (tuple(entrada.split(', ')),)
            cursor.execute(sentencia, llaves_primarias)  # De esta manera ejecutamos la sentencia
            registros = cursor.fetchall()  # Recuperamos todos los registros que serán una lista
            for registro in registros:
               print(registro)
except Exception as e:
        print(f'Ocurrió un error: {e}')
finally:
    conexion.close()