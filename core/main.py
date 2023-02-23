#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#Gregos - by [jero98772,camilo,GianSz,camilo_alvarez,igatsi]
from .tools.tools import *
from mesa import Agent,Model
class agent_gregos(Agent):
	def __init__(self,color):
		self.color=color
		self.moves=[]
		#print("El agente Gregos ha hecho su primera jugada")
	def make_move(self,board):
		move=random.choice(list(board.legal_moves))
		return str(move)
	def make_suggestion(self,board):
		move=random.choice(list(board.legal_moves))
		return str(move)
	def analize_player(self):
		pass
	def set_dificult(self,level):
		"""
		set_dificult will be integer in range 0<x<100
		"""
		pass
	def greeting(self):
		return BANNER+"hola soy Gregos y sere tu coach"
class player():
	def __init__(self,color):
		self.color=color
class model_gregos(Model):
	def __init__(self):
		self.agent=agent_gregos
		self.board=chess.Board()
	def agent_move(self):
		self.board.push_san(self.agent.move(self.board))
		return self.board
	def player_move(self,move):
		board.push_san(str(move))
	def ourBoard(self):
		return self.board
class cli:
	def __init__(self):
		self.gregos=agent_gregos(None)
		self.player=player(None)
		self.board = chess.Board()
		print(self.gregos.greeting())
	def ask_colors(self):
		print("Chose your color (default:random) \n\t[W:white]\n\t[B:black]\n\t[R:random]\n ")
		color=input().lower()
		if color=="w" or color=="white":
			turn=True
		elif color=="b" or color=="black":
			turn=False
		else:# color=="r" or color=="random":
			turn=random.randint(0,1)
		return turn
	def play(self):
		self.player.color=self.ask_colors()
		self.gregos.color=not self.player.color
		i=1
		while 1:
			print(self.board)
			if i%2==self.player.color:
				print(list(self.board.legal_moves))
				a=input("input:\n")
				#self.player.move()
				self.board.push_san(str(a))
				#tmp=self.board.pop()#undo move for grekos suggestion
				#self.gregos.move(best_move)
			else:
				best_move,score=minimax(self.board, 6, self.gregos.color, self.gregos.color, float('-inf'), float('inf'))
				print(best_move,score)
				#self.gregos.move(best_move)
				self.board.push_san(str(best_move))
			i+=1
