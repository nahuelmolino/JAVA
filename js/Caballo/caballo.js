


const n = 4;
//creo un arreglo de n*n, donde relleno las posiciones con -1
const board = Array.from({ length: n }, () => Array(n).fill(-1));
const movimientosPosibles = [
 [-2, -1], [-2, 1],
  [-1, -2], [-1, 2],
  [1, -2], [1, 2],
  [2, -1], [2, 1]
];

console.log(board)
//desde cualquier posicion del tablero, como maximo se pueden hacer 8 movimientos.
// Cada tupla es (deltaFila, deltaColumna).
//basicamente es un arreglo de arreglos (matriz 2D en forma de lista)

/*
Cada subarreglo representa un movimiento válido del caballo en ajedrez:

[-2, -1] significa: subir 2 casillas y moverse 1 a la izquierda.

[1, 2] significa: bajar 1 casilla y moverse 2 a la derecha.

tablero[fila][columna]
*/
/*
console.log(board)


console.log(Array.from({ length: 3}, () => -1))

console.log(Array.from({ length: 3}, () => Array(3).fill(-1)))


console.log(Array.from({ length: 3 }, () => Array(3).fill(-1)))
function crearTablero(n) {
  const board = [];
  for (let i = 0; i < n; i++) {
    board[i] = []; // crear fila vacía
    for (let j = 0; j < n; j++) {
      board[i][j] = -1; // inicializar cada celda con -1
    }
  }
  return board;
}

const tablero = crearTablero(4);
console.log(tablero);

*/



//verifico que los movimientos sean validos, que no se excedan y tampoco lo hayan visitado antes.
function esMovimientoValido(x, y, board) {
  return x >= 0 && x < n && y >= 0 && y < n && board[x][y] === -1;
}

function resolver(x, y, mov, board) {
  console.log(board)
  if (mov === n * n) return true;

  for (let [dx, dy] of movimientosPosibles) {
    const nx = x + dx;
    const ny = y + dy;

    if (esMovimientoValido(nx, ny, board)) {
      board[nx][ny] = mov;
      if (resolver(nx, ny, mov + 1, board)) return true;
      board[nx][ny] = -1; // Backtrack
    }
  }
  return false;
}

function iniciarTourDelCaballo() {
  board[0][0] = 0;
  if (resolver(0, 0, 1, board)) {
    console.log("Tour encontrado:");
    console.table(board);
  } else {
    console.log("No hay solución.");
  }
}


iniciarTourDelCaballo()
