# Language: Python (numpy, matplotlib, but no other libraries)
# 1) Use sample program to load spikewave data.
# 2) Add your own script to detect each spike, by setting threshold.
# 3) After detecting time stamp of spike timing, make histogram (PSTH, Post stimulus time
# histogram, bin = 20ms)
# 4) in (3) , convert unit of the vertical axis of the histogram to spikes/second form just number of
# spikes.
# 5) Superimpose all spike waveform


#%%
import numpy as np
import matplotlib.pyplot as plt

# ====================================
# 初期設定
# ====================================
# load array from saved .npz file
loaded_array = np.load('Task_spike_wave_data.npz')
# copy array data to varible you defined
spike_waveform = loaded_array['spkdata']  # raw spike wave data
ttime = loaded_array['timedata']  # this is x axis, time (msec)
stimON = loaded_array['stimON']   # stim onset timing (light turned on)
stimOFF = loaded_array['stimOFF'] # stimm offset timing (light turned off) 
threshold = 1.5 # Volt

fsz = 18 # define font size just for visualization

# ====================================
# プロット用データの作成
# ====================================
passed_x = ttime[np.where(spike_waveform > threshold)]      # ピーク検出 thresholdを超えるものを検出
passed_y = np.tile(2, len(passed_x))


# ピーク検出 閾値を超えた最初の点で検出
NN = len(spike_waveform)
yy = spike_waveform
yy_prev = np.append(yy[0],yy[0:len(yy)-1])
passed_idx = np.where((yy>=threshold) & (yy_prev<threshold))
# 配列が二重になっていて使いにくいので、１次元に直す
passed_idx = passed_idx[0]


# hist用データの生成
bbin = 20
xmin = ttime[0]
xmax = ttime[-1]
spike_timing = ttime[passed_idx]
bins_array = np.arange(xmin - bbin, xmax + bbin, bbin)
HIST, bins_ = np.histogram(spike_timing, bins=bins_array, range=(xmin, xmax))
bins_centr = [(bins_[i-1]+bins_[i])/2 for i in range(1, len(bins_))]
firing_rate = HIST/(bbin/1000)
print("hist_ : ", len(bins_array))


superimpose_x, superimpose_y = [], []
# ピークポイント±20で切り出す
for i in passed_idx:
    low_idx = i - 20        # 左端のインデックスを取得
    high_idx = i + 20       # 右端のインデックスを取得
    superimpose_y.append(spike_waveform[low_idx : high_idx])


# ====================================
# データプロット
# ====================================
plt.close("all")
mm = 3
nn = 1
plt.figure(figsize=(10,14))
plt.subplots_adjust(wspace=0.4, hspace=0.6)

# plot data you loaded above
ax1 = plt.subplot(mm,nn,1)
ax1.plot(ttime, spike_waveform,'b-',label = 'spike waveform')
ax1.plot([stimON, stimON], [-3, 3],'r--',label = 'STIM ON')
ax1.plot([stimOFF, stimOFF], [-3, 3],'m--',label = 'STIM OFF')
ax1.plot(ttime, np.ones(len(ttime))*threshold,'g--',label = 'threshold')
ax1.scatter(passed_x, passed_y, marker = 'x', color = 'r', label = 'Spike detected')

# set labels.
ax1.set_title('Spike wave data', fontsize=fsz)
ax1.set_ylabel('voltage(V)', fontsize=fsz)
ax1.set_xlabel('time from STIM ONSET (msec)', fontsize=fsz)
ax1.set_ylim([-3,3])
ax1.set_xlim([ttime[0],ttime[len(ttime)-1]])
ax1.legend(loc='best') # add legend
ax1.grid()

ax2 = plt.subplot(mm,nn,2)
ax2.plot([stimON, stimON], [0, 300],'r--', linewidth = 3)
ax2.plot([stimOFF, stimOFF], [0, 300],'m--', linewidth = 3)
ax2.set_yticks(np.arange(0, 301, 50))
ax2.bar(bins_centr, firing_rate, color = 'b', width = bbin)

ax2.set_title('PSTH (Post Stimulus Time Histogram', fontsize=fsz)
ax2.set_ylabel('Firing rate (spikes/sec) \n (spike number divided by 10msec)', fontsize=fsz)
ax2.set_xlabel('time from STIM ONSET (msec)', fontsize=fsz)
ax2.set_xlim([ttime[0],ttime[len(ttime)-1]])

ax3 = plt.subplot(mm,nn,3)
xticks = np.linspace(-2,2, 40)      # xデータを生成
for i in superimpose_y:
    ax3.plot(xticks, i, color = 'b')
ax3.plot([0,0],[-3,3],'r--')
ax3.plot([-3,4], np.ones(2)*threshold,'g--')

ax3.set_title('Spike Waveform', fontsize=fsz)
ax3.set_ylabel('Voltage(V)', fontsize=fsz)
ax3.set_xlabel('normalized time (msec)', fontsize=fsz)
ax3.set_xlim([-2,2])
ax3.set_ylim([-3,3])
ax3.grid()

plt.show()
# %%
