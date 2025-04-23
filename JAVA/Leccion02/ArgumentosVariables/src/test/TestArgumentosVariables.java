
package test;

public class TestArgumentosVariables {
    public static void main(String[] args) {
     imprimirNumeros(1,2,3,4,8);
     
     imprimirNumeros(1,28);
     
    }
    //tipo ... significa que vamos a recibir argumentos varibales.
    //se convierte en un arreglo. Se trata igual
    private static void imprimirNumeros(int ...numeros){
        for (int i = 0; i < numeros.length; i++) {
            System.out.println("Elementos: " + numeros[i]);
        }
    }
    
    
}
