# Instructions 
# x = -5:5, sampling frequency=60Hz (>> Nyquist frequency)
# ---------------------------------------
# 1)-1 Plot sine wave
#    sine1  [Amplitude, Frequency, Phase, Baseline] =  [1, 0.2, 0, 0.5] 
# 1)-2  Convert to Frequency domain by FFT
#       Detect peak frequency ( peak can be multiple peaks ) and mark in the Amplitude spectrum figure
#     Then, print detected peak frequencies
# 1)-3 Inverse FFT (IFFT) and plot reconstructed functions
#
# 2)-1 Plot Uniform noise range from -2 to 2, 
# 2)-2 Convert to Frequency domain by FFT
# 2)-3 Inverse FFT (IFFT) and plot reconstructed functions

# 3)-1 Plot (1)sine1 and (2)noise
# 3)-2 Convert to Frequency domain by FFT
# 3)-3 IFFT

# 4)-1 Cutt off frequency, high cut freq=+/- 0.21 
# 4)-2 IFFT

# 5)-1 Cutt off frequency, high cut freq=+/- 2 
# 5)-2 IFFT

# Save figure as 'Task05-5_1DNoise_FFT_Yourname.pdf'
# Submit both your source code and figure pdf file

#%%
import numpy as np
import matplotlib.pyplot as plt
import math

# ===================================================
# 関数定義
# ===================================================
# sin波
def sinewave(timedata, amp, freq, phase, baseline):
    phase_rad = phase*np.pi/180     # 位相
    omega = 2*np.pi*freq            # 角周波数
    y = amp * np.sin(omega * timedata - phase_rad) + baseline
    return y

# フーリエ変換
def sine_fft(y, n, dt):
    freqs = np.fft.fftfreq(n, dt)                       # 時間軸を周波数に変換する
    shifted_freq = np.fft.fftshift(freqs)

    F_amp = np.fft.fft(y)                               # フーリエ変換
    F_abs = np.abs(F_amp)                               # フーリエ変換の絶対値
    F_abs_amp = (F_abs/n) * 2                           # 振幅を元の波形サイズに調整
    F_abs_amp[0] = F_abs_amp[0]/2                       # DC成分を２で割る
    shifted_F_abs_amp = np.fft.fftshift(F_abs_amp)

    return shifted_freq, shifted_F_abs_amp, F_amp

#カットオフ
def cutoff_sine_fft(y, n, dt, fc_low, fc_high):
    freqs = np.fft.fftfreq(n, dt)                       # 時間軸を周波数に変換する
    shifted_freq = np.fft.fftshift(freqs)

    Fc_amp = np.fft.fft(y)
    Fc_amp[np.abs(freqs < fc_low)] = 0                  # カットオフ（低周波成分）
    Fc_amp[np.abs(freqs > fc_high)] = 0                 # カットオフ（高周波成分）
    Fc_abs = np.abs(Fc_amp)
    Fc_abs_amp = Fc_abs / n * 2
    Fc_abs_amp[0] = Fc_abs_amp[0] / 2                   # DC成分を2で割る
    shifted_Fc_abs_amp = np.fft.fftshift(Fc_abs_amp)

    return shifted_freq, shifted_Fc_abs_amp, Fc_amp

# 逆フーリエ変換
def sine_ifft(fft_amp):
    If_amp = np.fft.ifft(fft_amp)   # 逆フーリエ変換
    If_real_amp = If_amp.real       # 実数部に変換
    return If_real_amp

def find_peak_datapoints(xx,data):
    yy = data
    yy_prev = np.append( yy[0],yy[0:len(yy)-1] )
    yy_next = np.append( yy[1:len(yy)],yy[len(yy)-1])
    # get location of data which passed criteria you set.
    select_ii = np.where((yy>yy_prev) & (yy>yy_next))
    return xx[select_ii], data[select_ii]
    
def Convert_arr2str(arr):
    flg = 0
    for ii in range(len(arr)):
        #--------------------
        # just for display, insert \n
        if flg == 0 and arr[ii]>=0:
            str_insert = '\n      '
            flg = 1
        else:
            str_insert = ''
        #--------------------
        temp="{:.2f}".format(arr[ii])
        if ii<1:
            str_arr = temp
        else:               
            str_arr = str_arr + ', ' + str_insert + temp
    return str_arr

# ===================================================
# パラメータをセット
# ===================================================
sampling_freq = 60                              # サンプリング周波数
x_time = np.arange(-5, 5.01, 1/sampling_freq)   # データポイント生成
N = np.size(x_time)                             # データ数
dt = 1/sampling_freq                            # サンプリング間隔

