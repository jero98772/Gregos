import chess
import pandas as pd
board = chess.Board()

#san_mainline="d4 d5 c4 c6 cxd5 e6 dxe6 fxe6 Nf3 Bb4+ Nc3 Ba5 Bf4".split()
l="abcdefgh"
n="12345678"
mytable = str.maketrans(l, n)
def changeNotation(san_mainline):
	san_mainline=san_mainline.split()
	tmp=[]
	for move in san_mainline:
	    board.push_san(move)
	for move in san_mainline:
		m=str(board.pop()).translate(mytable)
		#print(m)
		tmp.append(int(m[:4]))
	tmp.reverse()
	#print(san_mainline)
	return tmp

#print(uci2algebraic(board,"d4"))
df=pd.read_csv("chess_openings.csv")#.head(5)
#df.iloc[5]
df["moves"]=df["moves"].apply(changeNotation)
print(df)
newdf=pd.DataFrame({"opening_name":df["opening_name"],"moves":df["moves"]})
newdf.to_csv("chess_openings3movestransalted.csv")

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