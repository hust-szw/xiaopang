# coding=utf-8
import itchat
from itchat.content import *
import threading
import datetime
import time
import requests
import json
from bs4 import BeautifulSoup
from demjson import *
#这里定义接收到消息所用方法
@itchat.msg_register(TEXT)
def msg_reply(msg):
    remark_name = decode(str(msg).replace("<","{").replace(">","}"))['User']['User']['RemarkName']
    info = msg['Text']
    global state
    if (state==0):
        if (info == "雨泽"):
            menu = "你好呀，我是雨泽小朋友，请问喊我有什么事？目前爸爸妈妈只教会了我以下技能哦~\n" \
                   "(你可以选择前面的序号让我来给你展示~)\n" \
                   "1：雨泽成长记录\n" \
                   "2：研招网消息查看\n"\
                   "3: 艾宾浩斯\n"
            state = 1
            return menu
        elif (info == "艾宾浩斯"):
            msg = "功能选择：\n" \
                  "1：输入今日学习任务\n" \
                  "2：查看近五日学习任务\n" \
                  "3：删除学习任务\n"
            state = 3
            return msg

        else:
            return get_response(info.encode('UTF-8'))
    if(state == 1):
        if(info =="1"):
            jieshao = "你好，我的名字叫邵雨泽~雨亭的雨，泽为的泽~你可以喊我雨泽！\n\n" \
                      "7月17日，我被爸爸妈妈带到了这个世界，好开心~\n\n" \
                      "7月24日，我学会了给爸爸妈妈汇报每日的天气情况，成为了爸爸妈妈的贴心小助手~\n\n" \
                      "7月27日，爸爸教会了我说话，他说这样他不在的时候我就可以陪着妈妈~\n\n" \
                      "8月13日，我可以帮爸爸妈妈查询和推送他们目标学校的考研信息啦~\n\n" \
                      "8月21日，我可以提醒爸爸妈妈用艾宾浩斯记忆曲线复习学习内容了~\n\n"
            state = 0
            return jieshao
        elif(info == "2"):
            msg = "请选择查看的学院：\n" \
                  "1：西北工业大学软件学院\n" \
                  "2：西安交通大学计算机学院\n"
            state = 2
            return msg
        elif (info == "3"):
            msg = "功能选择：\n" \
                  "1：输入今日学习任务\n" \
                  "2：查看近五日学习任务\n" \
                  "3：删除学习任务\n"
            state = 3
            return msg
        else:
            state = 0
            return("抱歉呦，雨泽还不会这项技能呢~")
    if (state == 2):
        if(info == "2"):
            return_msg = ""
            xjd_msg = get_xjd_msg()
            for i in range(10):
                return_msg =return_msg+xjd_msg[i]+"\n"
            state = 0
            return return_msg
        elif(info == "1"):
            return_msg = "招生公告信息：\n"
            xgd_msg1 = get_xgd_msg(1)
            xgd_msg2 = get_xgd_msg(2)
            for i in range(5):
                return_msg =return_msg+xgd_msg1[i]+"\n"
            return_msg = return_msg+"\n招生简章信息：\n"
            for i in range(5):
                return_msg = return_msg + xgd_msg2[i] + "\n"
            state = 0
            return return_msg
    if(state == 3):
        if(info == "1"):
            msg = "请输入学习任务："
            state = 4
            return msg
        elif(info == '2'):
            msg = "近五日学习任务如下：\n"
            for e in msgbox:
                if ((e["day"] < 5) & (remark_name == e["nickname"])):
                    msg = msg + str(e["day"]) + "天前：\n" + e["msg"] + "\n\n"
            state = 0
            return msg
        elif (info == '3'):
            msg = "学习任务如下："
            i = 0
            for e in msgbox:
                if ( remark_name == e["nickname"]):

                    msg = msg + str(i)+".\n"+str(e["day"]) + "天前：\n" + e["msg"] + "\n\n"
                    i= i+1
            state = 0
            msg= msg+"请输入需要删除的任务编号"
            state = 6
            return msg
        else:
            pass
    if (state == 4): #创建学习任务
        creatmsg(info,remark_name)
        state = 0
        return ("今日任务创建成功")
    if(state == 5): #查看学习任务
        msg = ""
        i = 1
        for e in msgbox:
            if ((e["day"] < 5) & (remark_name == e["nickname"])):
                msg = msg + str(e["day"]) + "天前：\n" + e["msg"] + "\n\n"
        state = 0
        return msg
    if (state == 6): #删除学习任务
        try:
            num = int(info)
        except:
            state = 0
            return "输入数字非法"
        if(num<0 or num>len(msgbox)-1):
            state = 0
            return "输入数字非法"
        else :
            try:
                msgbox.pop(num)
            except:
                state = 0
                return "删除失败"
            with open("msg.txt", "w+") as f:
                f.write(encode(msgbox))
            state = 0
            return "删除成功"

