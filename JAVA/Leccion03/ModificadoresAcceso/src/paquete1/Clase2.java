package paquete1;
//clase default o packege

class Clase2 extends Clase1 {

    String atributoDefault = "Valor del atributo default";

    //Clase2() {
     //   System.out.println("Constructor default");
    //}

    public Clase2 (){
        super();
        this.atributoDefault = "Modificaci�n del atributo default";
        System.out.println("atributoDefault = " + this.atributoDefault);
        this.metodoDefault();
    }
    void metodoDefault() {
        System.out.println("M�todo default ");
    }
    
    

}
