import numpy as np
from math import log, sqrt
import scipy.stats
import pandas as pd
import random
import matplotlib.pyplot as plt
from scipy.integrate import tplquad,dblquad,quad

def log_likelihood(n1, n2, a, W):
    # this function takes a numpy array for n1, n2, and the accuracy (0/1), whether they answerd correctly
    # as well as W, the hypothesis
    # and returns the *log* likelihood of the responses, log P(acc | n1, n2, W)

    assert (len(n1) == len(n2) == len(a))

    p = 1.0 - scipy.stats.norm.cdf(0, loc=np.abs(n1 - n2),
                                   scale=W * np.sqrt(n1 ** 2 + n2 ** 2))  # the probability of answering correctly
    return np.sum(np.where(a, np.log(p), np.log(1.0 - p)))

def log_prior(W):
    if W<0:
        return -float('inf')
    else:
        return log(np.exp(-W))

def log_posterior(W):
    return log_prior(W) + log_likelihood(data['n1'], data['n2'], data['correct'], W)

data=pd.read_csv("Assignment9-data.csv")
"""
hypothesis_list=[]
temp=random.random()
hypothesis_list.append(temp)
postscore=[]
postscore.append(log_posterior(temp))
for i in range(11000):
    print("i:",i)
    w = hypothesis_list[-1]
    w_next = w + np.random.normal(0, 1)
    print(w_next,w)
    p1=log_posterior(w_next)
    p2=log_posterior(w)
    if p1>p2:
        hypothesis_list.append(w_next)
        postscore.append(p1)
    else:
        if random.random()*p2<p1:
            hypothesis_list.append(w_next)
            postscore.append(p1)
        else:
            hypothesis_list.append(w)
            postscore.append(p2)

fig = plt.figure ()
ax= fig.add_subplot(111)
ax.hist(postscore[1000:],color="grenn")
plt.ylabel('log posterior score')
plt.show()

pp=0
postsum=0
kk=0
for i in range(10000):
    postsum+=postscore[i+1000]
    if hypothesis_list[i+1000]<0.3 and hypothesis_list[i+1000]>0.2:
        kk+=1
        pp+=postscore[i+1000]
print("probability:",pp/postsum)
print("times:",kk)
"""

def f(w):
    return np.exp(log_prior(w))*np.exp(log_likelihood(data['n1'], data['n2'], data['correct'], w))

const=1/(quad(f,0,10000))
print(const)