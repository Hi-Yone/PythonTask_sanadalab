# Instructions
# 1) Generate time data from 0 to 20 sec, 0.05 sec step
# 2) Convert timedata to cycle based on wavelength(frequency) parameters. frequency =  = [0.1,0.2,0.4] (Hz)
# 3) Convert cycles to radians.
# 4) Plot sine waves 
# 5) Set axes labels, ticks accordingly (refer attached pdf file)
# 6) Save figure as 'Task03-7_time_to_rad2_sinewave_Yourname.pdf'
# 7) Submit both your source code and figure pdf file

#%%
import numpy as np
import matplotlib.pyplot as plt

freq = [0.1,0.2,0.4]

xdata_time = np.arange(0, 20.05, 0.05)
ydata_sine1 = np.sin(2*np.pi*freq[0] * xdata_time)
ydata_sine2 = np.sin(2*np.pi*freq[1] * xdata_time)
ydata_sine3 = np.sin(2*np.pi*freq[2] * xdata_time)

fig = plt.figure(figsize=(12,7))
plt.grid()
plt.title('Sinewave')
plt.xlabel('Time(second)', fontsize=15)
plt.ylabel('y', fontsize=15)
plt.plot(xdata_time, ydata_sine1, label = '0.1Hz')
plt.plot(xdata_time, ydata_sine2, label = '0.2Hz')
plt.plot(xdata_time, ydata_sine3, label = '0.4Hz')
plt.legend()
# %%
