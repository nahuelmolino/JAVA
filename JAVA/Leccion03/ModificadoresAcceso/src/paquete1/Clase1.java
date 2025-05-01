package paquete1;

public class Clase1 {
   //atributo
    public String atributoPublico = "Valor atributo public";
    protected String atributoProtected =  "valor atributo protected";
    
    public Clase1(){
        System.out.println("Constructor publico");
    }
    
    protected Clase1(String atributoProtected){
        System.out.println("Constructor protected");}
     
    public void metodoPublico (){
        System.out.println("Método public");
    }
    
    protected void metodoProtected(){
        System.out.println("Método protected");}
}
