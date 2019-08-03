import matplotlib.pyplot as plt
fig = plt.figure()
ax=[None]*7
ax[0] = fig.add_subplot(241)
ax[1] = fig.add_subplot(242)
ax[2] = fig.add_subplot(243)
ax[3] = fig.add_subplot(244)
ax[4] = fig.add_subplot(245)
ax[5] = fig.add_subplot(246)
ax[6] = fig.add_subplot(247)
cluster=[1,2,3,4,5]
ax[1].plot(cluster)
k=5
ax[1].set_title("this is the"+str(k)+"main idea")
plt.show()