#%%
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10.1, 0.1)
print(len(x))

def y1(x):
    y = x
    return y

def y2(x):
    y = y1(x) + np.random.uniform(-3, 3, 101)
    return y    

def y3(x):
    y = y1(x) + np.random.normal(0, 2, 101)
    return y

fig = plt.figure(figsize=(10,10))
plt.subplots_adjust(wspace=0.4, hspace=1.0)

ax1 = plt.subplot(2,1,1)
ax1.set_title("y=x, add uniform noise")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.grid()
plt.xticks(np.arange(0.0, 12.5, 2.5))
plt.yticks(np.arange(-5.0, 17.5, 2.5))
ax1.plot(x, y1(x), c = 'r', label = 'y = x')
ax1.plot(x, y1(x) + 3, linestyle = 'dashed', color = 'violet', label = 'y = x + 3')
ax1.plot(x, y1(x) - 3, linestyle = 'dashed', color = 'violet', label = 'y = x - 3')
ax1.scatter(x, y2(x), c = 'r', label = 'y = x + uniform_rand(-3, 3)')
ax1.legend(bbox_to_anchor = (0,1), loc = 'upper left')



ax1 = plt.subplot(2,1,2)
ax1.set_title("y=x, add normal distribution noise")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.grid()
plt.xticks(np.arange(0.0, 12.5, 2.5))
plt.yticks(np.arange(-5.0, 17.5, 2.5))
ax1.plot(x, y1(x), c = 'r', label = 'y = x')
ax1.plot(x, y1(x) + 3, linestyle = 'dashed', color = 'violet', label = 'y = x + 3')
ax1.plot(x, y1(x) - 3, linestyle = 'dashed', color = 'violet', label = 'y = x - 3')
ax1.scatter(x, y3(x), c = 'r', label = 'y = x + normal_rand(\u03bc = 0, \u03c3 = 2)')
ax1.legend(bbox_to_anchor = (0,1), loc = 'upper left')
# %%
