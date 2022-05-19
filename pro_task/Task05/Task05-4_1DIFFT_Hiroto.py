# Instructions 
# x = -5:5, sampling frequency=60Hz (>> Nyquist frequency)
# ---------------------------------------
# 1) Plot following sine waves and square waves, then convert to Frequency domain by FFT
#    Sine wave, Parameters [Amplitude, Frequency, Phase, Baseline]
#    1: sine1 ( [1, 0.2, 0, 0.5] )
#    2: sine2 ( [2, 2, 270, 0.5] ）
#    3: sine1 + sine2
#    4: sine1*sine2
#    5: Square wave1 (freq = 1Hz, n=[ 1,  3,  5,  7,  9, 11])
#    6: Sine1*Square wave1
# 2) Detect peak frequency ( peak can be multiple peaks ) and mark in the Amplitude spectrum figure
#      NOTE: DO NOT use FOR loop to detect peak frequencies. 
# 3) Print detected peak frequencies in each figures
# 4) Inverse FFT (IFFT) and plot reconstructed functions
# 5) Show difference between reconstructed functions and original data

# Save figure as 'Task05-4_1DIFFT_Yourname.pdf'
# Submit both your source code and figure pdf file

#%%
import numpy as np
import matplotlib.pyplot as plt
import math

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

# フーリエ変換
def sine_fft(y, n, dt):
    F_amp = np.fft.fft(y)                               # フーリエ変換
    F_abs = np.abs(F_amp)                               # フーリエ変換の絶対値
    F_abs_amp = (F_abs/n) * 2                           # 振幅を元の波形サイズに調整
    F_abs_amp[0] = F_abs_amp[0]/2                       # DC成分を２で割る
    shifted_F_abs_amp = np.fft.fftshift(F_abs_amp)

    freqs = np.fft.fftfreq(N, dt)                       # 時間軸を周波数に変換する
    shifted_freq = np.fft.fftshift(freqs)

    return shifted_freq, shifted_F_abs_amp, F_amp

# 逆フーリエ変換
def sine_ifft(fft_amp):
    If_amp = np.fft.ifft(fft_amp)   # 逆フーリエ変換
    If_real_amp = If_amp.real       # 実数部に変換
    return If_real_amp

# 逆フーリエ変換した波形と元の波形の差を調べる
def calc_difference(original_sine, converted_sine):
    difference = np.round([converted_sine[i] - original_sine[i] for i in range(len(original_sine))], 8)
    return difference

def find_peak_datapoints(xx,data):
    yy = data
    yy_prev = np.append( yy[0],yy[0:len(yy)-1] )
    yy_next = np.append( yy[1:len(yy)],yy[len(yy)-1])
    # get location of data which passed criteria you set.
    select_ii = np.where((yy>yy_prev) & (yy>yy_next))
    return xx[select_ii], data[select_ii], select_ii

    
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

sampling_freq = 60                              # サンプリング周波数
x_time = np.arange(-5, 5.01, 1/sampling_freq)   # データポイント生成
N = np.size(x_time)                             # データ数
dt = 1/sampling_freq                            # サンプリング間隔

PARAMETER1 = [1, 0.2, 0, 0.5]                   # Amplitude, Frequency, Phase, Baseline
PARAMETER2 = [2, 2, 270, 0.5]                   # Amplitude, Frequency, Phase, Baseline

# ---------------------< sin波を生成、フーリエ変換 >-----------------------
n_array = generate_n_array(6)                   # n = [1,3,5,7,9,11]
y0 = sinewave(x_time, *PARAMETER1)
y1 = sinewave(x_time, *PARAMETER2)
y2 = sinewave(x_time, *PARAMETER1) + sinewave(x_time, *PARAMETER2)
y3 = sinewave(x_time, *PARAMETER1) * sinewave(x_time, *PARAMETER2)
y4 = squarewave(x_time, n_array, 1, 1, 0, 0)
y5 = squarewave(x_time, n_array, 1, 1, 0, 0) + sinewave(x_time, *PARAMETER1)

# フーリエ変換
shifted_freq0, shifted_F_abs_amp0, F_amp0 = sine_fft(y0, N, dt)
shifted_freq1, shifted_F_abs_amp1, F_amp1 = sine_fft(y1, N, dt)
shifted_freq2, shifted_F_abs_amp2, F_amp2= sine_fft(y2, N, dt)
shifted_freq3, shifted_F_abs_amp3, F_amp3 = sine_fft(y3, N, dt)
shifted_freq4, shifted_F_abs_amp4, F_amp4 = sine_fft(y4, N, dt)
shifted_freq5, shifted_F_abs_amp5, F_amp5 = sine_fft(y5, N, dt)

# ピーク検出
peak_freq0, peak_amp0, idx = find_peak_datapoints(shifted_freq0, shifted_F_abs_amp0)
peak_freq1, peak_amp1, idx = find_peak_datapoints(shifted_freq1, shifted_F_abs_amp1)
peak_freq2, peak_amp2, idx = find_peak_datapoints(shifted_freq2, shifted_F_abs_amp2)
peak_freq3, peak_amp3, idx = find_peak_datapoints(shifted_freq3, shifted_F_abs_amp3)
peak_freq4, peak_amp4, idx = find_peak_datapoints(shifted_freq4, shifted_F_abs_amp4)
peak_freq5, peak_amp5, idx = find_peak_datapoints(shifted_freq5, shifted_F_abs_amp5)

# フーリエ逆変換
If_sine0 = sine_ifft(F_amp0)
If_sine1 = sine_ifft(F_amp1)
If_sine2 = sine_ifft(F_amp2)
If_sine3 = sine_ifft(F_amp3)
If_sine4 = sine_ifft(F_amp4)
If_sine5 = sine_ifft(F_amp5)

