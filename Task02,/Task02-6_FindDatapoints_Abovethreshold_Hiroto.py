# =============================================================================
# Task02-6, Find Datapoints above threshold
# =============================================================================
# Instruction
# 0-1) import numpy and matplotib.pyplot
# 0-2) Generate x from 0 to 10, number of data = 1000

# 1) Find data above threshold
# 1-1) Geneate sinewave , y1 = sin(x)
# 1-2) set threshold=90%from positive peak
# 1-3) find datapoints above the threshold
# 1-4) mark the found datapoints by binary (element is either 0 or 1) data array
# 1-5) plot sinewave, binary array, and threshold

# 2) Find data below threshold
# 2-1)Geneate sinewave, y1 = sin(x)
# 2-2) set threshold=-90%from negative peak
# 2-3) find datapoints below the threshold
# 2-4) mark the found datapoints by binary (element is either 0 or 1) data array
# 2-5) plot sinewave, binary array, and threshold

# 3) Find peak
# 3-1) generate following data
#      y1 = 2sin(x), y2 = 2sin(2x)
#      yy = y1 + y2 + (normal distribution noise)
# 3-2) find maximum data (set threshold at maxvalue, and do same process as (1) and (2))
# 3-3) mark by binary data array
# 3-4) plot data, binary array, and threshold

# 4) Save pdf file of the figure ("Task02-6_FindDatapoints_Abovethreshold_yourname.pdf")
# 5) Submit your source code and figure pdf

#%%
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10, 0.01)
y = np.sin(x)

max_y = max(y)
min_y = min(y)

thr_above = np.tile([max_y * 0.9], 1000)
y2 = np.where(y >= max_y * 0.9, 1, 0)

thr_below = np.tile([min_y * 0.9], 1000)
y3 = np.where(y <= min_y * 0.9, -1, 0)

y4, y5 = 2 * np.sin(x), 2 * np.sin(2*x)
yy = y4 + y5 + np.random.normal(size=1000)
max_yy = max(yy)
thr_above_noise = np.tile([max_yy], 1000)
yy_bin = np.where(yy >= max_yy, max_yy, 0)

fig = plt.figure(figsize=(7, 7))
plt.subplots_adjust(wspace=1.5, hspace=0.6)

ax1 = plt.subplot(3,2,1)
ax1.set_title('(1)Find data above threshold')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.plot(x, y, label = 'y1 = sin(x)')
ax1.plot(x, y2, label = 'selected location')
ax1.plot(x, thr_above, linestyle = 'dashed', color = 'r', label = 'threshold')
ax1.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

ax2 = plt.subplot(3,2,3)
ax2.set_title('(2)Find data below threshold')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.plot(x, y, label = 'y1 = sin(x)')
ax2.plot(x, y3, label = 'selected location')
ax2.plot(x, thr_below, linestyle = 'dashed', color = 'r', label = 'threshold')
ax2.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

ax3 = plt.subplot(3,2,5)
ax3.set_title('(3)Find data below threshold')
ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.set_ylim(-5, 5)
ax3.plot(x, yy, label = 'y1 = sin(x) + noise(normal)')
ax3.plot(x, yy_bin, label = 'selected location')
ax3.plot(x, thr_above_noise, linestyle = 'dashed', color = 'r', label = 'threshold')
ax3.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

ax4 = plt.subplot(3,2,2)
ax4.plot(np.nan, np.nan)
ax4.set_axis_off()
ax5 = plt.subplot(3,2,4)
ax5.plot(np.nan, np.nan)
ax5.set_axis_off()
ax6 = plt.subplot(3,2,6)
ax6.plot(np.nan, np.nan)
ax6.set_axis_off()


# %%

# %%