#获得交大研招网信息
def get_xjd():
    url = "http://yz.xjtu.edu.cn/index/zsdt.htm"
    res = requests.get(url)
    res.encoding = 'utf-8'
    html= res.text
    # print(html)
    soup = BeautifulSoup(html,"html.parser")
    list = soup.findAll(name="li", attrs={"class" :"clearfix"})
    for i in range(len(list)):
        list[i] = str(list[i])
    # global xjd_last
    # xjd_last = list
    return list

#艾宾浩斯提醒
def creatmsg(msg,nickname):
    global msgbox
    m = {
        "msg":msg,
        "nickname":nickname,
        "day":0
    }
    msgbox.append(m)
    with open("msg.txt","w+") as f:
        f.write(encode(msgbox))

def msg_daily_push():
    with open("msg.txt", "r+") as f:
        temp_msg = decode(f.read())
        for people in push_list:
            target = ""
            for msg in temp_msg:
                print(msg)
                if(msg['nickname']==people['remark_name']):
                    msg["day"]=msg["day"]+1
                    if(msg["day"]==1):
                        target = target + "\n第1次复习：\n"+msg['msg']+"\n"
                    elif(msg["day"]==3):
                        target = target + "\n第2次复习：\n" + msg['msg']+"\n"
                    elif (msg["day"] == 7):
                        target = target + "\n第3次复习：\n" + msg['msg'] + "\n"
                    elif (msg["day"] == 14):
                        target = target + "\n第4次复习：\n" + msg['msg'] + "\n"
                    elif (msg["day"] == 29):
                        target = target + "\n第5次复习：\n" + msg['msg'] + "\n"
                    elif(msg["day"] > 29):
                        temp_msg.remove(msg)
            if(target == ""):
                user_name = itchat.search_friends(remarkName=people["remark_name"])[0]["UserName"]
                itchat.send_msg("今日暂无学习任务", toUserName=user_name)
            else:
                user_name = itchat.search_friends(remarkName=people["remark_name"])[0]["UserName"]
                itchat.send_msg("今日学习任务如下：\n"+target, toUserName=user_name)
        with open("msg.txt", "w+") as f:
            f.write(encode(temp_msg))
        global msgbox
        msgbox = temp_msg
        print(temp_msg)

#交大资讯更新推送
def push_xjd():
    global xjd_last
    xjd_latest = get_xjd()
    new_msg = list(set(xjd_latest).difference(set(xjd_last))) #需要被推送更新的
    old_msg = list(set(xjd_last).difference(set(xjd_latest))) #需要被淘汰的信息
    push_msg = ""
    if(new_msg != []):
        push_msg ="您有新的院校信息：\n"
        for msg in new_msg:
            temp_msg = BeautifulSoup(msg,"html.parser").li.a
            title = str(temp_msg['title'])
            date = str(temp_msg.span.string)
            href = "http://yz.xjtu.edu.cn/"+str(temp_msg['href'])[3:]

            push_msg =  push_msg+"\n日期："+date+"\n" \
                        "标题："+title+"\n" \
                        "链接："+href+"\n"
            # print(push_msg)
        xjd_last = list((set(xjd_last)-set(old_msg))|set(new_msg))
    return push_msg

def xjd_daily_push():
    pushlist  = push_xjd()
    if(pushlist!=[]):
        for people in push_list:
            user_name = itchat.search_friends(remarkName=people["remark_name"])[0]["UserName"]
            itchat.send_msg(pushlist, toUserName=user_name)
def get_xjd_msg():
    i= 1
    msg_list = []
    get_list = get_xjd()
    for msg in get_list:
        temp_msg = BeautifulSoup(msg, "html.parser").li.a
        title = str(temp_msg['title'])
        date = str(temp_msg.span.string)
        href = "http://yz.xjtu.edu.cn/" + str(temp_msg['href'])[3:]
        print(href)

        push_msg =  "序号："+ str(i)+"\n" \
                    "日期：" + date + "\n" \
                    "标题：" + title + "\n" \
                    "链接：" + href + "\n"
        msg_list.append(push_msg)
        i=i+1
    return msg_list

