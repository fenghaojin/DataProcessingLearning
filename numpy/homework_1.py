import numpy as np
from matplotlib import pyplot as plt

gb_path="/home/fenghao/dataprocessing/numpy/data/GB_video_data_numbers.csv"
us_path="/home/fenghao/dataprocessing/numpy/data/US_video_data_numbers.csv"

t1=np.loadtxt(fname=gb_path,delimiter=",",dtype="int")

t1_comments=t1[:,3].copy()
print(t1_comments.shape)

""" t1=t1[t1[:,1] <= 500000]

t1_likes=t1[:,1].copy()
t1_comments=t1[:,3].copy()

t1_comments=t1_comments[t1_comments <= 5000]

d=250
num_bins=(t1_comments.max()-t1_comments.min())//d

fig=plt.figure(figsize=(20,8),dpi=80)
plt.hist(t1_comments,num_bins)

fig=plt.figure(figsize=(20,8),dpi=80)
plt.scatter(t1_likes,t1_comments)
plt.ticklabel_format(style='plain', axis='x')

plt.show()
 """
