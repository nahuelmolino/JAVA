
package ar.com.system2023.mundopc;

/*Clase Padre Disponsitivo entrada.*/
public class DispositivoEntrada {
    
    /*Atributos privados*/
    private String tipoEntrada;
    private String marca;
    
    /*Constructor*/
    public DispositivoEntrada(String tipoEntrada, String marca){
        this.tipoEntrada=tipoEntrada;
        this.marca=marca;
        
    }
    
    /*getter y setter */
    
    public String getTipoEntrada(){
        return this.tipoEntrada;
    }
    
    public void setTipoEntrada(String tipoEntrada){
        this.tipoEntrada = tipoEntrada;
    }


    public String getMarca() {
        return this.marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    @Override
    public String toString() {
        return "DispositivoEntrada{" + "tipoEntrada=" + tipoEntrada + ", marca=" + marca + '}';
    }
    
    
    
}
