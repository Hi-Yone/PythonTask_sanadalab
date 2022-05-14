# Instructions
# 1) Generate time data from 0 to 20 sec, 0.05 sec step
# 2) Plot sine waves, where, parameter is as follows
#         y1 [Amp, freq phase, baseline] = [2, 0.1(Hz), 0(deg) ,0.5]
#         y2 [Amp, freq phase, baseline] = [1, 0.1(Hz), 90(deg),0.5]
# 5) Set axes labels, ticks accordingly (refer attached pdf file)
# 6) Save figure as 'Task04-1_plot_sinewave_Yourname.pdf'
# 7) Submit both your source code and figure pdf file

#%%
import numpy as np
import matplotlib.pyplot as plt

xdata_time = np.arange(0, 20.05, 0.05)
freq = 0.1                                          # freqency
base = 0.5                                          # base
omega = 2*np.pi * freq                              # omega
y1 = 2*np.sin(omega*xdata_time) + base              # y1
y2 = np.sin(omega*xdata_time - np.pi/2) + base      # y2
baseline = np.tile([base], len(xdata_time))         # baseline

fig = plt.figure(figsize=(7,5))
plt.grid()
plt.xlabel('time(sec)')
plt.ylabel('y')
plt.ylim(-5, 3)
plt.plot(xdata_time, y1, color = 'b', label = 'y1: Amp=2,Freq=0.1[Hz], \n phase=0[deg],base=0.5')
plt.plot(xdata_time, y2, color = 'g', label = 'y2: Amp=1,Freq=0.1[Hz], \n phase=90[deg],base=0.5')
plt.plot(xdata_time, baseline, color = 'r', linestyle = '--', label = 'Baseline')         # baseline
plt.legend()

# %%
