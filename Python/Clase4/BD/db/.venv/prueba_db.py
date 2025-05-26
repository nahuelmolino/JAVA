import psycopg2
# Esto es para poder conectarnos a Postgre
conexion = psycopg2.connect(    user = 'postgres',    password = 'admin',    host = '127.0.0.1',    port = '5432',    database = 'test_db')
# print (conexion)
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona'
            cursor.execute(sentencia)  # De esta manera ejecutamos la sentencia
            registros = cursor.fetchall()  # Recuperamos todos los registros que serán una lista
            print(registros)
except Exception as e:
        print(f'Ocurrió un error: {e}')
finally:
    conexion.close()

# devuelve una lista, que internamente tiene una tupla, cada registro se almacena en una tupla

# cantidad de registros

# mostar lista

# https://www.psycopg.org/docs/usage.html
