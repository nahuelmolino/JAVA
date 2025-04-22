"use strict";

//clases

class Empleado{
    constructor(nombre,sueldo){
        this._nombre = nombre;
        this._sueldo = sueldo;
    }

    obtenerDetalles(){
        return `Empleado: nombre: ${this._nombre},
        Sueldo: ${this._sueldo}`;
    }
}

class Gerente extends Empleado{
    constructor(nombre,sueldo,departamento){
        super(nombre,sueldo);
        this._departamenteo = departamento;

    }

    obtenerDetalles(){
        return `Gerente: ${super.obtenerDetalles()} depto: ${this._departamenteo}`;
    }
}

//metodo fuera de ambas clases.
//segun el tipo que le pasemos es la info o rta que vamos a conseguir.
function imprimir(tipo){
    console.log(tipo.obtenerDetalles());
}

//instancias
let gerente1 = new Gerente("Carlos", 5000, "Sistemas");
console.log(gerente1) //Objeto de la clase hija

let empleado1 = new Empleado("Juan",3000);
console.log(empleado1);//Objeto de la clase padre

//obtenerDetalles tiene sobreescritura 
//polimorfismo, accememos en la funcion a los metodos correspondientes.

imprimir(gerente1)
imprimir(empleado1)

