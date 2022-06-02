# Use sample program to load spikewave data.
# Convolve by gaussian to filter data
# Set different threshold (upper and lower bound) for each unit.
# Detect spike timing of all 3 units
# Superimpose all spike waveform of each unit in different color code
# Upload your program and figure pdf to GoogleClassroom

# 課題２
# マルチディテクションが起こる可能性ある（ノイズが多い）
# →最初になます（畳み込み積分）
# 切り出してピークを検出。３種類。
# 拡大すると正解データ（ピーク）があるので、正誤の確認をする。
# 完全に重なってしまっている場合はピークが一つしか検出されないが、気にしない。


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
ax1.set_xlim(80,100)

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
ax1.set_ylim([-0.1,1.6])

ax1.legend(loc='upper right', fontsize = 6)


# =============================================================================
# Plot data and stim timing
# =============================================================================
ax2 = plt.subplot(grid[1:3, :2])
ax2.plot(ttime, spike_waveform,'b-',label = 'spike waveform')

ax2.plot([stimON, stimON], [-3,15],'r--',label = 'STIM ON')
ax2.plot([stimOFF, stimOFF], [-3,15],'m--',label = 'STIM OFF')
ax2.plot(ttime, spike_waveform_filtered, color = 'c')
ax2.set_ylabel('voltage(V)', fontsize=fsz)
ax2.set_xlabel('time from STIM ONSET (msec)', fontsize=fsz)
ax2.set_xlim([ttime[0],ttime[len(ttime)-1]])


spk_timing_y = np.ones(len(spike_timing))*11  

ax2.plot(spike_timing[select_spk0], spk_timing_y[select_spk0],'rv',label = 'spike #0')
ax2.plot(spike_timing[select_spk1], spk_timing_y[select_spk1],'g^',label = 'spike #1')
ax2.plot(spike_timing[select_spk2], spk_timing_y[select_spk2],'bs',label = 'spike #2')
ax2.legend(loc='upper right', fontsize = 6)
ax2.set_xlim(80,100)

ax2.grid()

# ============================================================================= 
# 
# =============================================================================
ax3 = plt.subplot(grid[3: , 0])
ax3.set_title('Spike Waveform', fontsize=fsz)
ax3.set_ylabel('Voltage(V)', fontsize=fsz)
ax3.set_xlabel('normalized time (msec)', fontsize=fsz)
ax3.grid()
ax3.plot(xf, kfilter)
ax3.set_xlim([-0.5,0.75])

plt.tight_layout()

plt.show()
# %%
