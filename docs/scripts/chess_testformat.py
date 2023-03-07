import pandas as pd
import chess
board = chess.Board()
board.push_san("Nf3")
sn=board.pop()
print(sn)
board.push_san(str(sn))

#df=pd.read_csv("games.csv")
#newdf=pd.DataFrame({"opening_name":df["opening_name"],"moves":df["moves"]})
#newdf.to_csv("chess_openings.csv")