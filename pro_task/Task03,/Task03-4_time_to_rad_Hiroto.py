# Instructions
# 1)-1 Generate data array xdata_rad= from 0 to 4*pi, 0.5*pi step. Assume unit of this axis is radian
# 1)-2 Convert radians to time. Assume you have 2*pi (1 cycle) in 10 second, that means frequency is 0.1(Hz),
# 1)-3 Plot radians as a function of time you converted above.

# 2)-1 Use time data you obtained (1)-2 
# 2)-2 Convert time to cycles,  Frequency=0.1Hz, wavelength = 1/Frequency.
# 2)-3 Convert to radians.
# 2)-4 Plot radians as a function of time.

# 3) Set axes labels, ticks accordingly (refer attached pdf file)
# 4) Save figure as 'Task03-4_time_to_rad_Yourname.pdf'
# 5) Submit both your source code and figure pdf file

#%%
import numpy as np
import matplotlib.pyplot as plt

ydata_rad = np.arange(0, 4*np.pi + 0.1, np.pi/2)    # radians
xdata_time = ydata_rad * (5/np.pi)                  # rad -> time

ydata_angle = ydata_rad *  (180/np.pi)              # rad -> angle

ticks_tex = ['0', '$\\frac{\pi}{2}$', '$\pi$', '$\\frac{3\pi}{2}$', '$2\pi$', '$\\frac{5\pi}{2}$', '$3\pi$', '$\\frac{7\pi}{2}$', '$4\pi$']

# グラフの描画(左)
fig = plt.figure(figsize=(10, 5))

ax1 = plt.subplot(1,2,1)
ax1.set_title('(1) Convert radians o second, \n Frequency = 0.10(Cycle/sec, Hz), \n wavelength = 10.0(second),')
ax1.set_xlabel('Time(second)', fontsize = 15)
ax1.set_ylabel('Radians(rad)', fontsize = 15)
ax1.set_xticks(xdata_time)
ax1.set_yticks(ydata_rad, ticks_tex)
ax1.grid()
ax1.plot(xdata_time, ydata_rad, color = 'b', marker = 'o')

# グラフの描画(右)
ax2 = plt.subplot(1,2,2)
ax2.set_title('(2) Convert radians o angle, \n Frequency = 0.10(Cycle/sec, Hz), \n wavelength = 10.0(second),')
ax2.set_xlabel('Time(second)', fontsize = 15)
ax2.set_ylabel('Radians(rad)', fontsize = 15)
ax2.set_xticks(xdata_time)
ax2.set_yticks(ydata_angle, ticks_tex)
ax2.grid()
ax2.plot(xdata_time, ydata_angle, color = 'r', marker = 'o')
# %%
