class Pelicula:

    # constructor de la clase: se ejecuta automaticamente cuando se crea un objeto de la calse.
    # Recibe el parametro nombre, que asigna el atributo protegido llamado _nombre
    # self: hace referencia al objeto que se está creando
    # _nombre: el _ inicial indica que es un atributo protegido que no deberia modificarse desde afuera de la calse.

    def __init__(self,nombre):
        self._nombre = nombre
    # este metodo define lo que se muestra cuadno haces print(objeto) o str(objeto)
    def __str__(self):
        return f'Pelicula: {self._nombre}'

    # este convierte a nombre en una propiedad, permiet acceder a _nombre como si fuera un atribut publico, pero en realidad esta llamando a este metodo.
    # print(p.nombre)
    # getter
    @property
    def nombre(self):
        return self._nombre

    # setter
    # esto permite modificar el atributo _nombre de forma controlada, tambien usando la sintaxis de atributo
    # p.nombre = "Matrix"
    @nombre.setter
    # Pero en realidad, eso llama al método nombre(self, nombre) y cambia _nombre.
    def nombre(self,nombre):
        self._nombre=nombre



