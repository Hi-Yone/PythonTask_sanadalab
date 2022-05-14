#%%
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10.5, 0.5)

fig = plt.figure(figsize=(10,10))
plt.subplots_adjust( )

ax1 = fig.add_subplot(2,1,1)
ax1.set_title("y = x")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
plt.xticks([0, 2.5, 5.0, 7.2, 10.0])
plt.yticks([0, 2.5, 5.0, 7.2, 10.0])
ax1.plot(x, x, marker = 'o', color = 'r', label = "y = x")
ax1.legend(bbox_to_anchor = (0,1), loc = 'upper left')
ax1.grid()

ax2 = fig.add_subplot(2,1,2)
ax2.set_title("y = sin(x)")
ax2.set_xlabel("x")
ax2.set_ylabel("y")
plt.xticks([0, 1.57, 3.14, 4.71, 6.28, 7.85, 9.42, 11.0])
plt.yticks([-1.0, -0.5, 0.0, 0.5, 1.0])
ax2.plot(x, np.sin(x), marker = '+', color = 'g', label = "y = sin(x)")
ax2.legend(bbox_to_anchor = (1,1), loc = 'upper right')
ax2.grid()

# %%
