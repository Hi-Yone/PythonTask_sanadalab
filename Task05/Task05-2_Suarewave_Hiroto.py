# Instructions
# Generate timedata from 0 to 5, 0.01 sec step
# def sinewave(). Input argument should be timedata, amplitude, frequency, phase and baseline, return y=sine()
# def squarewave(). Input argument shoudl be timedata, n_array, amplitue, frequency, phase and base. return y=squarewave()
# compute square wave where, [Amp, frequency, phase, baseline] = [1, 1(Hz), 0(deg)), 0]. 
# Equasion of square wave is shown in the attached pdf.
# (1)n array =1
# (2)n array =1,3
# (3)n array =1,3,5
# (4)n array =1~11
# (5)n array =1~21
# (6)n array =1~999
# n: odd number

# plot them in each subplot
# Set axes labels, ticks accordingly (refer attached pdf file)
# Save figure as 'Task05-2_Suarewave_Yourname.pdf'
# Submit both your source code and figure pdf file

#%%
import numpy as np
import matplotlib.pyplot as plt

timedata = np.arange(0, 5, 0.01)
AMP, FREQ, PHASE, BASELINE = 1, 1, 0, 0

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

# ---------------------------< data plot >----------------------------
fig = plt.figure(figsize=(8,12))
plt.subplots_adjust(hspace=1.2)

n_array = generate_n_array(1)
ax1 = plt.subplot(6,1,1)
ax1.set_title('(1) Square wave, y=$\sum{\\frac{4}{n\pi} * \sin{(2\pi ft)}}$, f=1[Hz], n=1')
ax1.set_xlabel('time(sec)')
ax1.set_ylabel('y')
ax1.grid()
ax1.plot(timedata, squarewave(timedata, n_array, AMP, FREQ, PHASE, BASELINE))

n_array = generate_n_array(2)
ax2 = plt.subplot(6,1,2)
ax2.set_title('(2) f=1[Hz], n= ' + str(n_array))
ax2.set_xlabel('time(sec)')
ax2.set_ylabel('y')
ax2.grid()
ax2.plot(timedata, squarewave(timedata, n_array, AMP, FREQ, PHASE, BASELINE))

n_array = generate_n_array(3)
ax3 = plt.subplot(6,1,3)
ax3.set_title('(3) f=1[Hz], n= ' + str(n_array))
ax3.set_xlabel('time(sec)')
ax3.set_ylabel('y')
ax3.grid()
ax3.plot(timedata, squarewave(timedata, n_array, AMP, FREQ, PHASE, BASELINE))

n_array = generate_n_array(6)
ax4 = plt.subplot(6,1,4)
ax4.set_title('(4) f=1[Hz], n= ' + str(n_array))
ax4.set_xlabel('time(sec)')
ax4.set_ylabel('y')
ax4.grid()
ax4.plot(timedata, squarewave(timedata, n_array, AMP, FREQ, PHASE, BASELINE))

n_array = generate_n_array(11)
ax5 = plt.subplot(6,1,5)
ax5.set_title('(5) f=1[Hz], n=2m-1, $1 \leq m \leq 11$')
ax5.set_xlabel('time(sec)')
ax5.set_ylabel('y')
ax5.grid()
ax5.plot(timedata, squarewave(timedata, n_array, AMP, FREQ, PHASE, BASELINE))

n_array = generate_n_array(500)
ax6 = plt.subplot(6,1,6)
ax6.set_title('(6) f=1[Hz], n=2m-1, $1 \leq m \leq 500$')
ax6.set_xlabel('time(sec)')
ax6.set_ylabel('y')
ax6.grid()
ax6.plot(timedata, squarewave(timedata, n_array, AMP, FREQ, PHASE, BASELINE))
# ------------------------------------------------------------------------
# %%
