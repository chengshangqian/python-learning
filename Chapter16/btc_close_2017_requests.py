import requests

json_url = "https://img-home.csdnimg.cn/data_json/toolbar/toolbar0812.json"
req = requests.get(json_url)
with open("btc_close_2017_requests.json", "w") as f:
    print(req.text)
    f.write(req.text)

file_urllib = req.json()
print(file_urllib)
