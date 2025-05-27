


const n = 5;
const board = Array.from({ length: n }, () => Array(n).fill(-1));


const moves = [
  [2, 1], [1, 2], [-1, 2], [-2, 1],
  [-2, -1], [-1, -2], [1, -2], [2, -1]
];


function esMovimientoValido(x, y, board) {
  return x >= 0 && x < n && y >= 0 && y < n && board[x][y] === -1;
}

function resolver(x, y, mov, board) {
  if (mov === n * n) return true;

  for (let [dx, dy] of moves) {
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
