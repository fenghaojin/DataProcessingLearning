import pandas as pd
#from pymongo import MongoClient

""" client=MongoClient()
collection=client["douban"]["tv1"]
data=list(collection.find())
print(data)

df=pd.DataFrame(data)
print(df) """

df=pd.read_csv("./dogNames2.csv")
""" print(df)
print(df.info())
print(df.describe()) """

df=df.sort_values(by="Count_AnimalName")
print(df.tail(5))
print('*'*20)
print(df[:5]["Row_Labels"])
print('*'*20)
print(df.loc[[9140,1156],["Row_Labels"]])
print('*'*20)
print(df.iloc[1,:])
