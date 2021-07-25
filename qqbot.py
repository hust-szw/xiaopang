import itchat
from itchat.content import *
import threading
import datetime
import time
import requests
import json

#这里定义接收到消息所用方法
@itchat.msg_register(TEXT)
def simple_reply(msg):
    itchat.send_msg('已经收到了文本消息，消息内容为%s'%msg['Text'],toUserName=msg['FromUserName'])
    print(msg['FromUserName'],msg['Text'])
    url = "http://api.tianapi.com/txapi/saylove/index?key=4dfffca8c9a947305f91ba5753a9994e"
    print(url)
    response = requests.get(url)
    print(response.text)
    return json.loads(response.text)["newslist"][0]["content"]


#定时消息
def clock_msg():

    while 1:
        now = datetime.datetime.now()
        now_str = now.strftime('%Y/%m/%d %H:%M:%S'[9:])
        #print('\r{}'.format(now_str),end='')
        for event in clock_enents:
            if((event['time']==now_str)):
                event['function']()
        if (now_str=="00:00:00"):#重置每条消息的推送状态
            for people in clock_enents:
                people["push_state"]:False
            print("0点重置")
        time.sleep(1)

def get_weather(people):
    url = "http://aider.meizu.com/app/weather/listWeather?cityIds="+people["cityid"]
    response = requests.get(url)
    weather = json.loads(response.text)["value"][0]["weathers"][0]["weather"]
    date = json.loads(response.text)["value"][0]["weathers"][0]["date"]
    week = json.loads(response.text)["value"][0]["weathers"][0]["week"]
    temp_day = json.loads(response.text)["value"][0]["weathers"][0]["temp_day_c"]
    temp_night = json.loads(response.text)["value"][0]["weathers"][0]["temp_night_c"]
    huazhuang = json.loads(response.text)["value"][0]["indexes"][1]["content"]
    chuanyi = json.loads(response.text)["value"][0]["indexes"][0]["content"]
    yundong = json.loads(response.text)["value"][0]["indexes"][4]["content"]
    ganmao = json.loads(response.text)["value"][0]["indexes"][2]["content"]
    pm25 = json.loads(response.text)["value"][0]["pm25"]["pm25"]
    wuran = json.loads(response.text)["value"][0]["pm25"]["quality"]

    contant = "💕  早上好呀 " + people["neck_name"] + "\n💕  请查收"+ people["city"]+"今日的天气预报" + "\n💕 " + "\n💕  日期：" + date + "  " + week   + "\n💕  天气：" \
              + weather + "\n💕  白天温度：" + temp_day + "℃""\n💕  夜晚温度：" + temp_night + "℃" + "\n💕  pm值：" + pm25 + "\n💕  空气指数：" + wuran \
              + "\n💕  化妆：" + huazhuang + "\n💕  穿衣：" + chuanyi + \
              "\n💕  运动：" + yundong + "\n💕  感冒预防：" + ganmao+"\n\n        今天也要记得微笑呀~"
    # print(contant)
    return contant

def daily_push():
    for people in push_list:
        if((0 in people["push_id"])&(not people["push_state"][0]) ):
            content = get_weather(people)
            user_name = itchat.search_friends(people["user_name"])[0]["UserName"]
            itchat.send_msg(content,toUserName=user_name)
            people["push_state"] = True




if __name__=="__main__":
    # 定时事件
    clock_enents=[
        {
        "name":"daily_push",
        "id": 0,
        "time": "09:00:00",
        "function": daily_push,
        },
    ]
    #推送列表
    push_list=[
        {
            # 我
            "user_name":"shallwe",
            "neck_name":"泽泽", #绰号
            "push_state":[False],  #今日推送状态
            "push_id":[0] ,#订阅功能
            "city":"西安",
            "cityid":"101110101"
        },
        {
            # 亭
            "user_name":"Sweet💕",
            "neck_name":"亭亭", #绰号
            "push_state":[False],  #今日推送状态
            "push_id":[0] ,#订阅功能
            "city":"龙泉驿",
            "cityid":"101270102"
        }
    ]
    # 启动定时线程
    try:
        clock_thread = threading.Thread(target=clock_msg)
        clock_thread.start()
    except:
        print("Error: 无法启动线程")
    # 登录
    itchat.auto_login(hotReload=True)  # 不想每次都扫描，登录时预配置
    itchat.run()
