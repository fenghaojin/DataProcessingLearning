import pandas as pd
from matplotlib import pyplot as plt

#print(pd.date_range(start="20240701",end="20240731",freq="H"))
#print(pd.date_range(start="20240701",periods=10,freq="M"))

df=pd.read_csv("./911.csv")

df["timeStamp"]=pd.to_datetime(df["timeStamp"])
df.set_index("timeStamp",inplace=True)
print(df.head())

count_by_month=df.resample("M").count()["title"]
print(count_by_month.head())

_x=[i.strftime("%Y%m%d") for i in count_by_month.index]
_y=count_by_month.values

fig=plt.figure(figsize=(20,8),dpi=80)
plt.plot(_x,_y)
plt.xticks(range(len(_x)),_x,rotation=45)
plt.show()
