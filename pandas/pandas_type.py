import pandas as pd
import numpy as np

""" t=np.arange(10)
t=t.reshape((2,5))
print(t) """

#df=pd.read_csv("./dogNames2.csv")

t1=pd.Series(np.arange(12))
t2=pd.DataFrame(np.arange(12).reshape((3,4)),index=list('abc'),columns=list('ABCD'))
print(t1)
print(t2)

d1={"name":["fenghao","tingting"],"age":[21,22],"tel":[198,158]}
t3=pd.DataFrame(d1)
print(t3)
print(type(t3))
