import requests
import json
import datetime
from time import strftime, sleep

from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat'
}
# 地址
url = 'https://j1.pupuapi.com/client/recommendation/product/net/group?store_id=deef1dd8-65ee-46bc-9e18-8cf1478a67e9&product_id=2df8aabf-a0f1-4f22-bc08-36a3be483acc&size=8'
# 发起请求
response = requests.get(url=url, headers=headers, verify=False)
text = response.text
# 转换成json格式
jsonbj = json.loads(text)
# 得到商品名
name = jsonbj['list'][0]['items'][0]['name']
# 得到商品价格信息
#折后价
zprice = (jsonbj['list'][0]['items'][0]['price']) /100
#原价
yprice = jsonbj['list'][0]['items'][0]['market_price'] /100
# 规格
guige = jsonbj['list'][0]['items'][0]['spec']
# 详细信息
x = jsonbj['list'][0]['items'][0]['sub_title']

print("--------------" + name + "----------")
print("规格：" + guige)
print("价格" + str(yprice))
print("原价/折扣价：" + str(yprice) + "/" + str(zprice))
print("详细内容：" + x)
print("\n\n--------------" + name + "的价格波动----------")

while (1):
    response = requests.get(url=url, headers=headers, verify=False)
    text = response.text
    # 转换成json格式
    jsonbj = json.loads(text)
    yprice = (jsonbj['list'][0]['items'][0]['price']) /100
    # 获取时间
    time = datetime.datetime.now()

    print(str(time) + "价格为" + str(yprice))
    # 休眠5秒
    sleep(5)


