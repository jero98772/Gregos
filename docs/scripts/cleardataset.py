import chess
board = chess.Board()

#convertir todas las jugadas a un valor numerico en notacion uci , pero con numeros en el tablero
#ejemeplo e2e4 -> 5254

def uci2algebraic(move:str,board:chess.Board()):
  """
  convert from uci notation to algebraic notation
  """
  movef=chess.Move.from_uci(move)
  return board.san(movef)