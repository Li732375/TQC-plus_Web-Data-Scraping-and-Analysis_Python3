# 載入 json 模組
import json


# 建立資料
data = {
        'people':[
                {'id': '1',
                 'name': 'Peter',
                 'country': 'Taiwan'},
                {'id': '2',
                 'name': 'Jack', 
                 'country': 'USA'},
                {'id': '3', 
                'name': 'Cindy', 
                'country': 'Japan'}
                ]}

# 將資料寫入json檔案
with open('write.json', 'w') as outfile:
    json.dump(data, outfile)
