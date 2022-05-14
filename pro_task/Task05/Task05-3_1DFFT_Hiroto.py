# Instructions 
# x = -5:5, sampling frequency=60Hz (>> Nyquist frequency)
# ---------------------------------------
# 1) Plot following sine waves and square waves, then convert to Frequency domain by FFT
#    Sine wave, Parameters [Amplitude, Frequency, Phase, Baseline]
#    1: sine1 ( [1, 0.2, 0, 0.5] )
#    2: sine2 ( [2, 2, 270, 0]
#    3: sine1 + sine2
#    4: sine1*sine2
#    5: Square wave1 (freq = 1Hz, n=[ 1,  3,  5,  7,  9, 11])
#    6: Sine1*Square wave1

# 2) Detect peak frequency ( peak can be multiple peaks ) and mark in the Amplitude spectrum figure
#      NOTE: DO NOT use FOR loop to detect peak frequencies. 
# 3) Print detected peak frequencies in each figures
# Save figure as 'Task05-3_1DFFT_Yourname.pdf'
# Submit both your source code and figure pdf file


#%%
import numpy as np
import matplotlib.pyplot as plt

sampling_freq = 60                              # サンプリング周波数
x_time = np.arange(-5, 5.01, 1/sampling_freq)      # データポイント生成
N = len(x_time)                                 # データ数
dt = 1/sampling_freq                            # サンプリング間隔
                     
PARAMETER1 = [1, 0.2, 0, 0.5]                   # Amplitude, Frequency, Phase, Baseline
PARAMETER2 = [2, 2, 270, 0]                     # Amplitude, Frequency, Phase, Baseline

# 指定されたサイズの配列を生成
def generate_n_array(size):
    arr = [2*i - 1 for i in range(1, size+1)]   # 要素の値は1以上の奇数
    return arr

# sin波
def sinewave(timedata, amp, freq, phase, baseline):
    phase_rad = phase*np.pi/180     # 位相
    omega = 2*np.pi*freq            # 角周波数
    y = amp * np.sin(omega * timedata - phase_rad) + baseline
    return y

# 矩形波
def squarewave(timedata, n_array, amp, freq, phase, baseline):
    y = 0
    for i in range(len(n_array)):
        y += 4/(n_array[i]*np.pi) * sinewave(timedata, amp, freq*n_array[i], phase, baseline)     # sin波の合算
    return y

def sine_fft(y, n, dt):
    F_abs = np.abs(np.fft.fft(y))                       # フーリエ変換の絶対値
    F_abs_amp = F_abs / n * 2                           # 振幅を元の波形に調整
    F_abs_amp[0] = F_abs_amp[0]/2                       # 
    shifted_F_abs_amp = np.fft.fftshift(F_abs_amp)

    freqs = np.fft.fftfreq(N, dt)
    shifted_freq = np.fft.fftshift(freqs)

    return shifted_freq, shifted_F_abs_amp

# -----------------< data plot(time data) >------------------
n_array = generate_n_array(6)

fig, ax = plt.subplots(6,2,figsize=(15,20))
plt.subplots_adjust(hspace=1.2)

y0 = sinewave(x_time, *PARAMETER1)
ax[0][0].set_title('Sin1')
ax[0][0].set_xlabel('time(sec)')
ax[0][0].set_ylabel('Amp')
ax[0][0].set_xlim(-5.5, 5.5)
ax[0][0].grid()
ax[0][0].plot(x_time, y0, color = 'r')

y1 = sinewave(x_time, *PARAMETER2)
ax[1][0].set_title('Sin2')
ax[1][0].set_xlabel('time(sec)')
ax[1][0].set_ylabel('Amp')
ax[1][0].set_xlim(-5.5, 5.5)
ax[1][0].grid()
ax[1][0].plot(x_time, y1, color = 'r')

y2 = sinewave(x_time, *PARAMETER1) + sinewave(x_time, *PARAMETER2)
ax[2][0].set_title('Sin1 + Sin2')
ax[2][0].set_xlabel('time(sec)')
ax[2][0].set_ylabel('Amp')
ax[2][0].set_xlim(-5.5, 5.5)
ax[2][0].grid()
ax[2][0].plot(x_time, y2, color = 'r')

y3 = sinewave(x_time, *PARAMETER1) * sinewave(x_time, *PARAMETER2)
ax[3][0].set_title('Sin1 × Sin2')
ax[3][0].set_xlabel('time(sec)')
ax[3][0].set_ylabel('Amp')
ax[3][0].set_xlim(-5.5, 5.5)
ax[3][0].grid()
ax[3][0].plot(x_time, y3, color = 'r')

