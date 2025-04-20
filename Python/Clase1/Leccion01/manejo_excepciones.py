#Capturar error de division por Cero.
resultado = None # None significa no valor

try:
    a = int(input('Digite el primer número: '))
    b = int(input('Digite el segundo número: '))
    resultado = a / b # modificamos
except TypeError as e:
    print(f'TypeError - Ocurrió un error: {type(e)}')
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrió un error: {type(e)}')
except Exception as e:
    print(f'Exception - Ocurrió un error: {type(e)}')
else:
    print(f'No se arrojo ninguna excepción')
finally: # Siempre se va a ejecutar
    print(f'Ejecucion de este bloque finally')

#Procesamiento de excepciones


print(f'El resulado es: {resultado}')
print('seguimos...')
