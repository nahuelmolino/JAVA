
package ar.com.system2023.mundopc;

public class Raton extends DispositivoEntrada{
    /*Atributos*/
    private final int idRaton;
    private static int contadorRatones;
    
    /*Constructor*/
    
    public Raton(String tipoEntrada, String marca){
        super(tipoEntrada, marca);
        this.idRaton= ++Raton.contadorRatones;
               
    }

    @Override
    public String toString() {
        return "Raton{" + "idRaton=" + idRaton + ", "+ super.toString()+'}';
    }
    
    
    
}
