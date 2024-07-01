import numpy as np

def fill_array(t1):
    for i in range(t1.shape[1]):
        temp_col=t1[:,i]
        num=np.count_nonzero(np.isnan(temp_col))
        if num != 0:
            temp_not_nan_col=temp_col[temp_col == temp_col]
            temp_col[temp_col != temp_col]=temp_not_nan_col.mean()

    return t1

if __name__ == "__main__":
    t1=np.arange(12).reshape(3,4).astype("float")
    t1[1,2:]=np.nan
    print(t1)
    t1=fill_array(t1)
    print(t1)
