package mundoPc;

//Importador General
import ar.com.system2023.mundopc.*;

public class mundoPc {

    public static void main(String[] args) {
        //crear objetos de raton teclado monitor
        //crear objetos de computadora
        //crear objetos de orden.
//Computadora HP
        Monitor monitorHP = new Monitor("HP", 13);//Importar la calse 
        Teclado tecaldoHP = new Teclado("Bluetooth", "HP");
        Raton ratonHP = new Raton("Bluetooth", "HP");
        Computadora compurtadoraHP = new Computadora("Computadora HP", monitorHP, tecaldoHP, ratonHP);

//Computadora Gamer        
        Monitor monitorGamer = new Monitor("Gamer", 32);//Importar la calse 
        Teclado tecaldoGamer = new Teclado("Bluetooth", "Gamer");
        Raton ratonGamer = new Raton("Bluetooth", "Gamer");
        Computadora compurtadoraGamer = new Computadora("Computadora Gamer", monitorGamer, tecaldoGamer, ratonGamer);

        Orden orden1 = new Orden();// Inicializamos el arreglo vacio.
        Orden orden2 = new Orden();//Una nueva lista para el objeto orden.
        orden1.agregarComputadora(compurtadoraHP);
        orden1.agregarComputadora(compurtadoraGamer);
        orden1.agregarComputadora(compurtadoraGamer);
        orden1.agregarComputadora(compurtadoraGamer);
        orden1.agregarComputadora(compurtadoraGamer);
        orden1.agregarComputadora(compurtadoraGamer);
        orden1.agregarComputadora(compurtadoraGamer);
        orden1.agregarComputadora(compurtadoraGamer);
        orden1.agregarComputadora(compurtadoraGamer);
        orden1.agregarComputadora(compurtadoraGamer);
        orden1.agregarComputadora(compurtadoraGamer);

        Computadora computadorasVarias = new Computadora("Computadora de diferentes marcas", monitorHP, tecaldoGamer, ratonHP);
        orden2.agregarComputadora(computadorasVarias);

        orden1.mostrarOrden();
        orden2.mostrarOrden();
    }

}
