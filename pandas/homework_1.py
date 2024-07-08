import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df=pd.read_csv("./IMDB-Movie-Data.csv")
print(df[0:2][["Runtime (Minutes)","Rating"]])

#得到数据
runtime=df[["Runtime (Minutes)"]].values.flatten()
max_runtime=runtime.max()
min_runtime=runtime.min()
num_bin_1=(max_runtime-min_runtime)//5
rating=df[["Rating"]].values.flatten()
max_rating=rating.max()
min_rating=rating.min()
num_bin_2=[1.6]
i=1.6
while i<=max_rating:
    i += 0.5
    num_bin_2.append(i)
print(num_bin_2)

fig1=plt.figure(figsize=(20,8),dpi=80)
plt.hist(runtime,num_bin_1)
plt.xticks(range(min_runtime,max_runtime+5,5))
fig2=plt.figure(figsize=(20,8),dpi=80)
plt.hist(rating,num_bin_2)
plt.xticks(num_bin_2)
plt.show()