#西工大消息推送
def get_xgd(index):
    if(index == 1): #招生公告
        url = "http://yzb.nwpu.edu.cn/new/sszs/zsgg.htm"
    elif(index == 2): #招生简章
        url = "http://yzb.nwpu.edu.cn/new/sszs/zsjz.htm"
    else:
        return []
    res = requests.get(url)
    res.encoding = 'utf-8'
    html= res.text
    soup = BeautifulSoup(html,"html.parser")
    tags = soup.find(attrs={"class":'col-md-9 col-sm-9 col-xs-12 cno-right'})
    list = tags.find_all(name = "li")
    for i in range(len(list)):
        list[i] = str(list[i])
    return list

def get_xgd_msg(index):
    i= 1
    msg_list = []
    get_list = get_xgd(index)
    for msg in get_list:
        temp_msg = BeautifulSoup(msg, "html.parser")
        title = str(temp_msg.a.string)
        date = str(temp_msg.span.string)
        href = "http://yzb.nwpu.edu.cn" + str(temp_msg.a["href"])[5:]
        # print(msg)
        # print(str(msg.a["href"]))

        push_msg =  "序号："+ str(i)+"\n" \
                    "日期：" + date + "\n" \
                    "标题：" + title + \
                    "链接：" + href + "\n"
        msg_list.append(push_msg)
        i=i+1
    return msg_list

def push_xgd():
    i = 1
    global xgd_last1,xgd_last2
    xgd_latest1 = get_xgd(1)
    xgd_latest2 = get_xgd(2)
    #招生公告
    new_msg1 = list(set(xgd_latest1).difference(set(xgd_last1))) #需要被推送更新的
    old_msg1 = list(set(xgd_last1).difference(set(xgd_latest1))) #需要被淘汰的信息
    #招生简章
    new_msg2 = list(set(xgd_latest2).difference(set(xgd_last2))) #需要被推送更新的
    old_msg2 = list(set(xgd_last2).difference(set(xgd_latest2))) #需要被淘汰的信息
    push_msg = ""
    if(new_msg1 != []):
        push_msg =push_msg + "您有新的招生公告及招生简章信息：\n"
        for msg in new_msg1:
            temp_msg = BeautifulSoup(msg, "html.parser")
            title = str(temp_msg.a.string)
            date = str(temp_msg.span.string)
            href = "http://yzb.nwpu.edu.cn" + str(temp_msg.a["href"])[5:]

            push_msg =  push_msg+\
                        "序号："+str(i)+"\n" \
                        "日期："+date+"\n" \
                        "标题："+title+ \
                        "链接："+href+"\n\n"
            i=i+1
            # print(push_msg)
        xgd_last1 = list((set(xgd_last1)-set(old_msg1))|set(new_msg1))

    if (new_msg2 != []):
        for msg in new_msg2:
            temp_msg = BeautifulSoup(msg, "html.parser")
            title = str(temp_msg.a.string)
            date = str(temp_msg.span.string)
            href = "http://yzb.nwpu.edu.cn" + str(temp_msg.a["href"])[5:]

            push_msg = push_msg + \
                       "序号：" + str(i) + "\n" \
                        "日期：" + date + "\n" \
                        "标题：" + title + \
                        "链接：" + href + "\n\n"
            i = i + 1
            # print(push_msg)
        xgd_last2 = list((set(xgd_last2) - set(old_msg2)) | set(new_msg2))
    return push_msg

def xgd_daily_push():
    pushlist  = push_xgd()
    if(pushlist!=[]):
        for people in push_list:
            user_name = itchat.search_friends(remarkName=people["remark_name"])[0]["UserName"]
            itchat.send_msg(pushlist, toUserName=user_name)


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
    i = 0
    while 1:
        now = datetime.datetime.now()
        now_str = now.strftime('%Y/%m/%d %H:%M:%S'[9:])
        #print('\r{}'.format(now_str),end='')
        for event in clock_enents:
            if((event['time']==now_str)):
                event['function']()
        if (now_str=="00:00:00"):#重置每条消息的推送状态
            for people in push_list:
                people["push_state"]=[False]
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
    try:
        xjd_last  = get_xjd()
        xgd_last1 = get_xgd(1)
        xgd_last2 = get_xgd(2)
    except:
        pass
    # 艾宾浩斯任务盒子
    with open("msg.txt", "r+") as f:
        textcontent =  str(f.read())
        if(textcontent!=""):
            msgbox = decode(textcontent)
        else:
            msgbox = []
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
        {
        "name":"xjd_daily_push",
        "id":1,
        "time":"12:00:00",
        "function":xjd_daily_push,
        },
        {
        "name": "xgd_daily_push",
        "id": 2,
        "time": "12:00:00",
        "function": xgd_daily_push,

        },
        {
        "name": "msg_daily_push",
        "id": 3,
        "time": "08:00:00",
        "function": msg_daily_push,
        }


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
