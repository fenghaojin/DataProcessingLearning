import pandas as pd

df=pd.read_csv("./directory.csv")
#print(df.info())
#print(df.loc[:,"Country"])

grouped=df.groupby(by="Country")#可以遍历，可以调用聚合方法
grouped_count=grouped["Brand"].count()

""" for i,j in grouped:
    print(i)
    print("*"*30) """

#print(grouped_count)
print(grouped_count["CN"])

China_data=df[df["Country"]=="CN"]
Province_data=China_data.groupby(by="State/Province").count()["Brand"]
print(Province_data)
