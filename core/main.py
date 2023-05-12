#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#Gregos - by jero98772
from .tools.tools import *
from flask import Flask, render_template ,request,redirect,session
import time

app = Flask(__name__)
app.secret_key = str(time.time())

AUDIO_PATH="core/static/mp3/audio.mp3"
BOARD_IMG_PATH="core/static/img/tmp"
player=None
BASELANGE="en"
class webpage:
	@app.route("/",methods=['POST','GET'])
	@app.route("/startgame.html",methods=['POST','GET'])	
	def startgame():
		if request.method == "POST":
			color=request.form["color"]
			level=request.form["level"]
			audio=request.form["audio"]
			langue=str(request.form["langue"])[0:2].lower()
			gamemode=request.form["mode"].replace(" ","")
			color = 1 if color == "White" else 0
			#print(player)
			global player
			print(player)
			player=play(lang=langue)
			print(player)
			player.player = color
			player.gregos = not color
			player.depth = int(level)-1
			player.audio = eval(audio)
			player.langueWords = transateweb(langue)
			return redirect(f"/game/{gamemode}")
		return render_template("startgame.html",banner=BANNER,langues=LANGUES)

	@app.route("/game/PlayervsMachine",methods=['POST','GET'])	
	def PlayervsMachine():
		win_probability=None
		print(player.turn)
		save_board_as_image(player.board,BOARD_IMG_PATH)
		print(player.langue)
		if len(player.openings)==1:
			player.opening=webTranslate("you opening is",BASELANGE,player.langue)+" "+player.openings["opening_name"][0]
			speak(player.opening,AUDIO_PATH,lang="en")
		print(player.turn)	
		if len(player.openings)==0 and player.opening=="":
			player.opening=webTranslate("you make a unknown opening",BASELANGE,player.langue)
			speak(player.opening,AUDIO_PATH,lang="en")
		print(player.turn)
		if player.turn%2==player.gregos:#gregos play
			best_move,score=get_best_move(player.board, player.depth, player.gregos, player.gregos)
			gregos_move=best_move
			movef = uci2algebraic(str(best_move),player.get_board())
			player.board.push_san(str(best_move))
			player.openings=calculate_posibles_openings(movef,player.turn-1,webTranslate("moves",BASELANGE,player.langue),player.openings["opening_name"],player.openings)
			"""
			i use str(board.san(move)) to format move example from e2e4 for e4, to uci to normal notacion  
			"""
			save_board_as_image(player.get_board(),BOARD_IMG_PATH)
			legal_moves=list(map(str,player.board.legal_moves))
			msg=webTranslate("i gregos move",BASELANGE,player.langue)+" "+str(gregos_move)
			
			if player.audio:
				speak(msg,AUDIO_PATH,lang="en")
			
			player.turn+=1
			return render_template("play.html",gregos_move=gregos_move,moves=legal_moves,gregos_turn=(player.turn%2==player.gregos),opening=player.opening,trad=player.langueWords)
		print(player.turn)		
		legal_moves=list(map(str,player.board.legal_moves))
		if request.method == "POST":
			move=request.form["move"]
			gregos_move,score=get_best_move(player.board, 4, player.player, player.player)#change 4 for play.deep
			msg=webTranslate("i gregos recommends you",BASELANGE,player.langue)+" "+str(gregos_move)
			
			if player.audio:
				speak(msg,AUDIO_PATH,lang="en")

			movef = uci2algebraic(move,player.get_board())
			player.openings=calculate_posibles_openings(movef,player.turn-1,webTranslate("moves",BASELANGE,player.langue),player.openings["opening_name"],player.openings)
			player.board.push_san(str(move))
			player.turn+=1
			save_board_as_image(player.get_board(),BOARD_IMG_PATH)
		print(player.turn)	
		if player.turn==1:
			if player.audio:
				speak(webTranslate(player.greeting(),BASELANGE,player.langue),AUDIO_PATH,lang="en")
			gregos_move="<pre>"+BANNER+"\n"+webTranslate(player.greeting(),BASELANGE,player.langue)+"</pre>"
		print(player.turn)	
		return render_template("play.html",gregos_move=gregos_move,moves=legal_moves,gregos_turn=(player.turn%2==player.gregos),opening=player.opening,trad=player.langueWords)

