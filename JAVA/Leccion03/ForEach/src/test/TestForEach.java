package test;

public class TestForEach {
    public static void main(String[] args) {
        int edades[]= {5,6,8,9}; // sintaxis resumida
     //for convencional   
        for (int i = 0; i < edades.length; i++) {
            System.out.println("edades["+i+"]" + edades[i] );
        }
        //sirve para arreglos, colecciones y listas.
        //definimos una variable donde guarda los valores del arreglo.
        for(int edad : edades){ //sintaxis del ForEach
            System.out.println("edad = " + edad);
        }
        
    }
}
