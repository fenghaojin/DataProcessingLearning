import pandas as pd
import numpy as np

df1=pd.DataFrame(np.ones((2,4)),index=["A","B"],columns=list('abcd'))
df2=pd.DataFrame(np.zeros((3,3)),index=["A","B","c"],columns=list('efg'))

print(df1.join(df2))
print(df2.join(df1))
