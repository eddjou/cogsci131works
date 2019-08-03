import numpy
import matplotlib.pyplot as plt

#x=numpy.arange(-10,10,0.1)
x=1
y=0
#y=numpy.zeros(200)
left=numpy.zeros(1000)
right=numpy.zeros(1000)
length=numpy.zeros(1000)
for i in range(1000):
    left[i] = -numpy.random.uniform()*10
    right[i]= numpy.random.uniform()*10
    length[i]=right[i]-left[i]

sumlength2 = 0
sumlength1=0
for j in range(1000):
    sumlength1+=1/length[j]
    if left[j]<x and right[j]>x:
        sumlength2+=1/length[j]
y=sumlength2/sumlength1
"""
fig=plt.figure()
ax=fig.add_subplot(111)
ax.plot(x,y)
plt.xlabel("x")
plt.ylabel("curve of probability when taking 100 regions")
plt.show()
"""
print(y)
