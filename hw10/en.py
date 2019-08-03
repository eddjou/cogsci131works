import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt

def H(p):
    s=0
    for i in p:
        s+=-i*np.log2(i)
    return s


data=pd.read_csv("Assignment10-WordFrequencies.csv",header=None)
shape=int(data.shape[0])
dic=[]
frec=[]
prob=[]
sum=0
for i in range(shape):
    dic.append(str(data.loc[i][0]))
    frec.append(float(data.loc[i][1]))
    sum+=frec[i]
for i in range(shape):
    prob.append(frec[i]/sum)

print(H(prob))