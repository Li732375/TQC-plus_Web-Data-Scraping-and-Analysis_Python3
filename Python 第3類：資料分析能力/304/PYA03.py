# 載入 numpy 模組
import numpy
# 載入 pandas 模組縮
import pandas 

# 讀入 read.csv 檔案
df = pandas.read_csv('read.csv')

# 判斷資料型態
#print('資料型態：%s' % type(numpy.array(df)))
print('資料型態：%s' % type(df.to_numpy()))
# 計算平均數
print('平均值：%.2f' % numpy.mean(df))
#print('平均值：%.2f' % numpy.mean(df.to_numpy()))
# 計算中位數
print('中位數：%.2f' % numpy.median(df.to_numpy()))
# 計算標準差
print('標準差：%.2f' % numpy.std(df.to_numpy()))
# =============================================================================
# print('標準差：%.2f' % numpy.std(df))
# FutureWarning: Calling float on a single element Series is deprecated and 
# will raise a TypeError in the future. Use float(ser.iloc[0]) instead
#   print('標準差：%.2f' % numpy.std(df))
# =============================================================================
# 計算變異數
print('變異數：%.2f' % numpy.var(df.to_numpy()))
# =============================================================================
# print('變異數：%.2f' % numpy.var(df))
# FutureWarning: Calling float on a single element Series is deprecated and 
# will raise a TypeError in the future. Use float(ser.iloc[0]) instead
#   print('變異數：%.2f' % numpy.var(df))
# =============================================================================
# 計算極差值
print('極差值：%.2f' % numpy.ptp(df))
#print('極差值：%.2f' % numpy.ptp(df.to_numpy()))
