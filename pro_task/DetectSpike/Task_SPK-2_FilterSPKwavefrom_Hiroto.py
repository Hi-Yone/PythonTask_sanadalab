#instruction.
#1 Use sample code (convolution filtering is already coded)
#2 Add you own FFT filtering and high cut off at 10[Hz]
#3 Confirm that both results are nearly same.
#4 Submit your source code and pdf files

#%%
import numpy as np
import matplotlib.pyplot as plt

fsz = 12
# load array
loaded_array = np.load('Task_SPK-2_spike_wave_data_multi.npz')
spike_waveform = loaded_array['spkdata']
ttime = loaded_array['timedata']
stimON = loaded_array['stimON']
stimOFF = loaded_array['stimOFF']
spk_timing_arr_0 = loaded_array['spk_timing_array_0']
spk_timing_arr_1 = loaded_array['spk_timing_array_1']
spk_timing_arr_2 = loaded_array['spk_timing_array_2']
spikeID = loaded_array['spikeID']
spike_timing = loaded_array['spktiming']

threshold_low = 1

# =============================================================================
# 関数定義
# =============================================================================
def fft_filtering(xx, yy):
    dt = xx[1] - xx[0]                                  # サンプリング間隔
    NN = np.size(xx)

    freqs = np.fft.fftfreq(NN, dt)                       # 時間軸を周波数に変換する
    shifted_freq = np.fft.fftshift(freqs)

    F_abs = np.abs(np.fft.fft(yy))                                   # フーリエ変換の絶対値
    F_abs_amp = (F_abs/NN) * 2                          # 振幅を元の波形サイズに調整
    F_abs_amp[0] = F_abs_amp[0]/2                       # DC成分を２で割る
    shifted_F_abs_amp = np.fft.fftshift(F_abs_amp)

    return shifted_freq, shifted_F_abs_amp

#カットオフ
def cutoff_fft(xx, yy, fc_low, fc_high):                # サンプリング間隔
    dt = xx[1] - xx[0]                                  # サンプリング間隔
    NN = np.size(xx)

    freqs = np.fft.fftfreq(NN, dt)                      # 時間軸を周波数に変換する
    shifted_freq = np.fft.fftshift(freqs)

    Fc_amp = np.fft.fft(yy)
    Fc_amp[freqs < fc_low] = 0                  # カットオフ（低周波成分）
    Fc_amp[freqs > fc_high] = 0                 # カットオフ（高周波成分）
    Fc_abs = np.abs(Fc_amp)
    Fc_abs_amp = Fc_abs / NN * 2
    Fc_abs_amp[0] = Fc_abs_amp[0] / 2           # DC成分を2で割る
    shifted_Fc_abs_amp = np.fft.fftshift(Fc_abs_amp)

    return shifted_freq, shifted_Fc_abs_amp, Fc_amp

def myfunc_ifft(F_fft):
    F_ifft = np.fft.ifft(F_fft)     # inverse FFT
    F_ifft_real = F_ifft.real       # real
    return F_ifft_real

# ======================================================================
# フーリエ変換・カットオフ・逆変換
# ======================================================================
# フーリエ変換
shifted_freq, shifted_F_abs_amp = fft_filtering(ttime, spike_waveform)

# cutoff
fc_low = -10
fc_high = 10
shifted_freq_cutoff, shifted_Fc_abs_amp, F_cutoff = cutoff_fft(ttime, spike_waveform, fc_low, fc_high)

# Inverse fft
F_ifft_data = myfunc_ifft(F_cutoff)

# =============================================================================
# FILTER RAW DATA by convolution
# =============================================================================
incr = np.round(ttime[1]-ttime[0], decimals = 2)
t_width  = 0.1
sigma = incr*2
xf = np.arange(0,t_width+incr,incr)-t_width/2
kfilter = np.exp(-xf**2/(2*sigma**2))
kfilter = kfilter/np.sum(kfilter)
spike_waveform_filtered = np.convolve(spike_waveform,kfilter, mode='same')

# =============================================================================
# data plot
# =============================================================================
plt.close("all")
fig_ = plt.figure(figsize=(8,10))
plt.subplots_adjust(wspace=0.4, hspace=0.6)

lowNum = 4
fsz = 13

ax1 = plt.subplot(lowNum,1,1)
ax1.plot(ttime,spike_waveform)
ax1.set_xlabel('time(msec)', fontsize = fsz)
ax1.set_title('Original spike waveform', fontsize = fsz)
ax1.set_xlim([0,10])

ax2 = plt.subplot(lowNum,1,2)
ax2.plot(shifted_freq,shifted_F_abs_amp)
ax2.set_xlabel('Frequency[Hz]', fontsize = fsz)
ax2.set_title('Frequency spectrum of Original spike waveform', fontsize = fsz)

ax3 = plt.subplot(lowNum,1,3)
ax2.set_xlabel('Frequency[Hz]', fontsize = fsz)
ax2.set_title('Frequency spectrum, High cut-off at 10 Hz', fontsize = fsz)
ax3.plot(shifted_freq_cutoff, shifted_Fc_abs_amp, color = 'r',)

ax4 = plt.subplot(lowNum,1,4)
ax4.plot(ttime, F_ifft_data, color = 'r', label='ifft')
ax4.plot(ttime,spike_waveform_filtered, '--', color = 'g', label='convolution')
ax4.set_xlabel('time(msec)', fontsize = fsz)
ax4.set_title('Inversed from filtered frequency spectrum', fontsize = fsz)
ax4.set_xlim([0,10])
ax4.legend()

# %%
