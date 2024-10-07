# --開始--批改評分使用，請勿變動
import matplotlib as mpl
mpl.use('Agg')
# --結束--批改評分使用，請勿變動

# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

# 四個月份
labels = ['Jun', 'Jul', 'Aug', 'Sep']
sizes = [20, 30, 40, 10]
# 圓餅圖顏色
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

# 長條圖 位置
plt.subplot(1, 2, 1)
# =============================================================================
# plt.subplot(nrows, ncols, index)
# nrows：子圖的列數，要分割成幾張垂直重疊的子圖。
# ncols：子圖的欄數，要分割成幾張水平並排的子圖。
# index：子圖索引，從 1 開始，由左至右的順序排列。
# =============================================================================
xticks = range(0, len(labels)) # 設定 X 軸刻度範圍
# 長條圖以labels為X軸，sizes為Y軸，各長條顏色為藍色（blue）
plt.xticks(xticks, labels)
plt.bar(labels, sizes, color = 'blue') # 水平軸、垂直軸、長條顏色

# 圓餅圖 位置
plt.subplot(1, 2, 2)
# 圓餅圖以 labels 為圖標，sizes 為各項所占百分比
# 圓餅圖 colors 為各項顏色，突顯「Aug」
# 圓餅圖顯示各項百分比到小數點第1位
explode = (0, 0, 0.1, 0) # 突出顯示 'Aug' 部分，對應 labels
plt.pie(sizes, explode = explode, labels = labels,
        colors = colors, autopct = '%.1f%%')
# =============================================================================
# autopct = '%.1f%%' 這裡不可改寫成 f-string 格式
# =============================================================================

# 長寬比為1:1
plt.axis('equal')

plt.savefig('chart.png')
plt.close()
