import requests
import json
from bs4 import BeautifulSoup
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



# def get_xjd():
#     url = "http://yz.xjtu.edu.cn/index/zsdt.htm"
#     res = requests.get(url)
#     res.encoding = 'utf-8'
#     html= res.text
#     # print(html)
#     soup = BeautifulSoup(html,"html.parser")
#     list = soup.findAll(name="li", attrs={"class" :"clearfix"})
#     for i in range(len(list)):
#         list[i] = str(list[i])
#     # global xjd_last
#     # xjd_last = list
#     return list


# xjd_last = get_xjd()
#
# xjd_last[0] = str('<li class="clearfix" id="line_u7_0">\n' \
#               '<a href="../info/1082/3104.htm" target="_blank" title="西安通大学2021年硕士研究生招生复试录取工作方案">\n' \
#               '<span class="date fr">2021-03-19</span>西安交通大学2021年硕士研究生招生复试录取工作方案</a>\n' \
#               '</li>')
# print(get_xjd()[0] == xjd_last[0])



# def push_xjd():
#     global xjd_last
#     xjd_latest = get_xjd()
#     new_msg = list(set(xjd_latest).difference(set(xjd_last))) #需要被推送更新的
#     old_msg = list(set(xjd_last).difference(set(xjd_latest))) #需要被淘汰的信息
#
#     if(new_msg != []):
#         for msg in new_msg:
#             temp_msg = BeautifulSoup(msg,"html.parser").li.a
#             title = str(temp_msg['title'])
#             date = str(temp_msg.span.string)
#             href = "http://yz.xjtu.edu.cn/"+str(temp_msg['href'])[3:]
#
#             push_msg =  "您有一条新的院校信息：\n" \
#                         "日期："+date+"\n" \
#                         "标题："+title+"\n" \
#                         "链接："+href+"\n"
#             print(push_msg)
#         xjd_last = list((set(xjd_last)-set(old_msg))|set(new_msg))

