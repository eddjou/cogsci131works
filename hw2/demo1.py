import numpy
import matplotlib.pyplot as plt
import math
def dis(s):
    ddis=0;
    for i in range(50):
        dx=numpy.random.normal(0,s,3600)
        dy=numpy.random.normal(0,s,3600)
        x=0
        y=0
        for i in range(3600):
            x=dx[i]+x
            y=dy[i]+y
        ddis+=pow(x**2+y**2,0.5)
    return ddis/50
distance=[]
fig=plt.figure()
ax=fig.add_subplot(111)
i=[-4]
distance.append(dis(10 ** i[-1]))
while i[-1]<=1:
    i.append(i[-1]+0.01)
    distance.append(dis(10 ** i[-1]))
ax.plot(i,distance)
plt.ylabel('Distance to nest')
plt.xlabel('log10(s)')
plt.show()