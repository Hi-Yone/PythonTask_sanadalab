# Instruction
# 1) Generate x1=normal distribution and y1= normal distribution. use np.random.normal or np.random.randn
# 2) Select data points within range, -1<x1<1, then plot selected data as red symbols. 
#    To select data, use np.where()
#    Data point outside of the range must be plotted as blue symbols.
# 3) Set axes labels, ticks accordingly (refer attached pdf file)
# 4) Save pdf file of the figure ("Task02-2_select_data_applied_yourname.pdf")
# 5) Submit your source code and figure pdf

#%%
import numpy as np
import matplotlib.pyplot as plt

x1 = np.random.randn(400)
y1 = np.random.randn(400)
x2 = x1[np.where((x1 > -1) &(x1 < 1))]
y2 = y1[np.where((x1 > -1) &(x1 < 1))]

fig = plt.figure(figsize=(10, 10))

plt.xticks(np.arange(-5.0, 5.1, 2.5))
plt.yticks(np.arange(-5.0, 5.1, 2.5))
plt.xlim(-5.0, 5.0)
plt.ylim(-5.0, 5.0)
data2 = plt.scatter(x2, y2, color = 'r', alpha = 0.5, zorder = 2, label = 'x1 VS y1 selected data')
data1 = plt.scatter(x1, y1, color = 'b', alpha = 0.5, zorder = 1, label = 'x1 VS y1 non-selected data')
plt.title('Scatter plot of normal distributions, \nselect data in $-1 ≤ x ≤ 1$')
plt.grid()
plt.legend()
plt.show()
# %%

# %%
