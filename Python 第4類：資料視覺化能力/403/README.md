## 作答提要
 - 基本上，答案都在提示提及了。
 - 參數 labels 表示該數據在圖例中顯示的名稱。
   
## 特別注意
 - 方法 x_ticks 表示水平軸實際刻度值，供引進的數據對應座標用。方法 xlabel 則表示水平軸顯示刻度值，兩者長度彼此對應。
 > 是的！實際刻度值與要顯示的刻度值可以不同。

 > 垂直軸也相同，但名稱內的 x 要改寫成 y。

 - 類別方法 subplot 表示切子圖，參數順序為
    - nrows：子圖列數，要分割成幾張垂直重疊的子圖。
    - ncols：子圖欄數，要分割成幾張水平並排的子圖。
    - index：子圖索引，從 1 開始，由左至右的順序排列。
 > 題目的檔案為 "待編修檔"，所以並非完全不可異動！需視題目而調整。

 > 參數 autopct 這裡不可改寫成 f-string 格式。

 - 長寬設定見作答 [401](https://github.com/Li732375/TQC-plus_Web-Data-Scraping-and-Analysis_Python3/blob/master/Python%20%E7%AC%AC4%E9%A1%9E%EF%BC%9A%E8%B3%87%E6%96%99%E8%A6%96%E8%A6%BA%E5%8C%96%E8%83%BD%E5%8A%9B/401/PYA04.py)