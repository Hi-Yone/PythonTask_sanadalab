# Instructions
# 1)-1 Generate data array xdata_rad= from 0 to 4*pi, pi/8 step. Assume unit of this axis is radian
# 1)-2 plot ydata=sin(xdata_rad) as a function of xdata_rad.

# 2)-1 Convert radians to time. Assume you have 2*pi (1 cycle) in 10 second, that means frequency is 0.1(Hz),
# 2)-2 plot ydata as a function of time

# 3) Set axes labels, ticks accordingly (refer attached pdf file)
# 4) Save figure as 'Task03-5_time_to_rad_sinewave_Yourname.pdf'
# 5) Submit both your source code and figure pdf file

#%%
import numpy as np
import matplotlib.pyplot as plt

xdata_rad = np.arange(0, 4*np.pi + 0.1, np.pi/8)
xdata_time = xdata_rad * 5/np.pi
ydata_amp = np.sin(xdata_rad)

# ticks用配列
xticks_rad = np.arange(0, 4*np.pi + 0.1, np.pi/2)   # pi/2の幅の目盛り(1)
xticks_tex = ['0', '$\\frac{\pi}{2}$', '$\pi$', '$\\frac{3\pi}{2}$', '$2\pi$', '$\\frac{5\pi}{2}$', '$3\pi$', '$\\frac{7\pi}{2}$', '$4\pi$']    #(1)
xticks_time = np.arange(0, 21, 2.5)
yticks = np.arange(-1.00, 1.01, 0.25)

fig = plt.figure(figsize=(10, 12))
plt.subplots_adjust(wspace=0.2, hspace=0.4)

ax1 = plt.subplot(2,1,1)
ax1.set_title('(1) y = sin(xdata_rad)')
ax1.set_xlabel('timedata in radians', fontsize = 14)
ax1.set_ylabel('Amplitude', fontsize = 14)
ax1.set_xticks(xticks_rad, xticks_tex)
ax1.set_yticks(yticks)
ax1.grid()
ax1.plot(xdata_rad, ydata_amp, color = 'b', marker = 'o')
5
ax2 = plt.subplot(2,1,2)
ax2.set_title('(2) Convert xdata_rad to timedata, \n y=sin(timedata), wavelength = 10')
ax2.set_xlabel('timedata', fontsize = 14)
ax2.set_ylabel('Amplitude', fontsize = 14)
ax2.set_xticks(xticks_time)
ax2.set_yticks(yticks)
ax2.grid()
ax2.plot(xdata_time, ydata_amp, color = 'r', marker = 'o')

# %%
