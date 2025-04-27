package domain;

public class Persona {
    //bloques estaticos y no estaticos.
    //antes del constructor.
    
    //el error que marca es xq todavia no esta el constuctor.
    private final  int idPersona;
    private static int  contadorPersona;
    
    //Bloque de inicializacion estatico.
    //en los metodos estaticos no podemos usar this.
    //se ejecuta una sola vez
    static{
        //en los estaticos solo el nombre de la clase
        System.out.println("Ejecucion bloque estatico");
        ++Persona.contadorPersona; 
        //idPersona=10;No es estatico un atributo, por esto tenemos un error
    }
    
    //Bloque de inicializacion NO Estatico.(contexto dinamico.)
    //bsata con abrir y cerrar llaves
    //se ejecuta cada vez que se  instancia la clase.
    {
        System.out.println("Ejecucion del bloque NO estático");
        this.idPersona = Persona.contadorPersona++;//Incrementamos el atributo
     }
    
    //Los bloques de inicializacion se ejecutan antes del constructor.
    
    
    //constructor
    
    public Persona(){
    
        System.out.println("Ejecucion del constructor");
    }
    
    //metodo get para recuuperar idPersona.
    
    
    public int getIDPersona(){
        return this.idPersona;
    }
}
 