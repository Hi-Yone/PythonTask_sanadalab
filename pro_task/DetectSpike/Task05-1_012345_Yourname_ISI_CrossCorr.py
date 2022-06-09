# cross collilation を検出する
# ISIも自分で検出する。

# ax3は元波形の相互相関の計算結果
# ax2は元波形とシャッフル波形の相互相関

#%%
import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# load Data
# =============================================================================
loaded_array = np.load('Task05_spike_wave_data_multi.npz')
spike_waveform = loaded_array['spkdata']
ttime = loaded_array['timedata']
stimON = loaded_array['stimON']
stimOFF = loaded_array['stimOFF']
spktiming =  loaded_array['spktiming']
spikeID =  loaded_array['spikeID']
spk_timing_arr_0 = loaded_array['spk_timing_array_0']
spk_timing_arr_1 = loaded_array['spk_timing_array_1']
spk_timing_arr_2 = loaded_array['spk_timing_array_2']

refractory_period = 2 #ms

spk_timing_0 = spktiming[np.where(spikeID == 0)]
spk_timing_1 = spktiming[np.where(spikeID == 1)]
spk_timing_2 = spktiming[np.where(spikeID == 2)]

NN0 = len(spk_timing_0)
NN1 = len(spk_timing_1)
NN2 = len(spk_timing_2)

#%%


# =============================================================================
# Set function
# =============================================================================
def Compute_cross_correlation(ttime, spk_timing_arr_1,spk_timing_arr_2 ):    
    NN = len(ttime)
    incr = ttime[1]-ttime[0]
    # =============================================================================
    # Compute cross-correlation
    # =============================================================================
    cross_corr = np.correlate(spk_timing_arr_2,spk_timing_arr_1, "same")
    t_delay = np.round(np.arange(-np.floor(NN/2),np.floor(NN/2)+1,1)*incr, decimals=2)  # ±数10msの配列を作っているだけ
    # =============================================================================
    # Comute shuffled cross-correlation
    # =============================================================================
    spk_timing_arr_2_shuffle = np.copy(spk_timing_arr_2) # copy original spike data
    np.random.shuffle(spk_timing_arr_2_shuffle) # shuffle spk_timing_arr_2, to make two arrays uncorrelated
    cross_corr_shuffle = np.correlate(spk_timing_arr_2_shuffle,spk_timing_arr_1, "same")
    
    return t_delay, cross_corr, cross_corr_shuffle

# =============================================================================
# Compute cross-correlation
# =============================================================================
t_delay_u10, cross_corr_u10, cross_corr_shuffle_u10 = Compute_cross_correlation(ttime, spk_timing_arr_0,spk_timing_arr_1 )
t_delay_u20, cross_corr_u20, cross_corr_shuffle_u20 = Compute_cross_correlation(ttime, spk_timing_arr_0,spk_timing_arr_2 )
t_delay_u21, cross_corr_u21, cross_corr_shuffle_u21 = Compute_cross_correlation(ttime, spk_timing_arr_1,spk_timing_arr_2 )

# =============================================================================
# Compute Inter spike interval (ISI)
# =============================================================================
ISI_u0 = spk_timing_0[1:NN0-1] - spk_timing_0[0:NN0-2]
ISI_u1 = spk_timing_1[1:NN1-1] - spk_timing_1[0:NN1-2]
ISI_u2 = spk_timing_2[1:NN2-1] - spk_timing_2[0:NN2-2]

# =============================================================================
# Display
# =============================================================================
mm = 5
nn = 1
plt.close("all")
# #_------
fig_ = plt.figure(figsize=(8,10))
plt.subplots_adjust(wspace=0.4, hspace=0.6)
# =============================================================================
# # plot raw data
# =============================================================================
ax1 = plt.subplot(mm,nn,1)
ax1.plot(ttime,spk_timing_arr_0,'r-',label = 'unit0')
ax1.plot(ttime,spk_timing_arr_1,'g-',label = 'unit1')
ax1.plot(ttime,spk_timing_arr_2,'b-',label = 'unit2')
ax1.plot(spk_timing_0,np.ones(NN0)*1.2,'rv')
ax1.plot(spk_timing_1,np.ones(NN1)*1.2,'gv')
ax1.plot(spk_timing_2,np.ones(NN2)*1.2,'bv')
ax1.set_yticks([0.0, 0.5, 1.0])
ax1.legend()
ax1.set_xlabel('time (msec)')
mm = 5
nn = 2

'''
ToDo : for文を消して普通にプロットする処理をかく。
Unit別にCrossCollilationをとる
ISIをヒストグラム化
おわり
'''
# =============================================================================
# # Plot cross correlograms
# =============================================================================
ax2_top = plt.subplot(mm,nn,3)
ax2_top.set_title('Cross-correlogram, unit#1 - unit#0')
ax2_top.set_xlabel('time (msec)')
ax2_top.set_yticks(np.arange(0.0, 3.1, 2))
ax2_top.set_xlim(-10, 10)
ax2_top.plot(t_delay_u10,cross_corr_u10)
ax2_top.plot(t_delay_u10,cross_corr_shuffle_u10,'m-')
yrng_top = [np.min(cross_corr_u10),np.max(cross_corr_u10)*1.1]
ax2_top.plot([0,0],yrng_top,'k:')
ax2_top.set_ylim(yrng_top)
ax2_top.legend()

