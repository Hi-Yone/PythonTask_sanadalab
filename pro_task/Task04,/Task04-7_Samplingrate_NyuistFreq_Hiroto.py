# Instructions
#
# (1) Generate x from -1 to 1, total data point is 10. use np.linspace()
# plot sinewave, where Amp = 1, Frequency = 4, Phase = 0deg, Baseline = 0
# Calcurate sampling interval of x, then conve to samplingrate. 
# (2) Plot sinewave, same parameters, same x data, but total datapoint is 16.  
# (3) Plot sinewave, same parameters, same x data, but total datapoint is 41.  
# (4) Plot sinewave, same parameters, same x data, but total datapoint is 201.  
# Save figure as 'Task04-7_Samplingrate_NyuistFreq_Yourname.pdf'
# Submit both your source code and figure pdf file

#%%
import numpy as np
import matplotlib.pyplot as plt

x = [np.linspace(-1, 1, 10), np.linspace(-1, 1, 16), np.linspace(-1, 1, 41), np.linspace(-1, 1, 201)]
np.array(x)

AMP = 1
FREQ = 4
PHASE = 0
BASELINE = 0

def sinewave(time, amp, freq, phase, baseline):
    phase_rad = phase*np.pi/180     # 位相
    omega = 2*np.pi*freq            # 角周波数

    y = amp * np.sin(omega * time - phase_rad) + baseline
    return y

fig = plt.figure(figsize=(10,20))
plt.subplots_adjust(hspace=0.5)

ax1 = plt.subplot(4,1,1)
ax1.set_title('Frequency of sinewave = 4[Hz], #datapoint=10')
ax1.set_xlabel('time(sec)')
ax1.set_yticks(np.arange(-1, 1.1, 0.5))
ax1.grid()
ax1.plot(x[0], sinewave(x[0], AMP, FREQ, PHASE, BASELINE), marker = 'o', label='sampleFreq=4.5', color = 'blue')
ax1.legend()

ax2 = plt.subplot(4,1,2)
ax2.set_title('Frequency of sinewave = 4[Hz], #datapoint=16')
ax2.set_xlabel('time(sec)')
ax2.set_yticks(np.arange(-1, 1.1, 0.5))
ax2.grid()
ax2.plot(x[1], sinewave(x[1], AMP, FREQ, PHASE, BASELINE), marker = 'o', label='sampleFreq=7.5', color = 'green')
ax2.legend()

ax3 = plt.subplot(4,1,3)
ax3.set_title('Frequency of sinewave = 4[Hz], #datapoint=41')
ax3.set_xlabel('time(sec)')
ax3.set_yticks(np.arange(-1, 1.1, 0.5))
ax3.grid()
ax3.plot(x[2], sinewave(x[2], AMP, FREQ, PHASE, BASELINE), marker = 'o', label='sampleFreq=20.0', color = 'red')
ax3.legend()

ax4 = plt.subplot(4,1,4)
ax4.set_title('Frequency of sinewave = 4[Hz], #datapoint=201')
ax4.set_xlabel('time(sec)')
ax4.set_yticks(np.arange(-1, 1.1, 0.5))
ax4.grid()
ax4.plot(x[3], sinewave(x[3], AMP, FREQ, PHASE, BASELINE), marker = 'o', label='sampleFreq=100.0', color = 'lightseagreen')
ax4.legend()
# %%
