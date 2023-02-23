#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#Gregos - by [jero98772,camilo,GianSz,camilo_alvarez,igatsi]
import chess
import os
import random
from gtts import gTTS
BANNER="""
  ____                          
 / ___|_ __ ___  __ _  ___  ___ 
| |  _| '__/ _ \/ _` |/ _ \/ __|
| |_| | | |  __/ (_| | (_) \__ \ 
 \____|_|  \___|\__, |\___/|___/
                |___/           
"""
POINTS_BY_PIECE=[(chess.PAWN, 1), (chess.BISHOP, 4), (chess.KING, 0), (chess.QUEEN, 10), (chess.KNIGHT, 5),(chess.ROOK, 3)]
def speak(audioString:str,lang='es'):
	"""
	speak audioString variable using google text to speak and a system call
	"""
	tts = gTTS(text=audioString,lang=lang)
	tts.save("audio.mp3")
	os.system("mpg123 audio.mp3")
def score_analisis(board:chess.Board(), my_color:bool):
	"""
	score_analisis the heuristic , this function calculate the score of the board
	"""
	score = random.random() 
	for (piece, value) in POINTS_BY_PIECE:
		score+=len(board.pieces(piece, my_color)) * value#i can eat
		score-=len(board.pieces(piece, not my_color)) * value#other can eat me
	score += 100 if board.is_checkmate() else 0
	#score += 10 if board.is_capture(move)  else 0#ahoga
	#square =  str(move)[-2:]  
	#myAttackers = board.attackers(not my_color,  chess.parse_square(square))
	#score +=len(myAttackers)*-2
	return score
def gameover(board:chess.Board())->bool:
	"""
	get board objet and return true if game is finish
	"""
	return board.is_stalemate() or board.is_stalemate() #or board.outcome()#check how work outcome()

def minimax(board:chess.Board(), depth:int, maximizing_player, maximizing_color,alpha,beta):
	"""
	this function use minmax function alpha and beta pruning
	minimax (board:chess.Board(), depth:int, maximizing_player, maximizing_color)
	"""
	if depth == 0 or gameover(board):#game over??
		#return None, staticAnalysis(board, maximizing color)#evalute stattsic

		return None, score_analisis(board,maximizing_color)
	#print(board)
	moves=list(board.legal_moves)#board.get moves ()
	#moves = board.get moves ()
	best_move = random.choice(moves)
	if maximizing_player:
		max_eval = float('-inf')
		for move in moves:
			board.push_san(str(move))    
			current_eval = minimax (board, depth-1,False,maximizing_color,alpha,beta,)[1]
			board.pop()
			if current_eval > max_eval:
				max_eval = current_eval
				best_move = move
			alpha=max(alpha,current_eval)
			if beta<=alpha:
				break
		return best_move, max_eval
	else:
		min_eval = float('inf')
		for move in moves:
			#board.make move (move[0], move[1])
			board.push_san(str(move))    
			current_eval = minimax(board, depth-1,True,maximizing_color,alpha,beta,)[1]
			board.pop()
			#board.unmake move ()
			if current_eval < min_eval:
				min_eval = current_eval
				best_move=move
			beta=min(alpha,current_eval)
			if beta<=alpha:
				break
		return best_move, min_eval
"""
r n b . k b n r
p p p p . p p p
. . . . . . . .
. . . . p . . .
. . . . . . . R
. . . P . . . .
P P P . P P P .
R N . Q K B N .


"""