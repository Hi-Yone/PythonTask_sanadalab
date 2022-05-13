# Instructions
#
# Plot sinewave, frequency =[1,4,8,16] , Amp=1, phase = 0, baseline = 0 in each row.
    # First column: sampling rate = 5. 
    # 2nd column: sampling rate = 20
    # 3rd column: sampling rate = 100
    # NOTE: define sampling rate (=sampling frequency) first. 
    #       Then compute sampling interval. Finally, generate xdata (ranges from -1 to 1)
# Save figure as 'Task05-1_Sampling_rate_Yourname.pdf'
# Submit both your source code and figure pdf file

#%%
import numpy as np
import matplotlib.pyplot as plt

SAMPLING_RATE = [5, 20, 100]
FREQ =[1.00, 4.00, 8.00, 16.00]
AMP, PHASE, BASELINE = 1, 0, 0

x_time = [np.arange(-1.0, 1.1, 1/i) for i in SAMPLING_RATE]     # データポイントを生成

def sinewave(x_time, amp, freq, phase, baseline):
    phase_rad = phase*np.pi/180     # 位相
    omega = 2*np.pi*freq            # 角周波数
    y = amp * np.sin(omega * x_time - phase_rad) + baseline
    return y

# ---------------------------< data plot >----------------------------
fig, ax = plt.subplots(4,3,figsize=(30,30))
plt.subplots_adjust(hspace=0.5, wspace=0.8)

for k in range(4):
    for l in range(3):
        ax[k][l].set_title('Freq = ' + str(FREQ[k]))
        ax[k][l].set_xlabel('time(sec)')
        ax[k][l].grid()
        ax[k][l].plot(x_time[l], sinewave(x_time[l], AMP, FREQ[k], PHASE, BASELINE), marker='o', label = 'sampleFreq = 5.0')
        ax[k][l].legend()
# ------------------------------------------------------------------------
# %%
