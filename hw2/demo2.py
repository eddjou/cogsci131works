import numpy
import matplotlib.pyplot as plt
import math

def E(s):
    return math.exp(0.1/s)+dis(s)**2

def dis(s):
    ddis=0;
    for i in range(10):
        dx=numpy.random.normal(0,s,3600)
        dy=numpy.random.normal(0,s,3600)
        x=0
        y=0
        for i in range(3600):
            x=dx[i]+x
            y=dy[i]+y
        ddis+=pow(x**2+y**2,0.5)
    return ddis/10

energy=[]
fig=plt.figure()
ax=fig.add_subplot(111)
i=[-2]
energy.append(math.log10(E(10 ** i[-1])))
while i[-1]<=0:
    i.append(i[-1]+0.005)
    energy.append(math.log10(E(10 ** i[-1])))
ax.plot(i,energy)
plt.ylabel('log10(Energy)')
plt.xlabel('log10(s)')
plt.show()