package test;

public class TestAutoBoxingUnboxing {
    public static void main(String[] args) {
        //cada uno de los metodos primitivos tiene una clase envolvente
        //Clases envolventes o Wrapper
        /*
            Clases envolventes de tipo primitivos
        int = la clase envolvente es Integer
        
        */
        //para muchos calculos tipo primitivo, int por ejemplo
        //para pocos calculos usamos el object por ejemplo Integer que es una clase con sus respectivos metodos.
        int enteroPrim = 10;// Tipo primitivo
        Integer entero = 10;// Tipo object con la clase Integer
        
          System.out.println("entero = " + enteroPrim);
          System.out.println("entero = " + entero.toString());
        
    }
}
