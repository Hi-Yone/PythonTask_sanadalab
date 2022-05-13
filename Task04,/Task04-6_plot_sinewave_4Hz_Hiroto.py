# Instructions
# Generate x from -1 to 1, total data point is 10. use np.linspace()
# plot sinewave, where Amp = 1, Frequency = 4, Phase = 0deg, Baseline = 0
# Save figure as 'Task04-6_plot_sinewave_4Hz_Yourname.pdf'
# Submit both your source code and figure pdf file

#%%
import numpy as np
import matplotlib.pyplot as plt

xdata = np.linspace(-1.0, 1.1, 10)
AMP = 1
FREQ = 4
PHASE = 0
BASELINE = 0

def sinewave(time, amp, freq, phase, baseline):
    phase_rad = phase*np.pi/180
    y = amp * np.sin(2*np.pi * freq * time - phase_rad) + baseline
    return y

fig = plt.figure(figsize=(10,10))
plt.subplots_adjust(hspace=0.5)

ax1 = plt.subplot(2, 1, 1)
ax1.set_xlabel('time(sec)')
ax1.set_ylabel('y')
ax1.set_yticks(np.arange(-1.0, 1.1, 0.25))
ax1.grid()
ax1.plot(xdata, sinewave(xdata, AMP, FREQ, PHASE, BASELINE))
# %%
