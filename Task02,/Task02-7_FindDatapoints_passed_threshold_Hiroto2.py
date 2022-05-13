# =============================================================================
# Task02-7, Find Datapoints passed threshold
# =============================================================================
# Instruction
# 0) import numpy and matplotlib.pyplot
# 1) Generate x, from 0 to 10, number of datapoints = 100
# 2) Generate sine wave, y = sin(2x)
# 3) Set threshold as 80% of peak
# 4) Detect datapoints just passed the threshold without using for loop.
# 5) Save pdf file of the figure ("Task02-7_FindDatapoints_passed_threshold_yourname.pdf")
# 6) Submit source code and figure pdf

#%%
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10.1, 0.1)
y = np.sin(2*x)

thr = y.max() * 0.8                     # 閾値
thr_line = np.tile(thr, 101)            # プロット用にtileで閾値を並べる
passed = np.where(thr >= y, 0, 1)       # 閾値を超えるyを探して二値化する
passed_arr = np.zeros(101)              # プロット用の配列を0で初期化

# 閾値を超える最初のインデックスを取得
i,idx = 0,0
passed_idx = []
while i <= len(passed) - 2:
    if passed[i] != passed[i+1]:
        i += 1
        idx = i
        if passed[i] == 1:
            passed_idx.append(idx)
    i += 1


for i in passed_idx:
    passed_arr[i] = 1



# グラフ描画
fig = plt.figure(figsize=(15, 7))
plt.title('Detect datapoints passed threshold')
plt.ylabel('y')
plt.xlabel('time')
plt.plot(x, y, marker = 'o', label = 'y = sin(2*x)')                            # y = sin(2*x)のグラフ
plt.plot(x, thr_line, color = 'r', linestyle = 'dashed', label = 'threshold')   # 閾値ライン
plt.plot(x, passed_arr, color = 'orange', label = 'selected location')          # 閾値を超えた瞬間だけ飛び出すようにする
plt.legend()



# %%
