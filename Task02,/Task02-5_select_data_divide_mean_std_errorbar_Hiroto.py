# Instruction
# 1) Use code you made in Task01-7
# Task01-7  
#  (1)-1 Generate two normal distribution array, number of data is 5000.
#         x1: mean=0, sigma=1
#         y1: x1 + normal_distribution(mean=0, sigma=1)
#  (1)-2 Make histogram of each normal distribution array (range = [-6,6], bin width = 0.25)
#  (1)-3 plot the histograms on side and top of the scatter plots (bar width =0.2), alpha = 0.5
#  (1)-4 Plot 2-D scatter plots of the normal distributions, alpha = 0.5

# 2) Divide y1 data into small groups, from -4 to 4, bin=0.5 along x axis
# 3) Compute mean and standard deviation at each bin
# 4) plot errorbar, superimpose to the scatter plot
# 5) save pdf file of the figure ("Task02-5_select_data_divide_mean_std_errorbar_yourname.pdf")
# 6) submit your source code and figure pdf


#%%
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec as gridspec

x1 =np.random.normal(0, 1, 5000)
y1 = x1 + np.random.normal(0, 1, 5000)
x1_binned = np.arange(-4,4, 0.5)
meanval = np.empty(len(x1_binned))
std_val = np.empty(len(x1_binned))
for i in range(len(x1_binned)):
    temp = y1[np.where((x1 >= x1_binned[i] - 0.5) & (x1 < x1_binned[i] + 0.5))]
    meanval[i] = np.mean(temp)
    std_val[i] = np.std(temp)

fig = plt.figure(figsize=(10,10))
gs = gridspec(3,3)

ss1 = gs.new_subplotspec((0,0), colspan = 2)
ss2 = gs.new_subplotspec((1,0), rowspan = 2, colspan = 2)
ss3 = gs.new_subplotspec((1,2), rowspan = 2)

ax1 = plt.subplot(ss1)
ax2 = plt.subplot(ss2)
ax3 = plt.subplot(ss3)

plt.subplots_adjust(wspace=0.4, hspace=0.4)

ax1.set_title('histgram of x1')
ax1.set_ylabel('number of data')
ax2.set_title('scatter plot of two normal distributions')
ax2.set_xlabel('x1 data')
ax2.set_ylabel('y1 data')
ax3.set_title('histgram of y1')
ax3.set_xlabel('number of data')

ax1.set_xticks(np.arange(-5.0, 5.1, 2.5))
ax1.set_yticks(np.arange(0, 501, 250))
ax2.set_xticks(np.arange(-5.0, 5.1, 2.5))
ax2.set_yticks(np.arange(-5.0, 5.1, 2.5))
ax2.set_xlim(-5, 5)
ax3.set_yticks(np.arange(-5.0, 5.1, 2.5))
ax3.set_xticks(np.arange(0, 501, 250))
ax3.set_xlim(0, 500)

ax1.grid()
ax2.grid()
ax3.grid()

x1_hist, x1_bins = np.histogram(x1, bins = 40, range = (-6,6))
y1_hist, y1_bins = np.histogram(y1, bins = 40, range = (-6,6))
newX1 = [(x1_bins[i-1]+x1_bins[i])/2 for i in range(1, len(x1_bins))]
newY1 = [(y1_bins[i-1]+y1_bins[i])/2 for i in range(1, len(y1_bins))]

ax1.bar(newX1, x1_hist, width = 0.25, color = 'r', alpha = 0.5, label = 'x1')
ax2.scatter(x1, y1, color = 'r', alpha = 0.5, label = 'x1VSy1')
ax2.errorbar(x1_binned,  meanval, std_val, capsize = 5, fmt = 'o', ecolor='black', markeredgecolor = "black", color = 'white', markersize = 10, label = '$\overline{y1} ± s$')
ax3.barh(newY1, y1_hist, height = 0.25, color = 'r', alpha = 0.5, label = 'y1')

ax1.legend()
ax2.legend(bbox_to_anchor=(1, 1), loc='upper right', borderaxespad=0, fontsize=10)
ax3.legend()

# %%
