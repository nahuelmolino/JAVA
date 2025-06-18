'use strict'

// Veamos como evitar este error
try{
    let x=10;//Lo traemos con alt + flecha hacia arriba o hacia abajo    
    //miFuncion();
    throw 'Mi error'; //Maneja tipo string
}
catch(error){
    console.log(typeof(error)) 
}
finally{
    console.log('Termina la revision de errores')
}   
//La ejecucion ahora continua... 
   console.log('Continuamos...') // Esto no se llega a ver porque esta bloqueado

   let resultado = 5;

   try{
        //y = 5;
        if(isNaN(resultado)) throw 'No es un número';
        else if(resultado ==='') throw 'Es cadena vacía';
        else if(resultado >= 0) throw 'Valor Positivo';
        else if(resultado <= 0) throw 'Valor Negativo';
   }
   catch(error){
        console.log(error);
        console.log(error.name);
        console.log(error.message)
   }
   finally{
        console.log('Termina la revisión de errores 2');
   }
