package paquete2;

public class Clase4 {
    //solo se accede desde un metodo get y set

    private String atributoPrivate = "Atributo privado";

    private Clase4() {
        System.out.println("construcor privado");

    }

    //Creamos un constructor publico para poder crear objetoss
    public Clase4(String argumento) {//Aqu� se puede llamar al construcor vacio
        this();//llamo al constructor privado
        System.out.println("Constructor publico");
    }

    //M�todo private
    private void metodoPrivado() {
        System.out.println("M�todo privado");
    }

    public String getAtributoPrivate() {
        return this.atributoPrivate;
    }

    public void setAtributoPrivate(String atributoPrivate) {
        this.atributoPrivate = atributoPrivate;
    }
    
    
}
