# Instructions
# 1) Generate data array angle=0-360, 45 step. Assume unit of this axis is degree
# 2) Convert angle to radians. NOTE: DO NOT use numpy.radians(), but code by youself
# 3)-1 plot radians VS y = sin(x), where x = radians that you obtained in (2)
# 3)-2 plot radians VS y = sin(2x), where x = radians that you obtained in (2)
# 3)-3 plot radians VS y = sin(3x), where x = radians that you obtained in (2)
# 5) Set axes labels, ticks accordingly (refer attached pdf file)
# 6) Save figure as 'Task03-3_angle_to_rad_sinewave_Yourname.pdf'
# 7) Submit both your source code and figure pdf file


#%%
from math import radians
import numpy as np
import matplotlib.pyplot as plt

angle_arr = np.arange(0, 361, 15)   # unit : degree
radians_arr = angle_arr * np.pi / 180   # unit : radians

y1 = np.sin(radians_arr)
y2 = np.sin(radians_arr * 2)
y3 = np.sin(radians_arr * 3)

fig = plt.figure(figsize=(10, 10))
plt.subplots_adjust(hspace =0.5, wspace = 0.5)

ticks_rad = np.arange(0, 2 * np.pi + 0.1, np.pi / 4)
ticks_tex = ['0', '', '$\\frac{\pi}{2}$', '', '$\pi$', '', '$\\frac{3\pi}{2}$', '', '$2\pi$']

ax1 = plt.subplot(3,1,1)
ax1.set_title('y = sin(x)')
ax1.set_xlabel('Radians(rad)')
ax1.set_ylabel('Amplitude')
ax1.set_xticks(ticks_rad, ticks_tex)
ax1.grid()
ax1.plot(radians_arr, y1, marker = 'o', color = 'b')

ax2 = plt.subplot(3,1,2)
ax2.set_title('y = sin(2x)')
ax2.set_xlabel('Radians(rad)')
ax2.set_ylabel('Amplitude')
ax2.set_xticks(ticks_rad, ticks_tex)
ax2.grid()
ax2.plot(radians_arr, y2, marker = 'o', color = 'r')

ax3 = plt.subplot(3,1,3)
ax3.set_title('y = sin(3x)')
ax3.set_xlabel('Radians(rad)')
ax3.set_ylabel('Amplitude')
ax3.set_xticks(ticks_rad, ticks_tex)
ax3.grid()
ax3.plot(radians_arr, y3, marker = 'o', color = 'g')

# %%
