import pandas as pd
df=pd.read_csv("openings.csv")
il=df.iloc[1]
#print(il)
#print(df.columns)
def openingAI(move:str,turn:int,cols:list,dataframe,):
	for i in cols:
		if str(df[i][turn])!=move:
			cols.remove(i)
	return cols	
cols=openingAI("e2e4",0,list(df.columns),df)
cols=openingAI("d2d4",4,cols,df)
if len(cols)==1:
	print("you played",cols[0])