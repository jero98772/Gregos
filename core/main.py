#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#Gregos - by [jero98772,camilo,GianSz,camilo_alvarez,igatsi]
from .tools.tools import *
from flask import Flask, render_template ,request,redirect
import time

app = Flask(__name__)

player=None
AUDIO_PATH="core/static/mp3/audio.mp3"
BOARD_IMG_PATH="core/static/img/tmp"

class play:
	def __init__(self,player=None,depth=4):
		self.gregos=not player
		self.player=player
		self.board = chess.Board()
		self.turn=1
		self.depth=depth
		self.audio=1
	def get_board(self):
		return self.board
		#in future we add a langue option 	
	def greetingEs(self):
		return "hola soy Gregos y sere tu coach"
	def greetingEn(self):
		return "Hello i am Gregos an i will be your couch"
	def greetingBannerEs(self):
		return BANNER+"hola soy Gregos y sere tu coach"
	def greetingBannerEn(self):
		return BANNER+"Hello i am Gregos an i will be your couch "

class webpage():
	@app.route("/",methods=['POST','GET'])
	@app.route("/startgame.html",methods=['POST','GET'])	
	def startgame():
		if request.method == "POST":
			color=request.form["color"]
			level=request.form["level"]
			audio=request.form["audio"]
			gamemode=request.form["mode"].replace(" ","")
			color = 1 if color == "White" else 0
			global player
			player=play()
			player.player = color
			player.gregos = not color
			player.depth = int(level)-1
			player.audio = eval(audio)
			return redirect(f"/game/{gamemode}")
		return render_template("startgame.html",banner=BANNER)
		

	@app.route("/game/PlayervsMachine",methods=['POST','GET'])	
	def PlayervsMachine():
		save_board_as_image(player.get_board(),BOARD_IMG_PATH)

		if player.turn%2==player.gregos:#gregos play
			best_move,score=get_best_move(player.board, player.depth, player.gregos, player.gregos)
			gregos_move=best_move
			player.board.push_san(str(best_move))
			save_board_as_image(player.get_board(),BOARD_IMG_PATH)
			legal_moves=list(map(str,player.board.legal_moves))
			msg="i gregos move "+str(gregos_move)
			
			if player.audio:
				speak(msg,AUDIO_PATH,lang="en")
			
			player.turn+=1
			return render_template("play.html",gregos_move=gregos_move,moves=legal_moves,gregos_turn=(player.turn%2==player.gregos))
		
		legal_moves=list(map(str,player.board.legal_moves))
		if request.method == "POST":
			move=request.form["move"]
			gregos_move,score=get_best_move(player.board, 4, player.player, player.player)
			msg="i gregos recommends you"+str(gregos_move)
			
			if player.audio:
				speak(msg,AUDIO_PATH,lang="en")
			
			player.board.push_san(str(move))
			player.turn+=1
			save_board_as_image(player.get_board(),BOARD_IMG_PATH)

		if player.turn==1:
			if player.audio:
				speak(player.greetingEn(),AUDIO_PATH,lang="en")
			gregos_move="<pre>"+player.greetingBannerEn()+"</pre>"
		return render_template("play.html",gregos_move=gregos_move,moves=legal_moves,gregos_turn=(player.turn%2==player.gregos))

