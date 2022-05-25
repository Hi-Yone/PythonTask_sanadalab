#%%
import numpy as np
import matplotlib.pyplot as plt

# load array from saved .npz file
loaded_array = np.load('Task_spike_wave_data.npz')
# copy array data to varible you defined
spike_waveform = loaded_array['spkdata']  # raw spike wave data
ttime = loaded_array['timedata']  # this is x axis, time (msec)
stimON = loaded_array['stimON']   # stim onset timing (light turned on)
stimOFF = loaded_array['stimOFF'] # stimm offset timing (light turned off) 
threshold = 1.5 # Volt
np.tile(threshold, len(spike_waveform))

fsz = 18 # define font size just for visualization
#----------------------------


plt.close("all")
mm = 3
nn = 1
fig = plt.figure(figsize=(16,20))
plt.subplots_adjust(wspace=0.4, hspace=0.6)

# plot data you loaded above
ax1 = plt.subplot(mm,nn,1)
ax1.plot(ttime, spike_waveform,'b-',label = 'spike waveform')
ax1.plot([stimON, stimON], [-3, 3],'r--',label = 'STIM ON')
ax1.plot([stimOFF, stimOFF], [-3, 3],'m--',label = 'STIM OFF')
ax1.plot(ttime, np.ones(len(ttime))*threshold,'g--',label = 'threshold')
# ax1.scatter(ttime, passed_thr, 'x')

# set labels.
ax1.set_title('Spike wave data', fontsize=fsz)
ax1.set_ylabel('voltage(V)', fontsize=fsz)
ax1.set_xlabel('time from STIM ONSET (msec)', fontsize=fsz)
ax1.set_ylim([-3,3])
ax1.set_xlim([ttime[0],ttime[len(ttime)-1]])
ax1.legend(loc='best') # add legend
ax1.grid()

ax2 = plt.subplot(mm,nn,2)
ax2.plot([stimON, stimON], [0, 100],'r--')
ax2.plot([stimOFF, stimOFF], [0, 100],'m--')

ax2.set_title('PSTH (Post Stimulus Time Histogram', fontsize=fsz)
ax2.set_ylabel('Firing rate (spikes/sec) \n (spike number divided by 10msec)', fontsize=fsz)
ax2.set_xlabel('time from STIM ONSET (msec)', fontsize=fsz)
ax2.set_xlim([ttime[0],ttime[len(ttime)-1]])
ax2.grid()

ax3 = plt.subplot(mm,nn,3)
ax3.plot([0,0],[-3,3],'r--')
ax3.plot([-3,4], np.ones(2)*threshold,'g--')

ax3.set_title('Spike Waveform', fontsize=fsz)
ax3.set_ylabel('Voltage(V)', fontsize=fsz)
ax3.set_xlabel('normalized time (msec)', fontsize=fsz)
ax3.set_xlim([-3,4])
ax3.set_ylim([-3,3])
ax3.grid()

plt.show()


# plt.savefig("Task_01234_Yourname_DetectSpikeTiming.pdf")
# %%
