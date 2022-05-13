# Instructions
# Generate timedata from 0 to 5, 0.01 sec step
# def sinewave(). Input argument should be timedata, amplitude, frequency, phase and baseline, return y=sine()
# Compute two sinewaves (y=sin), 
# where, frequency = [0.5,5] / [Amp, phase, baseline] = [1, 0, 0]
# Plot these sinewaves in subplot(2,1,1)
# Add all of the two sinewaves and plot in subplot(2,1,2)

# Set axes labels, ticks accordingly (refer attached pdf file)
# Save figure as 'Task04-3_add_sinewaves_Yourname.pdf'
# Submit both your source code and figure pdf file

#%%
import numpy as np
import matplotlib.pyplot as plt

xdata_time = np.arange(0, 5.01, 0.01)
amp = 1
freq = [0.5, 5]
phase = 0
base = 0

def sinewave(time, amp, freq, phase, baseline):
    phase_rad = phase*np.pi/180
    y = amp * np.sin(2*np.pi * freq * time - phase_rad) + baseline
    return y

fig = plt.figure(figsize=(8, 12))
plt.subplots_adjust(wspace=0.5, hspace=0.5)

ax1 = plt.subplot(2,1,1)
ax1.set_title('y')
ax1.set_xlabel('time(sec)')
ax1.set_ylabel('y')
ax1.set_yticks(np.arange(-1, 1.1, 0.25))
ax1.grid()
ax1.plot(xdata_time, sinewave(xdata_time, amp, freq[0], phase, base), label = 'f = ' + str(freq[0]))
ax1.plot(xdata_time, sinewave(xdata_time, amp, freq[1], phase, base), label = 'f = ' + str(freq[1]))
ax1.legend()

ax2 = plt.subplot(2,1,2)
ax2.set_title(r'$\Sigma$' + '(y)')
ax2.set_xlabel('time(sec)')
ax2.set_ylabel('y')
ax2.set_yticks(np.arange(-2, 2.1, 0.5))
ax2.grid()
ax2.plot(xdata_time, sinewave(xdata_time, amp, freq[0], phase, base) + sinewave(xdata_time, amp, freq[1], phase, base))
ax2.legend()
# %%
