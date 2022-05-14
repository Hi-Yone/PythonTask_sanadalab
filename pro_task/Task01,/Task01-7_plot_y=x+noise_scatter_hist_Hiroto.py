#%%
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec as gridspec

x1 =np.random.normal(0, 1, 5000)
y1 = x1 + np.random.normal(0, 1, 5000)

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
ax3.set_yticks(np.arange(-5.0, 5.1, 2.5))
ax3.set_xticks(np.arange(0, 501, 250))
ax3.set_xlim(0, 500)

x1_hist, x1_bins = np.histogram(x1, bins = 40, range = (-6,6))
y1_hist, y1_bins = np.histogram(y1, bins = 40, range = (-6,6))
newX1 = [(x1_bins[i-1]+x1_bins[i])/2 for i in range(1, len(x1_bins))]
newY1 = [(y1_bins[i-1]+y1_bins[i])/2 for i in range(1, len(y1_bins))]

ax1.bar(newX1, x1_hist, width = 0.25, color = 'r', alpha = 0.5, label = 'x1')
ax2.scatter(x1, y1, color = 'r', alpha = 0.5, label = 'x1VSy1')
ax3.barh(newY1, y1_hist, height = 0.25, color = 'r', alpha = 0.5, label = 'y1')

ax1.legend()
ax2.legend()
ax3.legend()

ax1.grid()
ax2.grid()
ax3.grid()

# %%
