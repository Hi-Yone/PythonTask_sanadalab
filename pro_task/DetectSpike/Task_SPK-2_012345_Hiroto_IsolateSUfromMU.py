# Use sample program to load spikewave data.
# Convolve by gaussian to filter data
# Set different threshold (upper and lower bound) for each unit.
# Detect spike timing of all 3 units
# Superimpose all spike waveform of each unit in different color code
# Upload your program and figure pdf to GoogleClassroom

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

threshold_high = 6      # 高閾値（青）
threshold_middle = 3.5    # 中閾値（赤）
threshold_low = 1       # 小閾値（緑）

thr_lowArr = np.tile(threshold_low, len(ttime))
thr_middleArr = np.tile(threshold_middle, len(ttime))
thr_highArr = np.tile(threshold_high, len(ttime))

# =================================================================
# 関数定義
# =================================================================
'''
閾値を高い->低いへと順にピーク検出
ピーク検出したら、一旦その部分を0にする（前後数msecも0にする）
spike_waveform_filterd_tmp を走査して閾値を超えるttimeのインデックスを取得
取得したインデックスに対応するspike_waveform_filterd_tmpを0にする。
同様に閾値を下げていく
'''
def find_peak_point(xdata, ydata, threshold, extract_range):
    ydata_tmp = np.copy(ydata)
    yy_prev = np.append(ydata_tmp[0],ydata_tmp[0:len(ydata_tmp)-1] )
    peak_idx = np.where((ydata_tmp>=threshold) & (yy_prev<threshold))   # ピークポイントのインデックスを取得
    peak_x = xdata[peak_idx]                # ピークポイントのxdataを取得
    peak_y = np.tile(10, len(peak_x))       # ピークの個数分だけタイルする

    # ピークポイント±○○個で切り出す
    for ii in peak_idx[0]:
        low_idx = ii - extract_range            # 左端のインデックスを取得
        high_idx = ii + extract_range           # 右端のインデックスを取得
        ydata_tmp[low_idx : high_idx] = 0    # ピークポイントの前後を0にする

    return peak_x, peak_y, ydata_tmp, peak_idx[0]

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
# find spike timing
# =============================================================================
extract_range = 50          # カットする範囲を決める
peak_high_x, peak_high_y, ydata_high_off, peak_idx_high = find_peak_point(ttime, spike_waveform_filtered, threshold_high, extract_range)
peak_middle_x, peak_middle_y, ydata_middle_off, peak_idx_middle = find_peak_point(ttime, ydata_high_off, threshold_middle, extract_range)
peak_low_x, peak_low_y, ydata_low_off, peak_idx_low = find_peak_point(ttime, ydata_middle_off, threshold_low, extract_range)

#----------------------------
plt.close("all")
mm = 3
nn = 1
fig_ = plt.figure(figsize=(9,12))
grid = plt.GridSpec(6, 2, wspace=0.4, hspace=1.0)

# =============================================================================
# Plot spike timing (saved data)
# =============================================================================
ax1 = plt.subplot(grid[0 , :2])
ax1.plot(ttime,spk_timing_arr_0,'r-')
ax1.plot(ttime,spk_timing_arr_1,'g-')
ax1.plot(ttime,spk_timing_arr_2,'b-')


select_spk0 = np.where(spikeID == 0)
select_spk1 = np.where(spikeID == 1)
select_spk2 = np.where(spikeID == 2) 

spk_timing_y = np.ones(len(spike_timing))*1.5  

ax1.plot(spike_timing[select_spk0], spk_timing_y[select_spk0],'rv',label = 'spike #0')
ax1.plot(spike_timing[select_spk1], spk_timing_y[select_spk1],'gv',label = 'spike #1')
ax1.plot(spike_timing[select_spk2], spk_timing_y[select_spk2],'bv',label = 'spike #2')
ax1.grid()

ax1.plot([stimON, stimON], [-3, 3],'r--',label = 'STIM ON')
ax1.plot([stimOFF, stimOFF], [-3, 3],'m--',label = 'STIM OFF')
ax1.set_xlabel('time from STIM ONSET (msec)', fontsize=fsz)
ax1.set_xlim([ttime[0],ttime[len(ttime)-1]])
ax1.set_ylim([-0.1,1.6])

