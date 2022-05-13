# 1) Generate x: 0-10, 1 step
# 2) Generate x1: tile 50 times (check example08). Size of x1 must be (50, 11)
# 3) Generate y1 = x1 + normal distribution. Use either np.random.randn() or np.random.normal().
# 4) Compute mean and standard deviation of y1
#
# 5) (A) Plot x VS y1 Fig(A)
#        Superimpose y=x as line plot
# 6) (B) Plot x VS mean(y1) with errorbar=std(y1). Use plt.errorbar()
#        Superimpose y=x as line plot
# 7) Set axes labels, ticks accordingly (refer attached pdf file)
# 8) Save figure as 'Task02-1_y=x_errorbar_Yourname.pdf'
# 9) Submit both your source code and figure pdf file

#%%
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 11)
x1 = np.tile(x, (50, 1))
y1 = x1 + np.random.randn(50,11)
y1_mean = np.mean(y1, axis = 0)
y1_std = np.std(y1, axis = 0)

fig = plt.figure(figsize=(8,6))

ax1 = plt.subplot(1,2,1)
ax1.set_xticks(np.arange(0, 11))
ax1.set_yticks(np.arange(-3, 14))
ax1.set_ylim(-3, 13)
ax1.set_title('(A)')
ax1.set_xlabel('x')
ax1.set_ylabel('y')

ax1.plot(x1, y1, 'o')
ax1.plot(x, x, color = 'black', label = 'y = x')

ax1.grid()
ax1.legend()

ax2 = plt.subplot(1,2,2)
ax2.set_xticks(np.arange(0, 11))
ax2.set_yticks(np.arange(-3, 14))
ax2.set_ylim(-3, 13)
ax2.set_title('(B)')
ax2.set_xlabel('x')
ax2.set_ylabel('y')

ax2.plot(x, x, color = 'black', label = 'y = x')
ax2.errorbar(x, y1_mean, y1_std, capsize = 5, fmt = 'o', ecolor='black', markeredgecolor = "black", color = 'white', label = '$\overline{y1} ± s$')

ax2.grid()
ax2.legend(bbox_to_anchor=(1, 1), loc='upper right', borderaxespad=0, fontsize=10)







# %%