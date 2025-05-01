package paquete1;
//clase default o packege
/*
class Clase2 extends Clase1 {

    String atributoDefault = "Valor del atributo default";

    //Clase2() {
     //   System.out.println("Constructor default");
    //}

    Clase2 (){
        
        this.atributoDefault = "Modificación del atributo default";
        System.out.println("atributoDefault = " + this.atributoDefault);
        this.metodoDefault();
    }
    void metodoDefault() {
        System.out.println("Método default ");
    }
    
    

}
*/

class Clase2{
    String atributoDefault = "Valor del atributo default";
    Clase2(){
        System.out.println("Constructor Default");
    }
    
    void metodoDefault(){
        System.out.println("Método Default");
    }
}