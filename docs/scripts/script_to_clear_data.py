import pandas as pd
df=pd.read_csv("games.csv")
newdf=pd.DataFrame({"opening_name":df["opening_name"],"moves":df["moves"]})
newdf.to_csv("chess_openings.csv")