# def get_xjd_msg():
#     i= 1
#     msg_list = []
#     get_list = get_xjd()
#     for msg in get_list:
#         temp_msg = BeautifulSoup(msg, "html.parser").li.a
#         title = str(temp_msg['title'])
#         date = str(temp_msg.span.string)
#         href = "http://yz.xjtu.edu.cn/" + str(temp_msg['href'])[3:]
#         # print(href)
#
#         push_msg =  "序号："+ str(i)+"\n" \
#                     "日期：" + date + "\n" \
#                     "标题：" + title + "\n" \
#                     "链接：" + href + "\n"
#         msg_list.append(push_msg)
#         i=i+1
#     return msg_list
# def get_xgd(index):
#     if(index == 1): #招生公告
#         url = "http://yzb.nwpu.edu.cn/new/sszs/zsgg.htm"
#     elif(index == 2): #招生简章
#         url = "http://yzb.nwpu.edu.cn/new/sszs/zsjz.htm"
#     else:
#         return []
#     res = requests.get(url)
#     res.encoding = 'utf-8'
#     html= res.text
#     soup = BeautifulSoup(html,"html.parser")
#     tags = soup.find(attrs={"class":'col-md-9 col-sm-9 col-xs-12 cno-right'})
#     list = tags.find_all(name = "li")
#     for i in range(len(list)):
#         list[i] = str(list[i])
#     return list
#
# def get_xgd_msg(index):
#     i= 1
#     msg_list = []
#     get_list = get_xgd(index)
#     for msg in get_list:
#         temp_msg = BeautifulSoup(msg, "html.parser")
#         title = str(temp_msg.a.string)
#         date = str(temp_msg.span.string)
#         href = "http://yzb.nwpu.edu.cn" + str(temp_msg.a["href"])[5:]
#         # print(msg)
#         # print(str(msg.a["href"]))
#
#         push_msg =  "序号："+ str(i)+"\n" \
#                     "日期：" + date + "\n" \
#                     "标题：" + title + "\n" \
#                     "链接：" + href + "\n"
#         msg_list.append(push_msg)
#         i=i+1
#     return msg_list
#
# def push_xgd():
#     i = 1
#     global xgd_last1,xgd_last2
#     xgd_latest1 = get_xgd(1)
#     xgd_latest2 = get_xgd(2)
#     #招生公告
#     new_msg1 = list(set(xgd_latest1).difference(set(xgd_last1))) #需要被推送更新的
#     old_msg1 = list(set(xgd_last1).difference(set(xgd_latest1))) #需要被淘汰的信息
#     #招生简章
#     new_msg2 = list(set(xgd_latest2).difference(set(xgd_last2))) #需要被推送更新的
#     old_msg2 = list(set(xgd_last2).difference(set(xgd_latest2))) #需要被淘汰的信息
#     push_msg = ""
#     if(new_msg1 != []):
#         push_msg =push_msg + "您有新的招生公告及招生简章信息：\n"
#         for msg in new_msg1:
#             temp_msg = BeautifulSoup(msg, "html.parser")
#             title = str(temp_msg.a.string)
#             date = str(temp_msg.span.string)
#             href = "http://yzb.nwpu.edu.cn" + str(temp_msg.a["href"])[5:]
#
#             push_msg =  push_msg+\
#                         "序号："+str(i)+"\n" \
#                         "日期："+date+"\n" \
#                         "标题："+title+ \
#                         "链接："+href+"\n\n"
#             i=i+1
#             # print(push_msg)
#         xgd_last1 = list((set(xgd_last1)-set(old_msg1))|set(new_msg1))
#
#     if (new_msg2 != []):
#         for msg in new_msg2:
#             temp_msg = BeautifulSoup(msg, "html.parser")
#             title = str(temp_msg.a.string)
#             date = str(temp_msg.span.string)
#             href = "http://yzb.nwpu.edu.cn" + str(temp_msg.a["href"])[5:]
#
#             push_msg = push_msg + \
#                        "序号：" + str(i) + "\n" \
#                         "日期：" + date + "\n" \
#                         "标题：" + title + \
#                         "链接：" + href + "\n\n"
#             i = i + 1
#             # print(push_msg)
#         xgd_last2 = list((set(xgd_last2) - set(old_msg2)) | set(new_msg2))
#     return push_msg
#
# xgd_last1 =  get_xgd(1)
# xgd_last2 =  get_xgd(2)
# print(xgd_last2)
# xgd_last1[0] = str('<li><span>2021-07-01</span><a href="../../info/1174/7905.htm">关于发放2021级硕士研究生录取通知书的通知\r\n</a> </li>')
# xgd_last2[0] = str('<li><span>2020-10-20</span><a href="../../info/1175/7655.htm">  2021年单独命题入学考试招生简章 \r\n</a> </li>')
# print(push_xgd())
import json
# from demjson import *
# # msgbox = []
# #
# # def creatmsg(msg,nickname):
# #     global msgbox
# #     m = {
# #         "msg":msg,
# #         "nickname":nickname,
# #         "day":0
# #     }
# #     msgbox.append(m)
# #     with open("msg.txt","w+") as f:
# #         f.write(encode(msgbox))
# #
# # def msg_daily_push():
# #     with open("msg.txt", "r+") as f:
# #         temp_msg = decode(f.read())
# #         for msg in temp_msg:
# #             print(msg)
# #             msg["day"]=msg["day"]+1
# #             if(msg["day"]==1):
# #                 print(1)
# #             elif(msg["day"]==2):
# #                 print(2)
# #             elif (msg["day"] == 3):
# #                 print(3)
# #             elif (msg["day"] == 4):
# #                 print(4)
# #             elif (msg["day"] == 5):
# #                 temp_msg.remove(msg)
# #         with open("msg.txt", "w+") as f:
# #             f.write(encode(temp_msg))
# #         global msgbox
# #         msgbox = temp_msg
# #         print(temp_msg)
# # creatmsg("szw","1314")
# # msg_daily_push()
# # creatmsg("lyt","1314")
# # msg_daily_push()
# # msg_daily_push()
# # msg_daily_push()
# # msg_daily_push()
from demjson import *
a = "{'MsgId': '1297252672273560629', 'FromUserName': '@717c84132424761a3e13775f3ed8fa12b223b5df7c33fe9d3c9299e0d5f3b78d', 'ToUserName': '@ed82706fa3b1642bf1d905d325efac7cbed2ff7910b02e39bf0b05b1b0334626', 'MsgType': 1, 'Content': '。', 'Status': 3, 'ImgStatus': 1, 'CreateTime': 1629529861, 'VoiceLength': 0, 'PlayLength': 0, 'FileName': '', 'FileSize': '', 'MediaId': '', 'Url': '', 'AppMsgType': 0, 'StatusNotifyCode': 0, 'StatusNotifyUserName': '', 'RecommendInfo': {'UserName': '', 'NickName': '', 'QQNum': 0, 'Province': '', 'City': '', 'Content': '', 'Signature': '', 'Alias': '', 'Scene': 0, 'VerifyFlag': 0, 'AttrStatus': 0, 'Sex': 0, 'Ticket': '', 'OpCode': 0}, 'ForwardFlag': 0, 'AppInfo': {'AppID': '', 'Type': 0}, 'HasProductId': 0, 'Ticket': '', 'ImgHeight': 0, 'ImgWidth': 0, 'SubMsgType': 0, 'NewMsgId': 1297252672273560629, 'OriContent': '', 'EncryFileName': '', 'User': <User: {'MemberList': <ContactList: []>, 'Uin': 0, 'UserName': '@717c84132424761a3e13775f3ed8fa12b223b5df7c33fe9d3c9299e0d5f3b78d', 'NickName': 'shallwe', 'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgeticon?seq=709550538&username=@717c84132424761a3e13775f3ed8fa12b223b5df7c33fe9d3c9299e0d5f3b78d&skey=', 'ContactFlag': 1, 'MemberCount': 0, 'RemarkName': 'szw', 'HideInputBarFlag': 0, 'Sex': 1, 'Signature': '', 'VerifyFlag': 0, 'OwnerUin': 0, 'PYInitial': 'SHALLWE', 'PYQuanPin': 'shallwe', 'RemarkPYInitial': 'SZW', 'RemarkPYQuanPin': 'szw', 'StarFriend': 0, 'AppAccountFlag': 0, 'Statues': 0, 'AttrStatus': 233765, 'Province': '陕西', 'City': '汉中', 'Alias': '', 'SnsFlag': 0, 'UniFriend': 0, 'DisplayName': '', 'ChatRoomId': 0, 'KeyWord': '', 'EncryChatRoomId': '', 'IsOwner': 0}>, 'Type': 'Text', 'Text': '。'}"

print(decode(a.replace("<","{").replace(">","}"))['User']['User']['RemarkName'])