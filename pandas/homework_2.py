import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df=pd.read_csv("./IMDB-Movie-Data.csv")

#构造全为0的数组
temp_genre_list=df["Genre"].str.split(",").to_list()
genre_list=list(set([i for j in temp_genre_list for i in j]))#[]是列表推导式
zeros_df = pd.DataFrame(np.zeros((df.shape[0], len(genre_list))), columns=genre_list)

#给电影的分类赋值
for i in range(df.shape[0]):
    zeros_df.loc[i,temp_genre_list[i]]=1

#统计结果
genre_count=zeros_df.sum(axis=0)
print(genre_count)

#排序
genre_count=genre_count.sort_values()

#画图
fig=plt.figure(figsize=(20,8),dpi=80)
_x=genre_count.index
_y=genre_count.values
plt.bar(range(len(_x)),_y)
plt.xticks(range(len(_x)),_x)
plt.grid()
plt.show()