ax1.legend(loc='upper right', fontsize = 6)


# =============================================================================
# Plot data and stim timing
# =============================================================================
ax2 = plt.subplot(grid[1:3, :2])
ax2.plot(ttime, spike_waveform,'b-',label = 'spike waveform')

ax2.plot(ttime, spike_waveform_filtered, color = 'c', label="filtered spike waveform")
ax2.plot([stimON, stimON], [-3,15],'r--',label = 'STIM ON')
ax2.plot([stimOFF, stimOFF], [-3,15],'m--',label = 'STIM OFF')
ax2.plot(ttime, thr_middleArr, color = 'r', label="detected unit 0")
ax2.plot(ttime, thr_lowArr, color = 'g', label="detected unit 1")
ax2.plot(ttime, thr_highArr, color = 'b', label="detected unit 2")

ax2.set_ylabel('voltage(V)', fontsize=fsz)
ax2.set_xlabel('time from STIM ONSET (msec)', fontsize=fsz)
ax2.set_xlim([ttime[0],ttime[len(ttime)-1]])
ax2.set_xlim([ttime[0],ttime[len(ttime)-1]])
ax2.scatter(peak_high_x, peak_high_y, color = 'b', marker = 'x')
ax2.scatter(peak_middle_x, peak_middle_y, color = 'r', marker = 'x')
ax2.scatter(peak_low_x, peak_low_y, color = 'g', marker = 'x')

spk_timing_y = np.ones(len(spike_timing))*11  

ax2.plot(spike_timing[select_spk0], spk_timing_y[select_spk0],'rv',label = 'spike #0')
ax2.plot(spike_timing[select_spk1], spk_timing_y[select_spk1],'g^',label = 'spike #1')
ax2.plot(spike_timing[select_spk2], spk_timing_y[select_spk2],'bs',label = 'spike #2')
ax2.legend(loc='upper right', fontsize = 6)
ax2.set_yticks(np.arange(-10, 16, 2.5))

ax2.grid()

# ============================================================================= 
# Normaized time(msec) plot
# =============================================================================
ax3 = plt.subplot(grid[3: , 0])
ax3.set_title('Spike Waveform', fontsize=fsz)
ax3.set_ylabel('Voltage(V)', fontsize=fsz)
ax3.set_xlabel('normalized time (msec)', fontsize=fsz)
ax3.grid()

normalized_time = np.linspace(-0.5, 0.75, extract_range*2)

for ii in peak_idx_middle:
    low_idx = ii - extract_range+10            # 左端のインデックスを取得
    high_idx = ii + extract_range+10           # 右端のインデックスを取得
    ax3.plot(normalized_time, spike_waveform_filtered[low_idx : high_idx], color='r')

for ii in peak_idx_low:
    low_idx = ii - extract_range+10            # 左端のインデックスを取得
    high_idx = ii + extract_range+10           # 右端のインデックスを取得
    ax3.plot(normalized_time, spike_waveform_filtered[low_idx : high_idx], color='g')

for ii in peak_idx_high:
    low_idx = ii - extract_range+10            # 左端のインデックスを取得
    high_idx = ii + extract_range+10           # 右端のインデックスを取得
    ax3.plot(normalized_time, spike_waveform_filtered[low_idx : high_idx], color='b')

ax3.plot(normalized_time, np.tile(threshold_high, len(normalized_time)), color='b', linestyle='--')
ax3.plot(normalized_time, np.tile(threshold_middle, len(normalized_time)), color='r', linestyle='--')
ax3.plot(normalized_time, np.tile(threshold_low, len(normalized_time)), color='g', linestyle='--')
ax3.plot(normalized_time, np.tile(0, len(normalized_time)), color='r')

yticks = np.arange(-5, 15.1, 5)
ax3.plot(np.tile(0, len(yticks)), yticks, color='r')
ax3.set_xlim([-0.5,0.75])

# plt.tight_layout()

plt.show()
# %%
