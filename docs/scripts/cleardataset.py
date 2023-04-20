import chess
import pandas as pd
board = chess.Board()

#san_mainline="d4 d5 c4 c6 cxd5 e6 dxe6 fxe6 Nf3 Bb4+ Nc3 Ba5 Bf4".split()
l="abcdefgh"
n="12345678"
mytable = str.maketrans(l, n)

def separate_moves(X,col_name="moves"):
	newdf=pd.DataFrame({"opening_name":df["opening_name"]})
	#for i in X.shape[0]:

	#n_moves = X.shape[0]#break every game in individual moves
	#moves = [[] for x in range(n_moves-1)]
	for _ in range(n_moves-1):
		game = eval(X[col_name][_])
	for move in game:
		try:
			player_move = move.split(" ")
		#print(player_move)
			moves[_].append(player_move)
			#moves[_].append(player_move[1]) #add white move
			#moves[_].append(player_move[2]) #add black move
		except:
      #if error occurs
			print(_, move)
	print(moves)
	#return moves
def changeNotation(san_mainline):
	san_mainline=san_mainline.split()
	#ns=""
	tmp=[]
	for move in san_mainline:
	    board.push_san(move)
	for move in san_mainline:
		m=str(board.pop()).translate(mytable)
		print(m)
		#ns+=m[:4]
		tmp.append(int(m[:4]))
	tmp.reverse()
	tmp=str(tmp).replace("[","").replace("]","").replace(" ","").replace(",","")
	print(tmp,"\n");exit()
	#print(san_mainline)
	return tmp

def test(df):
	a=df["moves"].apply(lambda x:len(x))
	#print(a.max(),a.idxmax())
	#print(df.iloc[a.idxmax()])
	n_cols = 2#a.max()

	# calculate the number of rows in each column
	n_rows = a.max()

	# reshape the data
	reshaped_data = df.to_numpy().reshape((-1, n_rows)).T

	# create a list of column names
	col_names = [f"col_{i+1}" for i in range(n_cols)]

	# create a new dataframe using the reshaped data and column names
	new_df = pd.DataFrame(data=reshaped_data, columns=col_names)
	print(new_df)
#print(uci2algebraic(board,"d4"))
df=pd.read_csv("chess_openings2moves.csv")#.head(5)

test(df)
#a=pd.DataFrame((df["moves"]))
#a=df["moves"].apply(lambda x:len(x))
#print(a.max(),a.idxmax())
#print(df.iloc[a.idxmax()])
#print(separate_moves(df,"moves"))
#df.iloc[5]
#df["moves"]=df["moves"].apply(changeNotation)
#print(df)
#newdf=pd.DataFrame({"opening_name":df["opening_name"],"moves":df["moves"]})
#newdf.to_csv("chess_openings3movestransalted.csv")



#l="abcdefgh"
#n="12345678"
#mytable = str.maketrans(l, n)
#trans_table =l.maketrans(trans_dict)
#df=df["moves"].str.translate(mytable)
#print(df)
#convertir todas las jugadas a un valor numerico en notacion uci , pero con numeros en el tablero
#ejemeplo e2e4 -> 5254
#df=pd.read_csv("games.csv")
#newdf=pd.DataFrame({"opening_name":df["opening_name"],"moves":df["moves"]})
#newdf.to_csv("chess_openings.csv")