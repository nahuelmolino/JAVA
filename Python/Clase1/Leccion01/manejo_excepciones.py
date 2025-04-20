#Capturar error de division por Cero.
resultado = None # None significa no valor
a = '10'
b = 0
try:
    resultado = a/b # modificamos
except Exception as e:
    print(f'Ocurrió un error: {e}')
#Procesamiento de excepciones

print(f'El resulado es: {resultado}')
print('seguimos...')