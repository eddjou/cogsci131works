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
#shape=500
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

maxlen=0
for i in range(shape):
    if len(dic[i])>maxlen:
        maxlen=len(dic[i])
print(maxlen)

condh=[]
for l in range(maxlen):
    sump=0
    newp=[]
    for j in range(shape):
        if len(dic[j]) == l+1:
            sump+=prob[j]
    for j in range(shape):
        if len(dic[j]) == l+1:
            newp.append(prob[j]/sump)
    condh.append(H(newp))
ll=[i+1 for i in range(maxlen)]
fig=plt.figure()
ax=fig.add_subplot(111)
ax.bar(ll,condh)
plt.show()