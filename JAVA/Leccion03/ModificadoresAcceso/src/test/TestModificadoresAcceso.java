package test;

import paquete1.Clase1;
import paquete2.Clase3;

public class TestModificadoresAcceso {
    //Public: puede ser utilizada desde una clase o desde otra clase, en cualquier parte de nuestro proyecto.
    
    public static void main(String[] args) {
        //aca creo la instancia en memoria de la clase, y si tiene constructor la crea.
        Clase1 clase1 = new Clase1();
        System.out.println("clase1 = " + clase1.atributoPublico);
        clase1.metodoPublico();
        
        Clase3 claseHija = new Clase3();
        System.out.println("claseHija = " + claseHija);
    }
   
}
