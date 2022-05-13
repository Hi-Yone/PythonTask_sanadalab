# Instruction
# 1) Generate x1=normal distribution and y1= normal distribution. Use np.random.normal or np.random.randn
# 2) Select data points within specified range, then plot selected data as red symbols. 
#    Data point outside of the range must be plotted as blue symbols.
#        (A) data inside of circle center(0,0), radius=2
#        (B) data inside of circle center(1,1), radius=2
#        (C) data below y1=x1,
#        (D) -1<=x1<=1
#        (E) -1<=y1<=1
#        (F) -1<=x1<=1  and -1<=y1<=1
# 3) Set axes labels, ticks accordingly (refer attached pdf file)
# 4) Save pdf file of the figure ("Task02-3_select_data_applied_yourname.pdf")
# 5) Submit your source code and figure pdf

#%%
import numpy as np
import matplotlib.pyplot as plt

x1 = np.random.randn(1000)
y1 = np.random.randn(1000)

x1_a = x1[np.where(x1**2 + y1**2 <= 4)]
y1_a = y1[np.where(x1**2 + y1**2 <= 4)]
x1_b = x1[np.where((x1-1)**2 + (y1 - 1)**2 <= 4)]
y1_b = y1[np.where((x1-1)**2 + (y1 - 1)**2 <= 4)]
x1_c = x1[np.where(x1 >= y1)]
y1_c = y1[np.where(x1 >= y1)]
x1_d = x1[np.where((-1 < x1) & (x1 < 1))]
y1_d = y1[np.where((-1 < x1) & (x1 < 1))]
x1_e = x1[np.where((-1 < y1) & (y1 < 1))]
y1_e = y1[np.where((-1 < y1) & (y1 < 1))]
x1_f = x1[np.where(((-1 < x1) & (x1 < 1)) & ((-1 < y1) & (y1 < 1)))]
y1_f = y1[np.where(((-1 < x1) & (x1 < 1)) & ((-1 < y1) & (y1 < 1)))]

fig = plt.figure(figsize=(8,5))

ax1 = plt.subplot(2,3,1)
ax2 = plt.subplot(2,3,2)
ax3 = plt.subplot(2,3,3)
ax4 = plt.subplot(2,3,4)
ax5 = plt.subplot(2,3,5)
ax6 = plt.subplot(2,3,6)

ax1.set_xticks(np.arange(-5.0, 5.1, 2.5))
ax1.set_yticks(np.arange(-5.0, 5.1, 2.5))
ax1.set_xlim(-5.0, 5.0)
ax1.set_ylim(-5.0, 5.0)

ax2.set_xticks(np.arange(-5.0, 5.1, 2.5))
ax2.set_yticks(np.arange(-5.0, 5.1, 2.5))
ax2.set_xlim(-5.0, 5.0)
ax2.set_ylim(-5.0, 5.0)

ax3.set_xticks(np.arange(-5.0, 5.1, 2.5))
ax3.set_yticks(np.arange(-5.0, 5.1, 2.5))
ax3.set_xlim(-5.0, 5.0)
ax3.set_ylim(-5.0, 5.0)

ax4.set_xticks(np.arange(-5.0, 5.1, 2.5))
ax4.set_yticks(np.arange(-5.0, 5.1, 2.5))
ax4.set_xlim(-5.0, 5.0)
ax4.set_ylim(-5.0, 5.0)

ax5.set_xticks(np.arange(-5.0, 5.1, 2.5))
ax5.set_yticks(np.arange(-5.0, 5.1, 2.5))
ax5.set_xlim(-5.0, 5.0)
ax5.set_ylim(-5.0, 5.0)

ax6.set_xticks(np.arange(-5.0, 5.1, 2.5))
ax6.set_yticks(np.arange(-5.0, 5.1, 2.5))
ax6.set_xlim(-5.0, 5.0)
ax6.set_ylim(-5.0, 5.0)

ax1.grid()
ax2.grid()
ax3.grid()
ax4.grid()
ax5.grid()
ax6.grid()

ax1.scatter(x1, y1, color = 'b', alpha = 0.5, zorder = 1, label = 'x1 VS y1 non-selected data')
ax3.scatter(x1, y1, color = 'b', alpha = 0.5, zorder = 1, label = 'x1 VS y1 non-selected data')
ax2.scatter(x1, y1, color = 'b', alpha = 0.5, zorder = 1, label = 'x1 VS y1 non-selected data')
ax4.scatter(x1, y1, color = 'b', alpha = 0.5, zorder = 1, label = 'x1 VS y1 non-selected data')
ax5.scatter(x1, y1, color = 'b', alpha = 0.5, zorder = 1, label = 'x1 VS y1 non-selected data')
ax6.scatter(x1, y1, color = 'b', alpha = 0.5, zorder = 1, label = 'x1 VS y1 non-selected data')

ax1.scatter(x1_a, y1_a, color = 'r', alpha = 0.5, zorder = 2)
ax2.scatter(x1_b, y1_b, color = 'r', alpha = 0.5, zorder = 2)
ax3.scatter(x1_c, y1_c, color = 'r', alpha = 0.5, zorder = 2)
ax4.scatter(x1_d, y1_d, color = 'r', alpha = 0.5, zorder = 2)
ax5.scatter(x1_e, y1_e, color = 'r', alpha = 0.5, zorder = 2)
ax6.scatter(x1_f, y1_f, color = 'r', alpha = 0.5, zorder = 2)

ax1.legend()
ax2.legend()
ax3.legend()
ax4.legend()
ax5.legend()
ax6.legend()

# %%
