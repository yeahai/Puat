# 2023/2/8 19:10
# 你好，夜嗨大帅比
import socket
import re
# for i in range(3):
#     ip_str = input("请输入IP地址：")
#     i += 1
#     regular = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
#     if regular.match(ip_str):
#         print("您输入的ip地址合法！")
#     else:
#         print("您输入的ip地址不合法，请重新输入！")

url = input("请输入网址:")

regular = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
wangzhi = re.compile('[a-zA-z]+://[^\s]*')
if wangzhi.match(url) or regular.match(url):
    print("合法")
else:
    print("不合法")
