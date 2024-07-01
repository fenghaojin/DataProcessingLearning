import numpy as np

gb_path="/home/fenghao/dataprocessing/numpy/data/GB_video_data_numbers.csv"
us_path="/home/fenghao/dataprocessing/numpy/data/US_video_data_numbers.csv"

t1=np.loadtxt(fname=gb_path,delimiter=",",dtype="int")

print(t1[2:5,:])
print(t1[0,0])
print(t1[[0,1,2],[0,1,2]])
