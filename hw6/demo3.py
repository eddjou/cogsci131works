import os
import numpy
import random
import pickle
import matplotlib.pyplot as plt
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

comp=numpy.zeros((10,10))
for num1 in range(10):
    for num2 in range(num1,10):
        A = load_image_files(num1)
        B = load_image_files(num2)
        N = len(A[0])  # the total size
        assert N == DIM[0] * DIM[1]  # just check our sizes to be sure
        weights = numpy.random.normal(0, 1, size=N)
        AA = A.copy()
        BB = B.copy()
        acc = 0
        for w in range(20):
            for i in range(25):
                if (len(AA) != 0 and len(BB) != 0):
                    mark = random.randint(0, 1)
                elif (len(AA) == 0 and len(BB) == 0):
                    print("empty.")
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
                    if (not H(numpy.dot(weights, temp))):
                        weights += temp
                else:
                    if (H(numpy.dot(weights, temp))):
                        weights -= temp
            accsum = 0
            for i in range(25):
                if (len(AA) != 0 and len(BB) != 0):
                    mark = random.randint(0, 1)
                elif (len(AA) == 0 and len(BB) == 0):
                    print("empty.")
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
            acc=accsum/25
            print(acc)
        comp[num1][num2]=acc
        comp[num2][num1]=acc
fig = plt.figure()
ax = fig.add_subplot(111)
plt.imshow(comp)
plt.show()
