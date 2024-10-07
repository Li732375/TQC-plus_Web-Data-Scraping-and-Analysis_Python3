# -*- coding: utf-8 -*-
# --開始--批改評分使用，請勿變動
import matplotlib as mpl
mpl.use('Agg')
# --結束--批改評分使用，請勿變動

# 載入 matplotlib.pyplot 並縮寫為 plt
import matplotlib.pyplot as plt

data1 = [1, 4, 9, 16, 25, 36, 49, 64]
data2 = [1, 2, 3, 6, 9, 15, 24, 39]
seq = [1, 2, 3, 4, 5, 6, 7, 8]

# 數據及線條設定
plt.plot(seq, data1, '--.b', seq, data2, '--.r', linewidth = 1) # 顏色不可互換
# 軸刻度
plt.axis([0, 8, 0, 70]) # X 軸 0 ~ 8，Y 軸 0 ~ 70
# =============================================================================
# plt.axis() 參數用法：
# 
# [x_min, x_max, y_min, y_max]：採用一個四元素串列表示依序表示水平、垂直軸極值。
# 'auto'：自動設置軸範圍。
# 'equal':固定軸的比例，確保 X 軸和 Y 軸的比例相同。
# 'off'：隱藏圖形中的 X 和 Y 軸。
# =============================================================================

# 圖表標題
plt.title('Figure', fontsize = 24)
# X軸標題
plt.xlabel('x-Value', fontsize = 16)
# Y軸標題
plt.ylabel('y-Value', fontsize = 16)

# 輸出圖片檔案
plt.savefig('chart.png')
plt.close()