# 元波形との差を計算
y_difference0 = calc_difference(y0, If_sine0)
y_difference1 = calc_difference(y1, If_sine1)
y_difference2 = calc_difference(y2, If_sine2)
y_difference3 = calc_difference(y3, If_sine3)
y_difference4 = calc_difference(y4, If_sine4)
y_difference5 = calc_difference(y5, If_sine5)

# -----------------<データプロット(time data) >------------------
fig, ax = plt.subplots(6,4,figsize=(25,20))
fig.subplots_adjust(wspace = 0.5, hspace=0.7)

y_array = [y0, y1, y2, y3, y4, y5]
for i in range(6):
    ax[i][0].set_xlabel('time(sec)')
    ax[i][0].set_ylabel('Amp')
    ax[i][0].set_xlim(-5.5, 5.5)
    ax[i][0].grid()
    ax[i][0].plot(x_time, y_array[i], color = 'r')

ax[0][0].set_title('Sin1')
ax[1][0].set_title('Sin2')
ax[2][0].set_title('Sin1 + Sin2')
ax[3][0].set_title('Sin1 × Sin2')
ax[4][0].set_title('Square wave,  y=$\sum{\\frac{4}{n\pi} * \sin{(2\pi ft)}}$, f=1[Hz], n=[1,3,5,7,9,11]')
ax[5][0].set_title('Square wave + Sin1')

#------------------------------------------------------------
# ---------------< データプロット(フーリエ変換 frequency data) >---------------
ax[0][1].set_title('freq, Sin1')
ax[1][1].set_title('freq, Sin2')
ax[2][1].set_title('freq, Sin1+Sin2')
ax[3][1].set_title('freq, Sin1 x Sin2')
ax[4][1].set_title('freq, Square wave')
ax[5][1].set_title('freq, Square wave + Sin1')

shifted_freq_array = [shifted_freq0, shifted_freq1, shifted_freq2, shifted_freq3, shifted_freq4, shifted_freq5]
shifted_F_abs_amp_array = [shifted_F_abs_amp0, shifted_F_abs_amp1, shifted_F_abs_amp2, shifted_F_abs_amp3, shifted_F_abs_amp4, shifted_F_abs_amp5]
# 振幅スペクトルをプロット
for i in range(4):
    ax[i][1].set_xlabel('frequency(Hz)')
    ax[i][1].set_ylabel('Amp')
    ax[i][1].set_yticks(np.arange(0, 3.1, 0.5))
    ax[i][1].set_xlim(-5.0, 5.0)
    ax[i][1].set_ylim(0, 3)
    ax[i][1].grid()
    ax[i][1].plot(shifted_freq_array[i], shifted_F_abs_amp_array[i], color = 'b')
for j in range(4, 6, 1):
    ax[j][1].set_xlabel('frequency(Hz)')
    ax[j][1].set_ylabel('Amp')
    ax[j][1].set_yticks(np.arange(0, 1.1, 0.5))
    ax[j][1].set_xlim(-20, 20)
    ax[j][1].grid()
    ax[j][1].plot(shifted_freq_array[j], shifted_F_abs_amp_array[j], color = 'b')

# ピークプロット
ax[0][1].scatter(peak_freq0, peak_amp0, color = 'r', marker = 'x')
ax[1][1].scatter(peak_freq1, peak_amp1, color = 'r', marker = 'x')
ax[2][1].scatter(peak_freq2, peak_amp2, color = 'r', marker = 'x')
ax[3][1].scatter(peak_freq3, peak_amp3, color = 'r', marker = 'x')
ax[4][1].scatter(peak_freq4, peak_amp4, color = 'r', marker = 'x')
ax[5][1].scatter(peak_freq5, peak_amp5, color = 'r', marker = 'x')

# ピークの周波数を表示
str_peak_freq0 = Convert_arr2str(peak_freq0)
ax[0][1].text(1,2, 'f = ' + str_peak_freq0)
str_peak_freq1 = Convert_arr2str(peak_freq1)
ax[1][1].text(1,2, 'f = ' + str_peak_freq1)
str_peak_freq2 = Convert_arr2str(peak_freq2)
ax[2][1].text(1,2, 'f = ' + str_peak_freq2)
str_peak_freq3 = Convert_arr2str(peak_freq3)
ax[3][1].text(1,2, 'f = ' + str_peak_freq3)
str_peak_freq4 = Convert_arr2str(peak_freq4)
ax[4][1].text(4.5,0.5, 'f = ' + str_peak_freq4)
str_peak_freq5 = Convert_arr2str(peak_freq5)
ax[5][1].text(4.5, 0.5, 'f = ' + str_peak_freq5)

#  ---------------< データプロット(逆変換 time data) >---------------
If_sine_array = [If_sine0, If_sine1, If_sine2, If_sine3, If_sine4, If_sine5]
y_difference_array = [y_difference0, y_difference1, y_difference2, y_difference3, y_difference4, y_difference5]

for i in range(6):
    # 逆フーリエ変換の結果をプロット
    ax[i][2].set_title('reconstructed function')
    ax[i][2].set_xlabel('time(sec)')
    ax[i][2].set_ylabel('amplitude')
    ax[i][2].set_xlim(-5.5, 5.5)
    ax[i][2].grid()
    ax[i][2].plot(x_time, If_sine_array[i])

    # 元の波形との差をプロット 
    ax[i][3].set_title('difference')
    ax[i][3].set_xlabel('time(sec)')
    ax[i][3].set_ylabel('amplitude')
    ax[i][3].set_xlim(-5.5, 5.5)
    ax[i][3].grid()
    ax[i][3].plot(x_time, y_difference0)
#------------------------------------------------------------

# %%
