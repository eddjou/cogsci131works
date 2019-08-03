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
#shape=1000
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

info=[0]*3

pp=[]
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
    pp.append(sump)
info[0]=H(prob)
for i in range(len(condh)):
    info[0]-=pp[i]*condh[i]

pp=[]
condh=[]
for i in letter:
    sump=0
    newp=[]
    for j in range(shape):
        if dic[j][-1] == i:
            sump+=prob[j]
    for j in range(shape):
        if dic[j][-1] == i:
            newp.append(prob[j]/sump)
    condh.append(H(newp))
    pp.append(sump)
info[1]=H(prob)
for i in range(len(condh)):
    info[1]-=pp[i]*condh[i]

vowel=['a','e','i','o','u']
pp=[]
condh=[]
for i in vowel:
    sump=0
    newp=[]
    for j in range(shape):
        k=0
        if (dic[j][k] in vowel) and (dic[j][k] == i):
            sump += prob[j]
        k+=1
        while k<len(dic[j]) and (dic[j][k-1] not in vowel):
            if (dic[j][k] in vowel) and (dic[j][k] == i):
                sump+=prob[j]
            k+=1
    for j in range(shape):
        k=0
        if (dic[j][k] in vowel) and (dic[j][k] == i):
            newp.append(prob[j] / sump)
        k+=1
        while k<len(dic[j]) and (dic[j][k-1] not in vowel):
            if (dic[j][k] in vowel) and (dic[j][k] == i):
                newp.append(prob[j] / sump)
            k+=1
    condh.append(H(newp))
    pp.append(sump)
sump=0
newp=[]
for j in range(shape):
    if set(dic[j])-set(vowel)==set(dic[j]):
        sump += prob[j]
for j in range(shape):
    if set(dic[j]) - set(vowel) == set(dic[j]):
        newp.append(prob[j] / sump)
condh.append(H(newp))
pp.append(sump)
print(np.sum(pp))
info[2]=H(prob)
for i in range(len(condh)):
    info[2]-=pp[i]*condh[i]
print(info)

fig=plt.figure()
ax=fig.add_subplot(111)
ax.bar(['first character','last character','first vowel'],info)
plt.show()

