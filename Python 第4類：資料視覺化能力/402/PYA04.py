# --開始--批改評分使用，請勿變動
import matplotlib as mpl
mpl.use('Agg')
# --結束--批改評分使用，請勿變動

# 載入 matplotlib.pyplot 並縮寫為 plt
import matplotlib.pyplot as plt
# 載入 csv 模組
import csv

x = []
y = []

# 讀入 read.csv
with open('read.csv', 'r', encoding = 'utf8') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
    for row in plots:
        x.append(row[0])
        y.append(float(row[1]))

x_ticks = range(1, len(x) + 1)
plt.plot(x_ticks, y, label = 'banana')
plt.xticks(x_ticks, x) # 刻度值、刻度標籤
# =============================================================================
# plt.xticks(a, b)
# 可以接受兩個參數：刻度值 (a) 和刻度標籤 (b) 。
# 刻度值設定時，要注意資料是否符合在 x 軸上的區間內。
# 例如，plt.xticks([0, 1, 2, 3], ['zero', 'one', 'two', 'three']) 會將 y 軸上的
# 刻度位置設定為 0, 1, 2, 3，並將刻度標籤設定為 'zero', 'one', 'two', 'three'。
# =============================================================================
plt.xlabel('date')
plt.ylabel('NT$')
plt.ylim(15, 25) # 將 y 軸的範圍設置為從 15 到 25。
# 添加圖表標題 title()
plt.title('Market Average Price')
plt.legend()
# 使用 savefig() 函數
plt.savefig('chart.png')
plt.close()
