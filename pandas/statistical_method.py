import pandas as pd
import numpy as np

df=pd.read_csv("./IMDB-Movie-Data.csv")
#print(df.info())
print(df.head(1))

#获取平均分
print("*"*20)
print(df["Rating"].mean())

#导演人数
print("*"*20)
print(len(set(df["Director"].to_list())))
print(len(df["Director"].unique()))

#演员人数
print("*"*20)
temp_actors_list=df["Actors"].str.split(",").to_list()
actors_list=[i for j in temp_actors_list for i in j]
print(len(set(actors_list)))
