import pandas as pd

df=pd.read_csv("./directory.csv")
print(df.index)
print(df.set_index("Country").index.unique())

#返回Series
grouped=df["Brand"].groupby(by=[df["Country"],df["State/Province"]]).count()
print(grouped)
print(type(grouped))

#返回DataFrame
grouped=df[["Brand"]].groupby(by=[df["Country"],df["State/Province"]]).count()
print(type(grouped))
