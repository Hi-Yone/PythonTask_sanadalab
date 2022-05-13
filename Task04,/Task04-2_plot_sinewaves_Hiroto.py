# Instructions
# Generate timedata from 0 to 20, 0.05 sec step
# def sinewave(). Input argument should be timedata, amplitude, frequency, phase and baseline, return y=sine()
# Plot sinewaves in following conditions.
# Basic parameter is : Amp, frequency, phase, baseline = 1, 0.1[Hz], 90[deg], 0
# 1) Vary Amplitude = [0.1, 0.5, 1, 2]
# 2) Vary Frequency = [0.1,0.2,0.4] (Hz)
# 3) Vary Phase = [0, 90, 180, 270] (deg))
# 4) Vary Baseline = [0, 0.5, 1, 2]
# Set axes labels, ticks accordingly (refer attached pdf file)
# Save figure as 'Task04-2_plot_sinewaves_Yourname.pdf'
# Submit both your source code and figure pdf file

#%%
import numpy as np
import matplotlib.pyplot as plt

xdata_time = np.arange(0, 20.01, 0.05)
amp = [0.1, 0.5, 1, 2]
freq = [0.1,0.2,0.4]
phase = [0, 90, 180, 270]
base = [0, 0.5, 1, 2]

def sinewave(time, amp, freq, phase, baseline):
    phase_rad = phase*np.pi/180
    y = amp * np.sin(2*np.pi * freq * time - phase_rad) + baseline
    return y

fig = plt.figure(figsize=(8, 12))
plt.subplots_adjust(wspace=0.5, hspace=0.5)

ax1 = plt.subplot(4,1,1)
ax1.set_title('(1) Vary Amplitude')
ax1.set_xlabel('time(sec)')
ax1.set_ylabel('y')
ax1.set_yticks(np.arange(-2, 2.1, 1))
ax1.grid()
for i in range(4):
    ax1.plot(xdata_time, sinewave(xdata_time, amp[i], 0.1, 90, 0), label = 'Amp = ' + str(amp[i]))
ax1.legend()

ax2 = plt.subplot(4,1,2)
ax2.set_title('(2) Vary Freqency')
ax2.set_xlabel('time(sec)')
ax2.set_ylabel('y')
ax2.set_yticks(np.arange(-1, 1.1, 0.5))
ax2.grid()
for i in range(3):
    ax2.plot(xdata_time, sinewave(xdata_time, 1, freq[i], 90, 0), label = 'Freq = ' + str(freq[i])) 
ax2.legend()

ax3 = plt.subplot(4,1,3)
ax3.set_title('(3) Vary Phase')
ax3.set_xlabel('time(sec)')
ax3.set_ylabel('y')
ax3.set_yticks(np.arange(-1, 1.1, 0.5))
ax3.grid()
for i in range(4):
    ax3.plot(xdata_time, sinewave(xdata_time, 1, 0.1, phase[i], 0), label = 'Phase = ' + str(phase[i]))
ax3.legend()

ax4 = plt.subplot(4,1,4)
ax4.set_title('(4) Vary Baseline')
ax4.set_xlabel('time(sec)')
ax4.set_ylabel('y')
ax4.set_yticks(np.arange(-1, 3.1, 1))
ax4.grid()
for i in range(4):
    ax4.plot(xdata_time, sinewave(xdata_time, 1, 0.1, 90, base[i]), label = 'baseline = ' + str(base[i]))
ax4.legend()
# %%