y4 = squarewave(x_time, n_array, 1, 1, 0, 0)
ax[4][0].set_title('Square wave,  y=$\sum{\\frac{4}{n\pi} * \sin{(2\pi ft)}}$, f=1[Hz], n=[1,3,5,7,9,11]')
ax[4][0].set_xlabel('time(sec)')
ax[4][0].set_ylabel('Amp')
ax[4][0].set_xlim(-5.5, 5.5)
ax[4][0].grid()
ax[4][0].plot(x_time, y4, color = 'r')

y5 = squarewave(x_time, n_array, 1, 1, 0, 0) + sinewave(x_time, *PARAMETER1)
ax[5][0].set_title('Square wave + Sin1')
ax[5][0].set_xlabel('time(sec)')
ax[5][0].set_ylabel('Amp')
ax[5][0].set_xlim(-5.5, 5.5)
ax[5][0].grid()
ax[5][0].plot(x_time, y5, color = 'r')

#------------------------------------------------------------
# ---------------< data plot(frequency data) >---------------
shifted_freq, shifted_F_abs_amp = sine_fft(y0, N, dt)
ax[0][1].set_title('Sin1')
ax[0][1].set_xlabel('time(sec)')
ax[0][1].set_ylabel('Amp')
ax[0][1].set_yticks(np.arange(0, 3.1, 1))
ax[0][1].set_xlim(-5.5, 5.5)
ax[0][1].set_ylim(0, 3)
ax[0][1].grid()
ax[0][1].plot(shifted_freq, shifted_F_abs_amp, color = 'b')

shifted_freqa, shifted_F_abs_ampa = sine_fft(y1, N, dt)
ax[1][1].set_title('Sin1')
ax[1][1].set_xlabel('time(sec)')
ax[1][1].set_ylabel('Amp')
ax[1][1].set_yticks(np.arange(0, 3.1, 1))
ax[1][1].set_xlim(-5.5, 5.5)
ax[1][1].set_ylim(0, 3)
ax[1][1].grid()
ax[1][1].plot(shifted_freq, shifted_F_abs_amp, color = 'b')

shifted_freq, shifted_F_abs_amp = sine_fft(y2, N, dt)
ax[2][1].set_title('Sin1')
ax[2][1].set_xlabel('time(sec)')
ax[2][1].set_ylabel('Amp')
ax[2][1].set_yticks(np.arange(0, 3.1, 1))
ax[2][1].set_xlim(-5.5, 5.5)
ax[2][1].set_ylim(0, 3)
ax[2][1].grid()
ax[2][1].plot(shifted_freq, shifted_F_abs_amp, color = 'b')

shifted_freq, shifted_F_abs_amp = sine_fft(y3, N, dt)
ax[3][1].set_title('Sin1')
ax[3][1].set_xlabel('time(sec)')
ax[3][1].set_ylabel('Amp')
ax[3][1].set_yticks(np.arange(0, 3.1, 1))
ax[3][1].set_xlim(-5.5, 5.5)
ax[3][1].set_ylim(0, 3)
ax[3][1].grid()
ax[3][1].plot(shifted_freq, shifted_F_abs_amp, color = 'b')

shifted_freq, shifted_F_abs_amp = sine_fft(y4, N, dt)
ax[4][1].set_title('Sin1')
ax[4][1].set_xlabel('time(sec)')
ax[4][1].set_ylabel('Amp')
ax[4][1].set_yticks(np.arange(0, 3.1, 1))
ax[4][1].set_xlim(-5.5, 5.5)
ax[4][1].set_ylim(0, 3)
ax[4][1].grid()
ax[4][1].plot(shifted_freq, shifted_F_abs_amp, color = 'b')

shifted_freq, shifted_F_abs_amp = sine_fft(y5, N, dt)
ax[5][1].set_title('Sin1')
ax[5][1].set_xlabel('time(sec)')
ax[5][1].set_ylabel('Amp')
ax[5][1].set_yticks(np.arange(0, 3.1, 1))
ax[5][1].set_xlim(-5.5, 5.5)
ax[5][1].set_ylim(0, 3)
ax[5][1].grid()
ax[5][1].plot(shifted_freq, shifted_F_abs_amp, color = 'b')

#------------------------------------------------------------

# %%
