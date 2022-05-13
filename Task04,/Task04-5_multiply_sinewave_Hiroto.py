# Instructions
# Generate timedata from 0 to 5, 0.01 sec step
# def sinewave(). Input argument should be timedata, amplitude, frequency, phase and baseline, return y=sine()
# Compute two sinewaves (y=sin), 
# where, frequency = [0.5,5] / [Amp, phase, baseline] = [1, 0, 0]
# Plot these sinewaves in subplot(2,1,1)
# Multiply the two sinewaves and plot in subplot(2,1,2)

# Set axes labels, ticks accordingly (refer attached pdf file)
# Save figure as 'Task04-5_multiply_sinewave_Yourname.pdf'
# Submit both your source code and figure pdf file

#%%
import numpy as np
import matplotlib.pyplot as plt

xdata_time = np.arange(0, 5.01, 0.01)
AMP = 1
FREQ = [0.5, 5]
PHASE = 0
BASELINE = 0

def sinewave(time, amp, freq, phase, baseline):
    phase_rad = phase*np.pi/180
    y = amp * np.sin(2*np.pi * freq * time - phase_rad) + baseline
    return y

fig = plt.figure(figsize=(10,10))
plt.subplots_adjust(hspace=0.5)

ax1 = plt.subplot(2, 1, 1)
ax1.set_title('y')
ax1.set_xlabel('time(sec)')
ax1.set_ylabel('y')
ax1.set_yticks(np.arange(-1.0, 1.1, 0.25))
ax1.grid()
ax1.plot(xdata_time, sinewave(xdata_time, AMP, FREQ[0], PHASE, BASELINE), label='f=0.5')
ax1.plot(xdata_time, sinewave(xdata_time, AMP, FREQ[1], PHASE, BASELINE), label='f=5.0')
ax1.legend()

ax2 = plt.subplot(2, 1, 2)
ax2.set_title('Multiply y')
ax2.set_xlabel('time(sec)')
ax2.set_ylabel('y')
ax2.set_yticks(np.arange(-1.0, 1.1, 0.25))
ax2.grid()
ax2.plot(xdata_time, sinewave(xdata_time, AMP, FREQ[0], PHASE, BASELINE) * sinewave(xdata_time, AMP, FREQ[1], PHASE, BASELINE))
ax2.legend()
# %%
