import os
import numpy
import random
import pickle
import matplotlib.pyplot as plt
import heapq

DIM = (28, 28)

def H(num):
    if(num<0):
        return 0
    else:
        return 1

def load_image_files(n, path="images/"):
    images = []
    for f in os.listdir(os.path.join(path, str(n))):  # read files in the path
        p = os.path.join(path, str(n), f)
        if os.path.isfile(p):
            i = numpy.loadtxt(p)
            assert i.shape == DIM
            images.append(i.flatten())
    return images

A = load_image_files(0)
B = load_image_files(1)

acc=[]
r=0
fig = plt.figure()
ax = fig.add_subplot(111)
filename = 'weights.data'
f = open(filename, 'rb')
weights = pickle.load(f)
marked=numpy.zeros(28*28)
for k in range(10,790,10):
    w2=abs(weights)
    minarr=heapq.nlargest(k, w2)
    for i in range(k):
        for j in range(28*28):
            if(w2[j]==minarr[i]):
                w2[j]=0
    accsum = 0
    AA = A.copy()
    BB = B.copy()
    for p in range(1000):
        if (len(AA) != 0 and len(BB) != 0):
            mark = random.randint(0, 1)
        elif (len(AA) == 0 and len(BB) == 0):
            print("step", r, ", empty.")
            break
        elif (len(AA) == 0):
            mark = 1
        else:
            mark = 0
        if (mark):
            k = random.randint(0, len(BB) - 1)
            temp = BB[k]
            BB.pop(k)
        else:
            k = random.randint(0, len(AA) - 1)
            temp = AA[k]
            AA.pop(k)
        if (mark):
            if (H(numpy.dot(weights, temp))):
                accsum += 1
        else:
            if (not H(numpy.dot(weights, temp))):
                accsum += 1
    acc.append(accsum / 1000)
    print(acc[r])
    r += 1
ax.plot(acc)
plt.show()
#plt.imshow(numpy.reshape(w2, (28, 28)), cmap=plt.cm.gray)
#plt.show()
"""
min=100000
for i in range(28):
    for j in range(28):
        if(marked[i][j]==0 and w2[i][j]<min):
            min=w2[i][j]
"""

