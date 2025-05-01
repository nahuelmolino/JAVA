package paquete2;

import paquete1.Clase1;
//clase hija de la clase 1, esta puede acceder a lo protected de la otra.
public class Clase3 extends Clase1 {
     public Clase3(){
         super("protected");
         this.atributoProtected="Accedemos desde la clase hija";
         System.out.println("AtributoProteted = " + this.atributoProtected);
         this.atributoPublico = "es totalmente publico";
         
         
     }
}
