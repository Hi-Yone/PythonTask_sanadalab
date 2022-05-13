# Instructions
# Generate timedata from 0 to 5, 0.01 sec step
# def sinewave(). Input argument should be timedata, amplitude, frequency, phase and baseline, return y=sine()
# Compute four sinewaves (y=sin), 
# where, frequency = [1,3,5,7](Hz( / [Amp, phase, baseline] = [1, 0(deg)), 0]
# Divide each sine waves by [1,3,5,7], respectively
# Plot these four sinewaves in subplot(2,1,1)
# Add all of the four sinewaves and plot in subplot(2,1,2)

# Set axes labels, ticks accordingly (refer attached pdf file)
# Save figure as 'Task04-4_add_sinewaves_Yourname.pdf'
# Submit both your source code and figure pdf file

#%%
import numpy as np
import matplotlib.pyplot as plt

xdata_time = np.arange(0, 5.01, 0.01)
amp = 1
freq = [1,3,5,7]
phase = 0
base = 0

def sinewave(time, amp, freq, phase, baseline):
    phase_rad = phase*np.pi/180
    y = amp * np.sin(2*np.pi * freq * time - phase_rad) + baseline
    return y

fig = plt.figure(figsize=(8, 12))
plt.subplots_adjust(wspace=0.5, hspace=0.5)
ax1 = plt.subplot(2,1,1)
ax1.set_title('y = $\\frac{\sin(2\pi ft)}{f}$')
ax1.set_xlabel('time(sec)')
ax1.set_ylabel('y')
ax1.set_yticks(np.arange(-1, 1.1, 0.25))
ax1.grid()
ax1.plot(xdata_time, sinewave(xdata_time, amp, freq[0], phase, base) / freq[0], label = 'f = ' + str(freq[0]))
ax1.plot(xdata_time, sinewave(xdata_time, amp, freq[1], phase, base) / freq[1], label = 'f = ' + str(freq[1]))
ax1.plot(xdata_time, sinewave(xdata_time, amp, freq[2], phase, base) / freq[2], label = 'f = ' + str(freq[2]))
ax1.plot(xdata_time, sinewave(xdata_time, amp, freq[3], phase, base) / freq[3], label = 'f = ' + str(freq[3]))
ax1.legend()

ax1 = plt.subplot(2,1,2)
ax1.set_title('y = ' + r'$\Sigma$' + '$\\frac{\sin(2\pi ft)}{f}$, f=[1,3,5,7]')
ax1.set_xlabel('time(sec)')
ax1.set_ylabel('y')
ax1.set_yticks(np.arange(-1, 1.1, 0.25))
ax1.grid()
sinewave_addition = 0
for i in range(4):
    sinewave_addition += sinewave(xdata_time, amp, freq[i], phase, base) / freq[i]
ax1.plot(xdata_time, sinewave_addition)
ax1.legend()

# %%
