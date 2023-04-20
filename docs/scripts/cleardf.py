import pandas as pd
import numpy as np
def getMaxCols(df):
	tmpdf=df["moves"].apply(lambda x:len(eval(x)))
	return tmpdf.max(),tmpdf.idxmax()
def adapt_data(df,colname="moves"):
	rows=len(df)
	cols,_=getMaxCols(df)
	print(cols,_)
	matrix=[]
	cols_names=["opening_name"]+["move_"+str(i) for i in range(cols)]
	#matrix=np.empty([rows,cols],dtype="S10")
	for i in range(rows):
		moves=eval(df[colname][i])
		new_row=[df["opening_name"][i]]+moves+((cols-len(moves))*[None])
		matrix.append(new_row)
		#opening_name=df["opening_name"][i]
		#for j in range(len(moves)):
		#	if df[opening_name]=
			#matrix[i][j]=moves[j]
	return matrix,cols_names
def main():
	df=pd.read_csv("chess_openings2moves.csv")#.head(10)
	data,cols=adapt_data(df,colname="moves")
	ndf = pd.DataFrame(data, columns =cols);print(ndf) 
	ndf.to_csv("chess_openings4individualcolumns.csv")
	#print(adapt_data(df,colname="moves"))
	#print(eval(df["moves"][0]),eval(df["moves"][0])[11])
main()