ax2_mid = plt.subplot(mm,nn,5)
ax2_mid.set_title('Cross-correlogram, unit#2 - unit#0')
ax2_mid.set_xlabel('time (msec)')
ax2_mid.set_yticks([0, 50])
ax2_mid.set_xlim(-10, 10)
ax2_mid.plot(t_delay_u20,cross_corr_u20)
ax2_mid.plot(t_delay_u20,cross_corr_shuffle_u20,'m-')
yrng_mid = [np.min(cross_corr_u20),np.max(cross_corr_u20)*1.1]
ax2_mid.plot([0,0],yrng_mid,'k:')
ax2_mid.set_ylim(yrng_mid)
ax2_mid.legend()

ax2_bottom = plt.subplot(mm,nn,7)
ax2_bottom.set_title('Cross-correlogram, unit#2 - unit#1')
ax2_bottom.set_xlabel('time (msec)')
ax2_bottom.set_yticks(np.arange(0.0, 3.1, 2))
ax2_bottom.set_xlim(-10, 10)
ax2_bottom.plot(t_delay_u21,cross_corr_u21)
ax2_bottom.plot(t_delay_u21,cross_corr_shuffle_u21,'m-')
yrng_bottom = [np.min(cross_corr_u21),np.max(cross_corr_u21)*1.1]
ax2_bottom.plot([0,0],yrng_bottom,'k:')
ax2_bottom.set_ylim(yrng_bottom)
ax2_bottom.legend()

# # =============================================================================
# # # plot cross correlogram (shuffled CC is subtructed)
# # =============================================================================
ax3_top = plt.subplot(mm,nn,4)
diff_CC_top = cross_corr_u10 - cross_corr_shuffle_u10               # 
ax3_top.set_title('Cross-correlogram, unit#1 - unit#0')
ax3_top.set_xlabel('time (msec)')
ax3_top.set_yticks([-2.5, 0, 2.5])
ax3_top.set_xlim([-10, 10])
ax3_top.plot(t_delay_u10,diff_CC_top)
yrng_top = [np.min(diff_CC_top),np.max(diff_CC_top)*1.1]
ax3_top.set_ylim(yrng_top)
ax3_top.plot([0,0],yrng_top,'k:')
ax3_top.legend()


ax3_mid = plt.subplot(mm,nn,6)
diff_CC_mid = cross_corr_u20 - cross_corr_shuffle_u20               # 
ax3_mid.set_title('Cross-correlogram, unit#2 - unit#0')
ax3_mid.set_xlabel('time (msec)')
ax3_mid.set_yticks([0, 50])
ax3_mid.set_xlim([-10, 10])
ax3_mid.plot(t_delay_u20,diff_CC_mid)
yrng_mid = [0 ,np.max(diff_CC_mid)*1.1]
ax3_mid.set_ylim(yrng_mid)
ax3_mid.plot([0,0],yrng_mid,'k:')
ax3_mid.legend()

ax3_bottom = plt.subplot(mm,nn,8)
diff_CC_bottom = cross_corr_u21 - cross_corr_shuffle_u21
ax3_bottom.set_title('Cross-correlogram, unit#2 - unit#1')
ax3_bottom.set_xlabel('time (msec)')
ax3_bottom.set_yticks([-2.5, 0, 2.5])
ax3_bottom.set_xlim([-10, 10])
ax3_bottom.plot(t_delay_u21,diff_CC_bottom)
yrng_bottom = [np.min(diff_CC_bottom),np.max(diff_CC_bottom)*1.1]
ax3_bottom.set_ylim(yrng_bottom)
ax3_bottom.plot([0,0],yrng_bottom,'k:')
ax3_bottom.legend()

# =============================================================================
# # plot Inter spike interval
# =============================================================================
mm = 5
nn = 3
time_bin = 0.5
hist_bin = 100

ax4_left = plt.subplot(mm,nn,13)
ax4_left.set_title('ISI histogram, unit #0')
ax4_left.set_xlabel('InterSpikeInterval,ISI (msec)')
ax4_left.set_xticks([0, 5, 10])
ax4_left.set_xlim([0,10])
ax4_left.plot([refractory_period, refractory_period],[0,8],'m--')
ax4_left.hist(ISI_u0, bins=hist_bin, color="r")

ax4_center = plt.subplot(mm,nn,14)
ax4_center.set_title('ISI histogram, unit #1')
ax4_center.set_xlabel('InterSpikeInterval,ISI (msec)')
ax4_center.set_xticks([0, 5, 10])
ax4_center.set_xlim([0,10])
ax4_center.plot([refractory_period, refractory_period],[0,8],'m--')
ax4_center.hist(ISI_u1, bins=hist_bin, color="g")

ax4_right = plt.subplot(mm,nn,15)
ax4_right.set_title('ISI histogram, unit #2')
ax4_right.set_xlabel('InterSpikeInterval,ISI (msec)')
ax4_right.set_xticks([0, 5, 10])
ax4_right.set_xlim([0,10])
ax4_right.plot([refractory_period, refractory_period],[0,8],'m--')
ax4_right.hist(ISI_u2, bins=hist_bin, color="b")

plt.tight_layout()
plt.show
# %%
