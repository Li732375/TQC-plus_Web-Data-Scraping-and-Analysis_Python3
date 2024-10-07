# --開始--批改評分使用，請勿變動
set_seed = 123
# --結束--批改評分使用，請勿變動

import numpy as np

x = np.random.RandomState(set_seed).randint(low = 5, high = 16, size = 15)
print('隨機正整數：', x)

x = x.reshape(3, 5)
print('X矩陣內容：')
print(x)
print('最大：', x.max())
print('最小：', x.min())
print('總和：', x.sum())
print('四個角落元素：')
print(x[np.ix_([0, 2], [0, 4])]) # 符合"行"索引(內 list) 0 和 2，及"列"索引(外 list)是 0 和 4 的元素。
# 選取第 0 和第 2 行、第 0 和第 4 列的索引。
# 將其應用到目標矩陣時，會得到這些行列的「外積」，即所有可能的行列組合。