PARAMETER1 = [1, 0.2, 0, 0.5]                   # Amplitude, Frequency, Phase, Baseline

# 元データ
y0 = sinewave(x_time, *PARAMETER1)              # sin波
y1 = np.random.uniform(-2,2, len(x_time))       # ノイズのみ
y2 = y0 + y1                                    # sin波+ノイズ

# ===================================================
# フーリエ変換、ピーク検出、カットオフ、逆変換
# ===================================================
# フーリエ変換
shifted_freq0, shifted_F_abs_amp0, F_amp0 = sine_fft(y0, N, dt)
shifted_freq1, shifted_F_abs_amp1, F_amp1 = sine_fft(y1, N, dt)
shifted_freq2, shifted_F_abs_amp2, F_amp2 = sine_fft(y2, N, dt)

# ピークポイント
peak_freq0, peak_amp0 = find_peak_datapoints(shifted_freq0, shifted_F_abs_amp0)

# カットオフ
fc_cutoff_freq0, fc_cutoff_amp0, Fc_amp0 = cutoff_sine_fft(y2, N, dt, -0.2, 0.2)
fc_cutoff_freq1, fc_cutoff_amp1, Fc_amp1 = cutoff_sine_fft(y2, N, dt, -2, 2)

# フーリエ逆変換
If_sine0 = sine_ifft(F_amp0)
If_sine1 = sine_ifft(F_amp1)
If_sine2 = sine_ifft(F_amp2)
If_sine3 = sine_ifft(Fc_amp0)
If_sine4 = sine_ifft(Fc_amp1)


# ===================================================
# データプロット
# ===================================================
fig, ax = plt.subplots(5,3,figsize=(20,15))
fig.subplots_adjust(wspace = 0.5, hspace=0.4)
fig.suptitle('Fast Fourier Transform (FFT), cut off freq', fontsize=30)

# 元波形(sin波, ノイズ)をプロット
y_array = [y0, y1, y2]
ax[0][0].set_title('Sin1')
ax[1][0].set_title('Noise')
ax[2][0].set_title('Sin1 + Noise')

for i in range(3):
    ax[i][0].set_xlabel('time(sec)')
    ax[i][0].set_ylabel('Amp')
    ax[i][0].set_xlim(-5.5, 5.5)
    ax[i][0].grid()
    ax[i][0].plot(x_time, y_array[i], color = 'r')

ax[0][0].set_yticks(np.arange(0, 1, 1))
ax[1][0].set_yticks(np.arange(-2, 2, 1))
ax[2][0].set_yticks(np.arange(-2, 2, 1))

ax[3][0].axis("off")
ax[4][0].axis("off")

# fft結果、cuttoff をプロット
shifted_freq_array = [shifted_freq0, shifted_freq1, shifted_freq2, fc_cutoff_freq0, fc_cutoff_freq1]
shifted_F_abs_amp_array = [shifted_F_abs_amp0, shifted_F_abs_amp1, shifted_F_abs_amp2, fc_cutoff_amp0, fc_cutoff_amp1]
ax[0][1].set_title('freq, Sin1')
ax[1][1].set_title('freq, Noise')
ax[2][1].set_title('freq, Sin1 + Noise')
ax[3][1].set_title('freq, Sin1 + Noise, Cutoff(-0.21 < f < 0.21)')
ax[4][1].set_title('freq, Sin1 + Noise, Cutoff(-2.1 < f < 2.1)')

for j in range(5):
    ax[j][1].set_xlabel('frequency(Hz)')
    ax[j][1].set_ylabel('Amp')
    ax[j][1].set_xlim(-5.5, 5.5)
    ax[j][1].set_ylim(0.0, 2.0)
    ax[j][1].grid()
    ax[j][1].plot(shifted_freq_array[j], shifted_F_abs_amp_array[j], color = 'b')

# ピークプロット
ax[0][1].scatter(peak_freq0, peak_amp0, color = 'r', marker = 'x')
str_peak0 = Convert_arr2str(peak_freq0)
ax[0][1].text(1, 1.5, 'f = ' + str_peak0)

# 逆変換結果をプロット
ifft_array = [If_sine0, If_sine1, If_sine2, If_sine3, If_sine4]
ax[0][2].set_title('reconstructed function')
for i in range(5):
    ax[i][2].set_xlabel('frequency(Hz)')
    ax[i][2].set_ylabel('amplitude')
    ax[i][2].set_xlim(-5.5, 5.5)
    ax[i][2].grid()
    ax[i][2].plot(x_time, ifft_array[i])

# %%
