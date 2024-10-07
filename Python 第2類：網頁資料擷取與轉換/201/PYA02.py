# 載入模組
import requests
import re

url = 'https://www.codejudger.com/target/5201.html'

# 使用 GET 請求
htmlfile = requests.get(url)
# 驗證HTTP Status Code
if htmlfile.status_code == 200:
    # 欲搜尋的字串
    search_str = input("請輸入欲搜尋的字串 : ")
    tar_str_list = re.findall(search_str, htmlfile.text)
    if search_str in htmlfile.text:
        print(search_str, "搜尋成功")
        print(search_str, "出現 %d 次" % len(tar_str_list))
    else:
        print(search_str, "搜尋失敗")
        print(search_str, "出現 0 次")
else:
    print("網頁下載失敗")
