import itchat
from itchat.content import *
import threading
import datetime
import time
import requests
import json
from bs4 import BeautifulSoup
#这里定义接收到消息所用方法
@itchat.msg_register(TEXT)
def msg_reply(msg):
    info = msg['Text']
    global state
    if (state==0):
        if (info == "雨泽"):
            menu = "你好呀，我是雨泽小朋友，请问喊我有什么事？目前爸爸妈妈只教会了我以下技能哦~\n" \
                   "(你可以选择前面的序号让我来给你展示~)\n" \
                   "0：雨泽成长记录\n" \
                   "1：研招网推送\n"
            state = 1
            return menu
        else:
            return get_response(info.encode('UTF-8'))
    if(state == 1):
        if(info =="0"):
            jieshao = "你好，我的名字叫邵雨泽~雨亭的雨，泽为的泽~你可以喊我雨泽！\n\n" \
                      "7月17日，我被爸爸妈妈带到了这个世界，好开心~\n\n" \
                      "7月24日，我学会了给爸爸妈妈汇报每日的天气情况，成为了爸爸妈妈的贴心小助手~\n\n" \
                      "7月27日，爸爸教会了我说话，他说这样他不在的时候我就可以陪着妈妈~\n\n"
            state = 0
            return jieshao
        elif(info == "1"):
            pass #爬取考研信息
            state = 0
        else:
            state = 0
            return("抱歉呦，雨泽还不会这项技能呢~")

#获得交大研招网信息
def get_xjd():
    url = "http://yz.xjtu.edu.cn/index/zsdt.htm"
    res = requests.get(url)
    res.encoding = 'utf-8'
    html= res.text
    # print(html)
    soup = BeautifulSoup(html,"html.parser")
    list = soup.findAll(name="li", attrs={"class" :"clearfix"})
    return list

#交大资讯更新推送
def push_jd():
    global xjd_last
    xjd_latest = get_xjd()
    new_msg = list(set(xjd_latest).difference(set(xjd_last))) #需要被推送更新的
    old_msg = list(set(xjd_last).difference(set(xjd_latest))) #需要被淘汰的信息
    if(new_msg != []):
        for msg in new_msg:
            pass #推送
        xjd_last = xjd_last-old_msg+new_msg

#图灵机器人
def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'   #改成你自己的图灵机器人的api，上图红框中的内容，不过用我的也无所谓，只是每天自动回复的消息条数有限
    data = {
        'key': 'fea3ffe3315a4798aa61bedf907908a0',  # Tuling Key
        'info': msg,  # 这是我们发出去的消息
        'userid': 'wechat-robot',  # 这里你想改什么都可以
    }
    # 我们通过如下命令发送一个post请求
    r = requests.post(apiUrl, data=data).json()
    return r.get('text')

#土味情话
def saylove():
    url = "http://api.tianapi.com/txapi/saylove/index?key=4dfffca8c9a947305f91ba5753a9994e"
    # print(url)
    response = requests.get(url)
    # print(response.text)
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
            for people in push_list:
                people["push_state"]:[False]
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
            user_name = itchat.search_friends(remarkName = people["remark_name"])[0]["UserName"]
            itchat.send_msg(content,toUserName=user_name)
            people["push_state"] = True




if __name__=="__main__":
    #研招网资讯推送列表
    xjd_last = get_xjd()

    #状态
    state = 0
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
            "remark_name":"szw",
            "neck_name":"泽泽", #绰号
            "push_state":[False],  #今日推送状态
            "push_id":[0] ,#订阅功能
            "city":"西安",
            "cityid":"101110101"
        },
        {
            # 亭
            "neck_name":"亭亭", #绰号
            "remark_name":"lyt",
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
