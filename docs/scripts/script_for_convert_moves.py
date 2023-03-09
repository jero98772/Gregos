import chess
import pandas as pd
import time
board = chess.Board()
best_move="e2e4"
movef = chess.Move.from_uci(best_move)
movef = board.san(movef)
#movef=board.push_san(str(best_move))
#movef=board.san(movef)

def calculate_posibles_openings(move:str,turn:int,colname:str,rows:list,dataframe):
	for i in range(len(rows)):
		try:
			if dataframe[colname][i].split()[turn]!=move:
				dataframe=dataframe.drop(index=i)
		except:
			dataframe=dataframe.drop(index=i)

	return dataframe.reset_index(drop=True)

def test2():
	a=""
	df=pd.read_csv("chess_openings.csv")#.head(15000)
	board = chess.Board()
	move="e2e4"
	movef = chess.Move.from_uci(move)
	movef = board.san(movef)
	print(len(df),"\n",df)
	df=calculate_posibles_openings(movef,0,"moves",df["opening_name"],df)
	print(len(df),"\n",df)
	time.sleep(1)
	move="e7e5"
	movef = chess.Move.from_uci(move)
	movef = board.san(movef)
	df=calculate_posibles_openings(movef,1,"moves",df["opening_name"],df)
	print(len(df),"\n",df)
	time.sleep(1)
	move="d2d3"
	movef = chess.Move.from_uci(move)
	movef = board.san(movef)
	df=calculate_posibles_openings(movef,2,"moves",df["opening_name"],df)
	print(len(df),"\n",df)
	time.sleep(1)
	move="d7d6"
	movef = chess.Move.from_uci(move)
	movef = board.san(movef)
	df=calculate_posibles_openings(movef,3,"moves",df["opening_name"],df)
	print(len(df),"\n",df)
	time.sleep(1)
	move="g2g3"
	movef = chess.Move.from_uci(move)
	movef = board.san(movef)
	df=calculate_posibles_openings(movef,4,"moves",df["opening_name"],df)
	print(len(df),"\n",df)

	if len(df)==1:
		a=df["opening_name"][0]
		print("open name",df["opening_name"][0])
	df=calculate_posibles_openings("g5",5,"moves",df["opening_name"],df)
	#print("end")
	df=calculate_posibles_openings("g5",6,"moves",df["opening_name"],df)
	#print("end")
	df=calculate_posibles_openings("g5",7,"moves",df["opening_name"],df)
	print("end",a)
	print(len(df),"\n",df)

test2()

print(movef)
