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
# 
# =============================================================================
fsz = 13
plt.close("all")
fig_ = plt.figure(figsize=(8,10))
plt.subplots_adjust(wspace=0.4, hspace=0.6)

plt.subplot(3,1,1)
plt.plot(ttime,spike_waveform)
plt.xlabel('time(msec)', fontsize = fsz)
plt.title('Original spike waveform', fontsize = fsz)
plt.xlim([0,10])

plt.subplot(3,2,3)
plt.plot(xf,kfilter)
plt.xlabel('time', fontsize = fsz)
plt.title('Convolution Filter', fontsize = fsz)

plt.subplot(3,1,3)
plt.plot(ttime,spike_waveform_filtered,'r-')
plt.xlabel('time(msec)', fontsize = fsz)
plt.xlim([0,10])
plt.title('Filtered wave', fontsize = fsz)
# %%
