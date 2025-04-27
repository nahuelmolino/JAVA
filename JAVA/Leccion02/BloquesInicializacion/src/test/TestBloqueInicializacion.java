package test;

import domain.Persona;

public class TestBloqueInicializacion {

    public static void main(String[] args) {
        Persona persona1 = new Persona();
        System.out.println("persona1 = " + persona1);

         Persona persona2 = new Persona();
         System.out.println("persona2 = " + persona2);
         
         /*
        Persona persona3 = new Persona();
        
        
        System.out.println(persona1.getIDPersona());
        System.out.println(persona2.getIDPersona());
        System.out.println(persona3.getIDPersona());*/
    }

    //se carga en memoria la clase con el estatico.
    //se crea la instancia de la clase, antes de que se ejecute el constructor se ejecuta el dinamico.
}
