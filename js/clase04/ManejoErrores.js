'use strict'

// Veamos como evitar este error
try{
    let x=10;//Lo traemos con alt + flecha hacia arriba o hacia abajo    
    miFuncion();
    throw 'Mi error';
}
catch(error){
    console.log(error) 
}
finally{
    console.log('Termina la revision de errores')
}   
//La ejecucion ahora continua... 
   console.log('Continuamos...') // Esto no se llega a ver porque esta bloqueado

   let resultado = 5;