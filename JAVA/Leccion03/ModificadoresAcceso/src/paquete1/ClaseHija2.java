package paquete1;

public class ClaseHija2 extends Clase2 {
    public ClaseHija2(){
        super();
        this.atributoDefault = "Modificaci�n del atributo Default";
        System.out.println("atributoDefault = " + this.atributoDefault);
        this.metodoDefault();
        
    }
}
