import os
import numpy
import random
import pickle
import matplotlib.pyplot as plt
DIM = (28, 28)
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
#B = load_image_files(1)
print(A)
filename = 'A.data'
f = open(filename, 'wb')
pickle.dump(A, f)
f.close()
f = open(filename, 'rb')
storedlist = pickle.load(f)
print(storedlist)
