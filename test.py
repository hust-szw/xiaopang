# import requests
# import json
# url = "http://aider.meizu.com/app/weather/listWeather?cityIds=101270101"
# print(url)
# response = requests.get(url)
# weather = json.loads(response.text)["value"][0]["weathers"][0]["weather"]
# date =  json.loads(response.text)["value"][0]["weathers"][0]["date"]
# week = json.loads(response.text)["value"][0]["weathers"][0]["week"]
# temp_day = json.loads(response.text)["value"][0]["weathers"][0]["temp_day_c"]
# temp_night = json.loads(response.text)["value"][0]["weathers"][0]["temp_night_c"]
# huazhuang = json.loads(response.text)["value"][0]["indexes"][1]["content"]
# chuanyi = json.loads(response.text)["value"][0]["indexes"][0]["content"]
# yundong = json.loads(response.text)["value"][0]["indexes"][4]["content"]
# ganmao = json.loads(response.text)["value"][0]["indexes"][2]["content"]
# pm25 = json.loads(response.text)["value"][0]["pm25"]["pm25"]
# wuran = json.loads(response.text)["value"][0]["pm25"]["quality"]
#
# nackname = "亭亭小公主"
# contant = "💕  早上好呀"+nackname+" 这是今天的天气!"+"\n💕 "+"\n💕  日期："+date+"  "+week+"\n💕  你的城市："+"成都"+"\n💕  天气：" \
#             +weather+"\n💕  白天温度："+temp_day+"℃""\n💕  夜晚温度："+temp_night+"℃"+"\n💕  pm值："+pm25+"\n💕  空气指数："+wuran \
#             +"\n💕  化妆："+huazhuang+"\n💕  穿衣："+chuanyi+ \
#             "\n💕  运动："+yundong+"\n💕  感冒预防："+ganmao
# print(contant)
#
# url = "http://api.tianapi.com/txapi/saylove/index?key=4dfffca8c9a947305f91ba5753a9994e"
# print(url)
# response = requests.get(url)
# print(json.loads(response.text)["newslist"][0]["content"]





# state = 0
# info = ""
# if (state == 0):
#     if (info == "雨泽"):
#         menu = "你好呀，我是雨泽小朋友，请问喊我有什么事？目前爸爸妈妈只教会了我以下技能哦~\n" \
#                "你可以选择前面的序号让我来给你展示~\n" \
#                "1：自我介绍\n" \
#                "2：考研资讯\n"
#         state = 1
#         print(menu)
#     else:
#         print("tuling")
# if (state == 1):
#     pass


import requests
from bs4 import BeautifulSoup

def get_xjd():
    url = "http://yz.xjtu.edu.cn/index/zsdt.htm"
    res = requests.get(url)
    res.encoding = 'utf-8'
    html= res.text
    # print(html)
    soup = BeautifulSoup(html,"html.parser")
    list = soup.findAll(name="li", attrs={"class" :"clearfix"})
    return list

def get_xgd():
    url = "http://yzb.nwpu.edu.cn/new/sszs/zsgg.htm"
    res = requests.get(url)
    res.encoding = 'utf-8'
    html= res.text
    soup = BeautifulSoup(html,"html.parser")
    tags = soup.find(attrs={"class":'col-md-9 col-sm-9 col-xs-12 cno-right'})
    list1 = tags.find_all(name = "li")

    url = "http://yzb.nwpu.edu.cn/new/sszs/zsjz.htm"
    res = requests.get(url)
    res.encoding = 'utf-8'
    html = res.text
    soup = BeautifulSoup(html, "html.parser")
    tags = soup.find(attrs={"class": 'col-md-9 col-sm-9 col-xs-12 cno-right'})
    list2 = tags.find_all(name="li")
    print(list2)


a = [1,2,3]
b = [1,2,4]
print(list(set(b).difference(set(a))))


