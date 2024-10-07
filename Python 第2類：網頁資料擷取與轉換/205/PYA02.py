# 載入 requests 與 json 模組
import requests
#import json # 不寫也無妨

# 開放資料Json格式連結
url = 'https://www.codejudger.com/target/5205.json'
# 發出Get請求
response = requests.get(url)

# 回傳內容長度
print('Content-Length:', len(response.content)) # 印出內容之間並沒有空格（雖然題目範例裡有一空格，哈）
# =============================================================================
# response.text: 回應的內容，以字串形式表示。通常是 HTML 或 JSON 格式的回應內容。
# response.content: 回應的內容，以字節形式表示。如果要處理二進位資料（如圖片）。
# =============================================================================

# 將取得的回傳內容轉換成Json格式
response = response.json()

print()

# 顯示新北市每一個地區的PM2.5相關資料
print('新北市PM2.5相關資料：')
for record in response:
    if record['County'] == '新北市':
        print('%s：' % record['SiteName'])
        print('\tAQI：%s' % record['AQI'])
        print('\tPM2.5：%s' % record['PM2.5'])
        print('\tPM10：%s' % record['PM10'])
        print('\t資料更新時間：%s' % record['PublishTime'])
