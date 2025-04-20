#Capturar error de division por Cero.
resultado = None # None significa no valor
a = 7
b = 0
try:
    resultado = a / b # modificamos
except TypeError as e:
    print(f'TypeError - Ocurrió un error: {type(e)}')
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrió un error: {type(e)}')
except Exception as e:
    print(f'Exception - Ocurrió un error: {type(e)}')
#Procesamiento de excepciones

print(f'El resulado es: {resultado}')
print('seguimos...')
 