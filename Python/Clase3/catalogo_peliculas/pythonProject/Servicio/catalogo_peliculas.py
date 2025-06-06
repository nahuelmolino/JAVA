import os

class CatalogoPeliculas:
    # atributo de clase( no de instancia) es compartido por todas las instancias de la clase.
    ruta_archivo = 'peliculas.txt'

    #puede acceder directamente a los atributos de clase
    # cls es contexto de clase
    #metodos de clase, lo que significa que no se necesita crear objetos de tipo Catalogo_peliculas para usar sus funciones
    @classmethod
    def agregar_peliculas(cls, pelicula):
        with open(cls.ruta_archivo, 'a', encoding = 'utf8') as archivo:
            archivo.write(f'{pelicula.nombre}\n')
    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo, 'r', encoding='utf8') as archivo:
            print(f'Catalogo de peliculas'.center(50, '-'))
            print(archivo.read())
    @classmethod
    def eliminar_peliculas(cls):
        os.remove(cls.ruta_archivo)
        print(f'Archivo eliminado: {cls.ruta_archivo}')

