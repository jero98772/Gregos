import pandas as pd
import time
df=pd.read_csv("chess_openings.csv")
#df=df.transpose()
#print(df.iloc[1])
#print(df["Slav Defense: Exchange Variation"])

#print(il)
#print(df.columns)
def openingAIbycolumns(move:str,turn:int,cols:list,dataframe):
	for i in cols:
		if str(df[i][turn])!=move:
			cols.remove(i)
	return cols
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
	print(len(df),"\n",df)
	df=calculate_posibles_openings("e4",0,"moves",df["opening_name"],df)
	print(len(df),"\n",df)
	time.sleep(1)
	df=calculate_posibles_openings("e5",1,"moves",df["opening_name"],df)
	print(len(df),"\n",df)
	time.sleep(1)
	df=calculate_posibles_openings("d3",2,"moves",df["opening_name"],df)
	print(len(df),"\n",df)
	time.sleep(1)
	df=calculate_posibles_openings("d6",3,"moves",df["opening_name"],df)
	print(len(df),"\n",df)
	time.sleep(1)
	df=calculate_posibles_openings("g3",4,"moves",df["opening_name"],df)
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
