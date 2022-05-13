#%%
import numpy as np
import matplotlib.pyplot as plt

def linear_func(x, a, b):
    y = a*x + b
    return y

def sin_func(x, a, b, c):
    y = a * np.sin(x-b) + c
    return y

x = np.arange(0, 10.5, 0.5)

fig = plt.figure(figsize=(10,10))
plt.subplots_adjust(wspace=0.4, hspace=1.0)

ax1 = plt.subplot(2,1,1)
ax1.set_title("y = a*x + b")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.grid()
plt.xticks(np.arange(0.0, 12.5, 2.5))
plt.yticks(np.arange(-5.0, 17.5, 2.5))
ax1.plot(x, linear_func(x, 1, 0), marker = 'o', c = 'r', label = 'y = x')
ax1.plot(x, linear_func(x, 2, -5), marker = 'o', c = 'b', label = 'y = 2*x - 5')
ax1.legend(bbox_to_anchor = (0,1), loc = 'upper left')

ax2 = plt.subplot(2,1,2)
ax2.set_title("y = a*x + b")
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.grid()
plt.xticks(np.arange(0.00, 13.0, 1.57))
plt.yticks(np.arange(-1.5, 3.0, 0.5))
ax2.plot(x, sin_func(x, 1, 0, 0), marker = '+', c = 'r', label = 'y = sin(x)')
ax2.plot(x, sin_func(x, 2, np.pi / 2, 0.5), marker = '+', c = 'b', label = 'y = 2*sin(x - pi/2) + 0.5')
ax2.legend(bbox_to_anchor = (1,0), loc = 'lower right')

#%%
