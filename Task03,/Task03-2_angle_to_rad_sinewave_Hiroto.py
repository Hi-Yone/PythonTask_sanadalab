# Instructions
# 1) Generate data array angle=0-360, 45 step. Assume unit of this axis is degree
# 2) Convert angle to radians. NOTE: DO NOT use numpy.radians(), but code by youself
# 3) plot angle VS y = sin(x),   where x = radians that you obtained in (2)
# 4) plot radians VS y = sin(x), where x = radians that you obtained in (2)
# 5) Set axes labels, ticks accordingly (refer attached pdf file)
# 6) Save figure as 'Task03-2_angle_to_rad_sinewave_Yourname.pdf'
# 7) Submit both your source code and figure pdf file

#%%
import numpy as  np
import matplotlib.pyplot as plt

x_angle = np.arange(0, 361, 15) # xの角度のリストを作成
x_radians = (x_angle*np.pi) / 180   # xをラジアンに直す

y_radians = np.sin(x_radians)

fig = plt.figure()
plt.subplots_adjust(wspace=1.0, hspace=1.0)

# -----------------------------------------

ax1 = plt.subplot(2,1,1)
ax1.grid()
ax1.set_title('y=sin(x), x-axis: angle')
ax1.set_xlabel('Angle(deg)')
ax1.set_ylabel('Amplitude')
ax1.set_xticks(np.arange(0, 361, 45))
ax1.set_yticks(np.arange(-1, 1.1, 0.5))
ax1.plot(x_angle, y_radians, color = 'b', marker = 'o')

# -----------------------------------------

ax2 = plt.subplot(2,1,2)
ax2.grid()
ax2.set_title('y=sin(x), x-axis: radians')
ax2.set_xlabel('Radians(rad))')
ax2.set_ylabel('Amplitude')
ax2.set_xticks(np.arange(0, 2 * np.pi + 0.1, np.pi/4), ['0', '','$\\frac{\pi}{2}$', '', '$\pi$', '', '$\\frac{3\pi}{2}$', '', '$2\pi$'])
ax2.set_yticks(np.arange(-1, 1.1, 0.5))
ax2.plot(x_radians, y_radians, color = 'r', marker = 'o')
# %%
