# Declaramos una variable
try:
    archivo = open('prueba.txt', 'w', encoding='utf8') #La w es de write que en ingles significa escribir.
    archivo.write('Programamos con diferentes tipos de archivos, ahora en txt.\n') # el \n es el enter en el txt
    archivo.write('Los acenos son importantes para las palabras\n')
    archivo.write('como por ejemplo: acción, ejecución y producción\n')
    archivo.write('las letras son:\nr read leer, \na append anexa, \nw write escribe, \nx crea un archivo')
    archivo.write('\nt esta es para texto o text\nb esta es para binary(imagenes, videos, pdf.)\nw+ lee y escribe r+ \n')
    archivo.write('Con esto terminamos')

except Exception as e:
    print(e)
finally: # siempre se ejecuta
    archivo.close() # Con esto se debe cerrar el archivo.

# archivo.write('todo ok'): este es un error porque lo cerre antes.
