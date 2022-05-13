# Instructions
# 1) Generate data array xdata_rad= from 0 to 4*pi, 0.5*pi step. Assume unit of this axis is radian
# 2) Convert radians to time in 4 different freuency conditions frequency = [0.1,0.2,0.4, 0.8] (Hz)
# 3) Plot radians as a function of time you converted above.

# 4) Use time data you obtained (2) 
# 5) Convert timedata to cycles bsed on wavelength(frequency) parameters. frequency = [0.1,0.2,0.4, 0.8] (Hz)
# 6) Then convert to radians.
# 7) Plot radians as a function of time.

# 8) Set axes labels, ticks accordingly (refer attached pdf file)
# 9) Save figure as 'Task03-6_time_to_rad2_Yourname.pdf'
# 10) Submit both your source code and figure pdf file

#%%
import numpy as np
import matplotlib.pyplot as plt

freq = [0.1, 0.2, 0.4, 0.8]
ydata_rad = np.arange(0, 4*np.pi + 0.1, 0.5* np.pi)

omega1 = 2*np.pi * freq[0]          # 角速度ω1, f = 0.1
omega2 = 2*np.pi * freq[1]          # 角速度ω2, f = 0.2
omega3 = 2*np.pi * freq[2]          # 角速度ω3, f = 0.4
omega4 = 2*np.pi * freq[3]          # 角速度ω4, f = 0.8

xdata_time1 = ydata_rad * 1/omega1  # １ラジアン変化するのに要する時間を掛ける
xdata_time2 = ydata_rad * 1/omega2  # １ラジアン変化するのに要する時間を掛ける
xdata_time3 = ydata_rad * 1/omega3  # １ラジアン変化するのに要する時間を掛ける
xdata_time4 = ydata_rad * 1/omega4  # １ラジアン変化するのに要する時間を掛ける

ydata_rad1 = xdata_time1 * omega1
ydata_rad2 = xdata_time2 * omega2
ydata_rad3 = xdata_time3 * omega3
ydata_rad4 = xdata_time4 * omega4

# ticks用配列
xticks = np.arange(0, 20.1, 2.5)
yticks = ['0', '$\\frac{\pi}{2}$', '$\pi$', '$\\frac{3\pi}{2}$', '$2\pi$', '$\\frac{5\pi}{2}$', '$3\pi$', '$\\frac{7\pi}{2}$', '$4\pi$']

fig = plt.figure(figsize=(12,7))

ax1 = plt.subplot(1,2,1)
ax1.set_title('Convert radians to second')
ax1.set_xlabel('Time(second)',fontsize = 15)
ax1.set_ylabel('Radians(rad)',fontsize = 15)
ax1.grid()
ax1.set_xticks(xticks)
ax1.set_yticks(ydata_rad, yticks)
ax1.plot(xdata_time1, ydata_rad, marker = 'o', label = '0.1Hz')
ax1.plot(xdata_time2, ydata_rad, marker = 'o', label = '0.2Hz')
ax1.plot(xdata_time3, ydata_rad, marker = 'o', label = '0.4Hz')
ax1.plot(xdata_time4, ydata_rad, marker = 'o', label = '0.8Hz')
ax1.legend()

ax2 = plt.subplot(1,2,2)
ax2.set_title('Convert second to radians')
ax2.set_xlabel('Time(second)',fontsize = 15)
ax2.set_ylabel('Radians(rad)',fontsize = 15)
ax2.grid()
ax2.set_xticks(xticks)
ax2.set_yticks(ydata_rad, yticks)
ax2.plot(xdata_time1, ydata_rad1, marker = 'o', label = '0.1Hz')
ax2.plot(xdata_time2, ydata_rad2, marker = 'o', label = '0.2Hz')
ax2.plot(xdata_time3, ydata_rad3, marker = 'o', label = '0.4Hz')
ax2.plot(xdata_time4, ydata_rad4, marker = 'o', label = '0.8Hz')
ax2.legend()

# %%
