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
condh=[]
letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in letter:
    sump=0
    newp=[]
    for j in range(shape):
        if dic[j][0] == i:
            sump+=prob[j]
    for j in range(shape):
        if dic[j][0] == i:
            newp.append(prob[j]/sump)
    condh.append(H(newp))

fig=plt.figure()
ax=fig.add_subplot(111)
ax.bar(letter,condh)
plt.show()