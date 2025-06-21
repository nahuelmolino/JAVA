import logging as log

# docs.python.org/3/howto/logging.html
# Llamamos una configuración básica

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s:%(levelname)s [%(filename)s:%(lineno)s] %(message)s',  # hora, nivel, archivo y linea que dio error
                datefmt='%I:%M:$S %p', # configuramos hora: i= hora, m: minutos, s: segundos p: am o pm
                handlers=[
                    log.FileHandler('capa_datos.log'), #nombre de archivo
                    log.StreamHandler() #consola que venimos manejando
                ]) # handlers: manejador de

if __name__ == '__main__':
    log.debug('Mensaje a nivel debug')
    log.info('Mensaje a nivel info')
    log.warning('Mensaje a nivel warning')
    log.error('Mensaje a nivel error')
    log.critical('Mensaje a nivel critical')