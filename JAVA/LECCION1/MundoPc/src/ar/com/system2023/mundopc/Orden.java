package ar.com.system2023.mundopc;
//no extiende de ninguna clase

public class Orden {

    private final int idOrden;
    private Computadora computadora[];//Arreglo de objetos
    private static int contadorOrdenes;
    private static final int MAX_COMPUTADORAS = 10;//atributo maximo de computadora.
    private int contadorComputadoras; //variable interna para saber cuantas computadoras hemos creado para comparar con el maximo.

    public Orden() {
        this.idOrden = ++Orden.contadorOrdenes;
        this.computadora = new Computadora[Orden.MAX_COMPUTADORAS];

    }

//metodo para agregar una nueva computadora al arreglo.
    public void agregarComputadora(Computadora computadora) {
        if (this.contadorComputadoras < Orden.MAX_COMPUTADORAS) {//verifico que no se supere el maximo de computadoras.
            this.computadora[this.contadorComputadoras++] = computadora;

        } else {
            System.out.println("Has superaro el liminte: " + Orden.MAX_COMPUTADORAS);
        }
    }
//Mostrar orden

    public void mostrarOrden() {
        System.out.println("Orden #: " + this.idOrden);
        System.out.println("Computadoras de la orden #: " + this.idOrden);
        for (int i = 0; i < this.contadorComputadoras; i++) {
            System.out.println(this.computadora[i]);
        }

    }

}
