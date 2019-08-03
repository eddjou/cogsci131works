import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt

def H(p):
    s=0
    if p==[]:
        return 0
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

dicc=dic.copy()
probb=prob.copy()
diccc=[]
probbb=[]
def find(N):
    for nn in range(N):
        maxx=0
        for mm in range(len(dicc)):
            if frec[maxx]<frec[mm]:
                maxx=mm
        diccc.append(dicc.pop(maxx))
        probbb.append(probb.pop(maxx))
    return diccc,probbb

loss = []
for i in range(int(shape/10)):
    inn=(i+1)*10
    idd,ipp=find(10)
    maxlen = 0
    for i in range(inn):
        if len(idd[i]) > maxlen:
            maxlen = len(idd[i])
    print(inn,"maxlen:",maxlen)
    ls = 0
    for l in range(maxlen):
        sump = 0
        newp = []
        for j in range(inn):
            if len(idd[j]) == l + 1:
                sump += ipp[j]
        for j in range(inn):
            if len(idd[j]) == l + 1:
                newp.append(ipp[j] / sump)
        ls += (l + 1) * np.log2(26) - H(newp)
    loss.append(ls/maxlen)

ll=[(i+1)*10 for i in range(int(shape/10))]
fig=plt.figure()
ax=fig.add_subplot(111)
ax.plot(ll,loss)
plt.show()
