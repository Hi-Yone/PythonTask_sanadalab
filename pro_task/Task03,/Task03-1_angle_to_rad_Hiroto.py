# Instructions
# 1) Generate data array angle=0-360, 45 step. Assume unit of this axis is degree
# 2) Convert angle to radians. NOTE: DO NOT use numpy.radians(), but code by youself
# 3) Plot radians as a function of angle
# 4) Generate data array radians = =0-2*pi, pi/4 step.

# 5) Convert radians to angle. NOTE: DO NOT use numpy.degrees(), but code by youself
# 6) Plot radians as a function of angle.
# 7) Set axes labels, ticks accordingly (refer attached pdf file)
# 8) Save figure as 'Task03-1_angle_to_rad_Yourname.pdf'
# 9) Submit both your source code and figure pdf file


#%%
import numpy as np
import matplotlib.pyplot as plt

x_angle = np.arange(0, 361, 45)
y_radians = (x_angle*np.pi)/180

x_radians = np.arange(0, 2*np.pi + 0.01, np.pi/4)
y_angle = x_radians * (180/np.pi)

# -------------------------------
plt.figure(figsize=(10,10))
ax1 = plt.subplot(1,2,1)
ax1.set_title('Convert angle to radians')
ax1.set_xlabel('angle')
ax1.set_ylabel('radians')
ax1.set_xticks(x_angle)
ax1.set_yticks(y_radians, ['0', '','$\\frac{\pi}{2}$', '', '$\pi$', '', '$\\frac{3\pi}{2}$', '', '$2\pi$'])
ax1.grid()
ax1.plot(x_angle, y_radians, color = 'b', marker = 'o')

# -------------------------------

ax2 = plt.subplot(1,2,2)
ax2.set_title('Convert radians to angle')
ax2.set_xlabel('angle')
ax2.set_ylabel('radians')
ax2.set_xticks(x_radians, x_angle)
ax2.set_yticks(y_angle, ['0', '','$\\frac{\pi}{2}$', '', '$\pi$', '', '$\\frac{3\pi}{2}$', '', '$2\pi$'])
ax2.grid()
ax2.plot(x_radians, y_angle, color = 'r', marker = 'o')

# %%
