#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#Gregos - by [jero98772,camilo,GianSz,camilo_alvarez,igatsi]
import chess
from multiprocessing import Pool
import os
import random
import chess.svg
from gtts import gTTS

BANNER="""
  ____                          
 / ___|_ __ ___  __ _  ___  ___ 
| |  _| '__/ _ \/ _` |/ _ \/ __|
| |_| | | |  __/ (_| | (_) \__ \ 
 \____|_|  \___|\__, |\___/|___/
                |___/           
"""
POINTS_BY_PIECE = [
  (chess.PAWN,100),
  (chess.KNIGHT,320),
  (chess.BISHOP, 330),
  (chess.ROOK, 500),
  (chess.QUEEN, 900),
  (chess.KING, 20000)
]
def uci2algebraic(move:str,board:chess.Board()):
	"""
	convert from uci notation to algebraic notation
	"""
	movef=chess.Move.from_uci(move)
	return board.san(movef)
def speak(audioString:str,path:str,lang='es'):
	"""
	speak audioString variable using google text to speak and a system call
	"""
	tts = gTTS(text=audioString,lang=lang)
	tts.save(path)
	os.system("mpg123 "+path)

def all_attackers(board:chess.Board(),color:bool)->int:
	"""
	return a number of attackers for color
	"""
	total=0
	for i in range(64):
  		total+=len(board.attackers(color,i)) 
	return total

def calculate_posibles_openings(move:str,turn:int,colname:str,rows:list,dataframe):
  """

  """
  for i in range(len(rows)):
    try:
      if dataframe[colname][i].split()[turn]!=move:
        dataframe=dataframe.drop(index=i)
    except:
      dataframe=dataframe.drop(index=i)

  return dataframe.reset_index(drop=True)

def save_board_as_image(board:chess.Board(),path:str):
	"""
	save board as image
	"""
	boardsvg = chess.svg.board(board)
	outputfile = open(path+".svg", "w")
	outputfile.write(boardsvg)
	outputfile.close()

def score_analisis(board:chess.Board(), my_color:bool):
	"""
	score_analisis the heuristic , this function calculate the score of the board
	"""
	score = random.random()*10
	for (piece, value) in POINTS_BY_PIECE:
		score+=len(board.pieces(piece, my_color)) * value
		score-=len(board.pieces(piece, not my_color)) * value
	score += 100 if board.is_checkmate() else 0
	score -= 20 if board.is_insufficient_material() else 0
	score -= 10 if board.is_stalemate() else 0
	
	#add pawns structure
	#score +=all_attackers(board,not my_color)
	#score -=all_attackers(board,my_color)
	return score
def winner(board:chess.Board(),turn:bool)->str:
	"""
	return a string the color of the winner
	"""
	if board.is_checkmate():
		if turn:return "White Win"
		else:return "Black Win"
	else: 
		return "No winner"

def gameover(board:chess.Board())->bool:
	"""
	Function that is in charge of evaluating if the match has gotten to a stalemate point, if it did returns
 	True, otherwise returns False.
	"""
	return board.is_stalemate() or board.is_insufficient_material() or board.is_checkmate() or board.is_seventyfive_moves() or board.is_variant_draw()

def alphabeta(board:chess.Board, depth:int, alpha:int, beta:int,  maximizing_player:bool, maximizing_color:bool) -> int:
  """
  #This function implements the MinMax algorithm along with the Alpha-Beta pruning enhancement technique. 
  #Minmax is an heuristic search algorithm that finds the best possible way to make a play when there's multiple 
  #choices available. Also works with the help of Alpha-Beta pruning technique which iscommonly use to discard 
  #the choices (branches of the tree) that don't show any benefits respect to the solution.
  """
  if depth == 0 or board.is_game_over():
    return score_analisis(board, maximizing_color)
  # Generate legal moves
  legal_moves = list(board.legal_moves)
  # Randomize moves to avoid predictable move patterns
  random.shuffle(legal_moves)
  
  if maximizing_player:
    max_eval = float('-inf')
    for move in legal_moves:
      board.push(move)
      eval = alphabeta(board, depth-1, alpha, beta, False, maximizing_color)
      board.pop()

      max_eval = max(max_eval, eval)
      alpha = max(alpha, eval)
      if beta <= alpha:
          break
    return max_eval
  else:
    min_eval = float('inf')
    for move in legal_moves:
      board.push(move)
      eval = alphabeta(board, depth-1, alpha, beta, True, maximizing_color)
      board.pop()

      min_eval = min(min_eval, eval)
      beta = min(beta, eval)
      if beta <= alpha:
          break
    return min_eval

def get_best_move(board:chess.Board, depth:int,  maximizing_player:bool, maximizing_color:bool):
  """
  Function that returns the best move using Alpha-Beta algorithm
  """
  best_move = None
  max_eval = float('-inf')
  alpha = float('-inf')
  beta = float('inf')
  for move in board.legal_moves:
      board.push(move)
      evalf = alphabeta(board, depth-1, alpha, beta,  maximizing_player, maximizing_color)
      board.pop()
      if evalf > max_eval:
          max_eval = evalf
          best_move = move
  return best_move, max_eval

