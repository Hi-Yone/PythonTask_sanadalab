#%%
import numpy as np 
import matplotlib.pyplot as plt

  
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
# Generate artificial data
# =============================================================================
ttime = np.arange(0,1001,1)/100
NN = len(ttime)
spk_timing_arr_1 = np.zeros(NN)
spk_timing_arr_2 = np.zeros(NN)
t_d = 20 # Time delay of unit2 from unit1
# unit 1
spk_timing_arr_1[np.where(np.random.rand(NN)>0.8)] = 1
# unit 2, supposed to delay t_d msec from unit 1
spk_timing_arr_2[t_d:NN-1] = spk_timing_arr_1[0:NN-t_d-1]
# get spike timing
spk_timing_1 = ttime[np.where(spk_timing_arr_1 == 1)]
spk_timing_2 = ttime[np.where(spk_timing_arr_2 == 1)]
# length of array 
NN1 = len(spk_timing_1)
NN2 = len(spk_timing_2)

# =============================================================================
# Compute cross-correlation
# =============================================================================
t_delay, cross_corr, cross_corr_shuffle = Compute_cross_correlation(ttime, spk_timing_arr_1,spk_timing_arr_2 )
# =============================================================================
# Compute Inter spike interval (ISI)
# =============================================================================
ISI_1 = spk_timing_1[1:NN1-1] - spk_timing_1[0:NN1-2]
ISI_2 = spk_timing_2[1:NN2-1] - spk_timing_2[0:NN2-2]

# =============================================================================
# Display
# =============================================================================
mm = 3
nn = 1
plt.close("all")
#_------
fig_ = plt.figure(figsize=(8,10))
plt.subplots_adjust(wspace=0.4, hspace=0.6)
# =============================================================================
# # plot raw data
# =============================================================================
plt.subplot(mm,nn,1)
plt.plot(ttime,spk_timing_arr_1,'b-',label = 'unit1')
plt.plot(ttime,spk_timing_arr_2,'r-',label = 'unit2')
plt.xlim(0,1)
plt.plot(spk_timing_1,np.ones(NN1)*1.2,'bx')
plt.plot(spk_timing_2,np.ones(NN2)*1.2,'rx')
plt.legend()
plt.xlabel('time (msec)')
# =============================================================================
# # Plot cross correlograms
# =============================================================================
mm = 3
nn = 2
plt.subplot(mm,nn,3)
plt.plot(t_delay,cross_corr, label='CrossCorrelogram(CC_)')
plt.plot(t_delay,cross_corr_shuffle,'m-',label='shuffled CC')
yrng = [np.min(cross_corr),np.max(cross_corr)*1.1]
plt.plot([0,0],yrng,'k:')
plt.ylim(yrng)
plt.title('Cross-correlogram, unit#2 - unit#1')
plt.legend()
plt.xlabel('time (msec)')
# =============================================================================
# # plot cross correlogram (shuffled CC is subtructed)
# =============================================================================
plt.subplot(mm,nn,4)
diff_CC = cross_corr - cross_corr_shuffle               # 
plt.plot(t_delay,diff_CC, label='CC - shuffled CC')
yrng = [np.min(diff_CC),np.max(diff_CC)*1.1]
plt.plot([0,0],yrng,'k:')
# plt.xlim([-50,50])
plt.ylim(yrng)
plt.legend()
plt.xlabel('time (msec)')
plt.title('Cross-correlogram, unit#2 - unit#1')
# =============================================================================
# # plot Inter spike interval
# =============================================================================
plt.subplot(mm,nn,5)
plt.hist(ISI_1)
plt.xlabel('InterSpikeInterval,ISI (msec)')
plt.title('ISI histogram, unit #1')
plt.subplot(mm,nn,6)
plt.hist(ISI_2)
plt.xlabel('InterSpikeInterval,ISI (msec)')
plt.title('ISI histogram, unit #2')
plt.tight_layout()

plt.show    
# %%
