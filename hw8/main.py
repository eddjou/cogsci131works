import numpy as np
import matplotlib.pyplot as plt

N=6
H1=[2*i+2 for i in range(50)]
H2=[2*i+1 for i in range(50)]
H3=[]
i3=0
while i3**2<=100:
    H3.append(i3**2)
    i3+=1
H4=[]
i4=0
for i in range(2,100):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        H4.append(i)
H5=[i*5 for i in range(1,21)]
H6=[i*10 for i in range(1,11)]

H=[]
H.append(H1)
H.append(H2)
H.append(H3)
H.append(H4)
H.append(H5)
H.append(H6)

NN=0
for gap in range(1,101):
    st = 1
    while st+gap<=101:
        NN+=1
        H.append([i+st for i in range(gap)])
        st+=1

def PDH(x,h):
    p=[0]*len(x)
    pp=1
    for i in range(len(x)):
        for j in range(len(h)):
            if x[i]==h[j]:
                p[i]=1/len(h)
                break
        pp*=p[i]
    if pp==1:
        return 0.0
    else:
        return pp

prior=np.zeros(N+NN)
for i in range(6):
    prior[i]=1/7
for i in range(NN):
    prior[6+i]=1/7/NN

data=[2,4,8,10]
y=np.zeros(100)
PHD=np.zeros(N+NN)
sump=0

for j in range(N+NN):
    sump += PDH(data, H[j]) * prior[j]
for i in range(N+NN):
    if sump==0:
        PHD[i]=0
    else:
        PHD[i]=PDH(data,H[i])*prior[i]/sump

for i in range(100):
    for j in range(N+NN):
        for k in range(len(H[j])):
            if i==H[j][k]:
                y[i]+=PHD[j]
                break
fig = plt.figure()
ax=fig.add_subplot(111)
#ax.plot(y,color="lightblue",linewidth=2)
plt.bar([i+1 for i in range(100)],y,width=1)
plt.show()

