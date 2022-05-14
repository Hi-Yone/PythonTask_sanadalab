#%%
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10.1, 0.1)
y = np.sin(2 * x)                       # y = sin(2x)を計算

thr = max(y) * 0.8                      # 閾値80%
thr_line = np.tile(thr, 101)            # プロット用にtileで閾値を並べる

passed_y_1 = np.where((thr <= y), 1, 0)       # 閾値を超えるyを探す（それ以外は0）
passed_y_2 = np.where((thr <= y), 0, 1)       # 0と1を入れ替えたものを作成
passed_y_3 = np.roll(passed_y_2, 1)           # 右に値を一つずらす 

passed = passed_y_1 & passed_y_3

# グラフ描画
fig = plt.figure(figsize=(15, 7))
plt.title('Detect datapoints passed threshold')
plt.ylabel('y')
plt.xlabel('time')
plt.xticks(np.arange(0, 10.1, 0.5))
plt.grid()
plt.plot(x, y, marker = 'o', label = 'y = sin(2*x)')                            # y = sin(2*x)のグラフ
plt.plot(x, thr_line, color = 'r', linestyle = 'dashed', label = 'threshold')   # 閾値ライン
plt.plot(x, passed, color = 'orange', label = 'selected location')              # 閾値を超えた瞬間だけ飛び出すようにする
plt.legend()

# %%