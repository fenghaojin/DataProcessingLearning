import numpy as np

gb_path="/home/fenghao/dataprocessing/numpy/data/GB_video_data_numbers.csv"
us_path="/home/fenghao/dataprocessing/numpy/data/US_video_data_numbers.csv"

t1=np.loadtxt(fname=gb_path,delimiter=",",dtype="float")
t2=np.loadtxt(fname=us_path,delimiter=",",dtype="float")

zeros=np.zeros((t1.shape[0],1))
ones=np.ones((t2.shape[0],1))

t1=np.hstack((zeros,t1))
t2=np.hstack((ones,t2))

t=np.vstack((t1,t2))
print(t)
