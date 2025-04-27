package enumeraciones;

public enum Continentes {
    AFRICA(53,"1.2 billones"),
    EUROPA(46,"1.1 billones"),
    ASIA(44,"1.9 millones"),
    AMERICA(34,"150 millones"),
    OCEANIA(14, "1.2 billones");

    //atributo encapsulado: xq es de tipo private, necesito si o si el metodo para accederlo.
    private final int paises;
    private final String habitantes;
    
    Continentes(int paises, String habitantes){
        this.paises=paises;
        this.habitantes = habitantes;
    }
    
    //M�todo Get
    public int getPaises(){
        return this.paises;
    }
    
    public String getHabitantes(){
        return this.habitantes;
    }
}
