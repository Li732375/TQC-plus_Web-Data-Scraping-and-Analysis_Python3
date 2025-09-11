## 作答提要
 - 基本上，答案都在提示提及了。
 - 計數的類別方法名稱為 count。
 - 題目提到 "輸出後二位學生的所有成績"，這裡作法不只一種。
   1. 列出前幾筆資料方法名稱為 head，參數為筆數。
   > 與之相對的方法名稱為 tail (末幾筆)，見題 [301](https://github.com/Li732375/TQC-plus_Web-Data-Scraping-and-Analysis_Python3/blob/master/Python%20%E7%AC%AC3%E9%A1%9E%EF%BC%9A%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90%E8%83%BD%E5%8A%9B/301/README.md?plain=1)。
   2. slice 寫法。
   
## 特別注意
 - 類別方法 groupby 僅僅是以此做出分群，不會修改數據。所以還要再次指定欄位。
 - 執行內容中，如 "Name: XX, dtype: int64" 這部分的內容也需一致。
 - 類別方法 sort_values 預設序位為由小到大。
 - 題意 "台北市最近病例的日期"，這裡作法不只一種，見題 [301](https://github.com/Li732375/TQC-plus_Web-Data-Scraping-and-Analysis_Python3/blob/master/Python%20%E7%AC%AC3%E9%A1%9E%EF%BC%9A%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90%E8%83%BD%E5%8A%9B/301/README.md?plain=1)。
   1. 以 **欄位名稱作屬性**，但名稱需不含空格、特殊符號，且不以數字開頭。
   2. 以字典形式存取，應用上更為廣泛。
