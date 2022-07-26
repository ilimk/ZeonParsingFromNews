import requests
import datetime
import json

timestr = datetime.datetime.now().strftime('%Y-%m-%d%%%H:%M:%S.%f')

urlOfNewsLine = 'http://newsline.kg/getNews.php?limit=2&last_dt=' + timestr

requestNewsLine = requests.get(urlOfNewsLine)

json_data = json.loads(requestNewsLine.text)

json_object = json.dumps(json_data['data'], indent = 4)
print(json_object)





