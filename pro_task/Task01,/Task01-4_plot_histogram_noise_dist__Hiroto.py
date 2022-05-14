#%%
from cgitb import small
from matplotlib import markers
from matplotlib.font_manager import findSystemFonts
import numpy as np
import matplotlib.pyplot as plt

x1 = np.random.normal(0, 2, 5000)
x2 = np.random.uniform(-3, 3, 5000)

fig = plt.figure(figsize=(12, 8))
plt.subplots_adjust(wspace=0.4, hspace=1.0)

ax1 = plt.subplot(3,2,1)
ax1.set_title("(A) Histogram of x1 and x2, plt.hist, \u03B1 = 1", fontsize = 9)
ax1.set_xlabel("x")
ax1.set_ylabel("number of data")
plt.xticks(np.arange(-10, 11))
plt.yticks(np.arange(0, 751, 250))
plt.ylim(0, 750)
ax1.hist(x1, bins = 40, range = [-10, 10], alpha = 1, color = 'b', label="x1 = normal(\u03BC = 0, \u03C3 = 2), bin = 40")
ax1.hist(x2, bins = 40, range = [-10, 10], alpha = 1, color = 'r', label="x2 = uniform(-3,3), bin = 40")
ax1.legend(bbox_to_anchor = (1,1), loc = 'upper right', fontsize = 5)

ax2 = plt.subplot(3,2,3)
ax2.set_title("(B) Histogram of x1 and x2, plt.hist, \u03B1 = 0.5", fontsize = 9)
ax2.set_xlabel("x")
ax2.set_ylabel("number of data")
plt.xticks(np.arange(-10, 11))
plt.yticks(np.arange(0, 751, 250))
plt.ylim(0, 750)
ax2.hist(x1, bins = 40, range = [-10, 10], alpha = 0.5, color = 'b', label="x1 = normal(\u03BC = 0, \u03C3 = 2), bin = 40, \u03B1 = 0.5")
ax2.hist(x2, bins = 40, range = [-10, 10], alpha = 0.5, color = 'r', label="x2 = uniform(-3,3), bin = 40, \u03B1 = 0.5")
ax2.legend(bbox_to_anchor = (1,1), loc = 'upper right', fontsize = 5)

ax3 = plt.subplot(3,2,5)
ax3.set_title("(C) Histogram of x1 and x2, plt.hist, histtype = step", fontsize = 9)
ax3.set_xlabel("x")
ax3.set_ylabel("number of data")
plt.xticks(np.arange(-10, 11))
plt.yticks(np.arange(0, 751, 250))
plt.ylim(0, 750)
ax3.hist(x1, bins = 40, range = [-10, 10], histtype = 'step', color = 'b', lw=5, label="x1 = normal(\u03BC = 0, \u03C3 = 2), bin = 40, type = step")
ax3.hist(x2, bins = 40, range = [-10, 10], histtype = 'step', color = 'r', lw=5, label="x2 = uniform(-3,3), bin = 40, type = step")
ax3.legend(bbox_to_anchor = (1,1), loc = 'upper right', fontsize = 5)

ax4 = plt.subplot(3,2,2)
ax4.set_title("(D) Histogram of x1 and x2,\n plt.bar(numpy.histogram), bin = 0.5, barwidth = 0.5", fontsize = 9)
ax4.set_xlabel("x")
ax4.set_ylabel("number of data")
plt.xticks(np.arange(-10, 11))
plt.yticks(np.arange(0, 751, 250))
plt.ylim(0, 750)
x1_hist, x1_bins = np.histogram(x1, bins = 40, range = (-10, 10))
x2_hist, x2_bins = np.histogram(x2, bins = 40, range = (-10, 10))
newX1 = [(x1_bins[i-1]+x1_bins[i])/2 for i in range(1, len(x1_bins))]
newX2 = [(x2_bins[i-1]+x2_bins[i])/2 for i in range(1, len(x2_bins))]
ax4.bar(newX1, x1_hist, color = 'b', label="x1 = normal(\u03BC = 0, \u03C3 = 2), plt.bar(numpy.histgram)")
ax4.bar(newX2, x2_hist, color = 'r', label="x2 = uniform(-3, 3), plt.bar(numpy.histgram)")
ax4.legend(bbox_to_anchor = (1,1), loc = 'upper right', fontsize = 5)

ax5 = plt.subplot(3,2,4)
ax5.set_title("(E) Histogram of x1\n comparison between plt.hist and plt.plot(numpy.histgram)", fontsize = 9)
ax5.set_xlabel("x")
ax5.set_ylabel("number of data")
plt.xticks(np.arange(-10, 11))
plt.yticks(np.arange(0, 751, 250))
plt.ylim(0, 750)
ax5.hist(x1, bins = 40, range = [-10, 10], alpha = 0.5, color = 'b', label="(A) x1 = normal(\u03BC = 0, \u03C3 = 2), bin = 40, \u03B1 = 0.5")
ax5.plot(newX1, x1_hist, marker='.', color='b', label="(D) x1 = normal(\u03BC = 0, \u03C3 = 2), plt.bar(numpy.histgram)")
ax5.legend(bbox_to_anchor = (1,1), loc = 'upper right', fontsize = 5)

ax6 = plt.subplot(3,2,6)
ax6.set_title("(F) Histogram of x2\n comparison between plt.hist and plt.plot(numpy.histogram)", fontsize = 9)
ax6.set_xlabel("x")
ax6.set_ylabel("number of data")
plt.xticks(np.arange(-10, 11))
plt.yticks(np.arange(0, 751, 250))
plt.ylim(0, 750)
ax6.hist(x2, bins = 40, range = [-10, 10], alpha = 0.5, color = 'r', label="x2 = uniform(-3,3), bin = 40, \u03B1 = 0.5")
ax6.plot(newX2, x2_hist, marker='.', color='r', label="x2 = uniform(-3, 3), plt.bar(numpy.histgram)")
ax6.legend(bbox_to_anchor = (1,1), loc = 'upper right', fontsize = 6)

# %%

# %%