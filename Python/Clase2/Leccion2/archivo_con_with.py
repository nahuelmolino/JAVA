from ManejoArchivo import ManejoArchivos

# MANEJO DE CONTEXTO WITH: sintaxis simplificada, abre y cierra el archivo.
# uso de la palabra with y el manejo de archivos.. Manejo de contexton with
#with open('prueba.txt', 'r', encoding='utf8') as archivo :
 # print(archivo.read())
# No hace falta ni el try, ni el finally
# en el contexto de with lo que se ejecuta de manera automatica
# Utiliza diferentes métodos: __enter__(abre el recurso)
# Ahora el siguiente método: __exit__(cierra el recurso)

with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())


