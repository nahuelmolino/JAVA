from logging import exception

opcion = None
while opcion != 4:
    try:
        print('Opciones: ')
        print('1. Agregar Pelicula')
        print('2. Listar las Peliculas')
        print('3. Eliminar catálogo de peliculas')
        print('4. Salir')
        opcion = int(input('Digite una opción de menú (1-4)'))
    except Exception as e:
        print(f'Ocurrió un error de tipo: {e}')
        opcion = None
    else:
        print('Salimos del programa')
