import numpy as np
import random

a=np.array([1,2,3,4,5,6])
print(a)
print(type(a))

b=np.array(range(6))
print(b)
print(type(b))

c=np.arange(8)
print(c)
print(c.dtype)

d=np.array([1,2,3],dtype='i1')
print(d.dtype)

e=d.astype('i2')
print(d.dtype)
print(e.dtype)

f=np.array([random.random() for i in range(10)])
print(f)

g=np.round(f,2)
print(g)
