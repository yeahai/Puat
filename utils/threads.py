# 2023/1/31 15:32
# 你好，夜嗨大帅比

from PyQt5.QtCore import QThread,pyqtSignal
import requests
import re
import socket
from requests.adapters import HTTPAdapter

from data_save.ua import headers
import pandas as pd

class NewTaskThread(QThread):
    # 信号,触发信号，更新窗体中的数据
    success = pyqtSignal(str,str)
    error = pyqtSignal(str,str)
    #
    def __init__(self,window,url,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.url = url
        self.window = window
        self.file_path = "../store/" + self.url + "_.txt"
        self.save_path = "../store/" + self.url + ".txt"

    def run(self):
        """具体线程应该做的事"""

        # 忽略警告
        requests.packages.urllib3.disable_warnings()

        import time
        import random

        with open('E:\\pythonProject1\\run_code\\utils\\dic1.txt', 'r', encoding='utf8') as rf:
            key = rf.readline().strip()

            while key:
                url = "http://" + key + "." + self.url
                try:
                    sess = requests.Session()
                    sess.mount('http://',HTTPAdapter(max_retries=3))
                    sess.mount('https://',HTTPAdapter(max_retries=3))
                    response = requests.get(url,headers,verify=False,timeout=1)
                    sess.keep_alive = False
                    if response.status_code == 200:
                        ip = socket.gethostbyname(url[7:].strip())
                        self.success.emit(ip,url)
                        with open(self.save_path,'a+',encoding='utf8') as af:
                            af.write(url + '\n')
                        response.close()
                        time.sleep(3)
                except Exception as e:
                    print(e)
                key = rf.readline().strip()

        # ok ------------------------------------

        # url = "https://crt.sh/?q=" + self.url
        # mySet = set()
        # response = requests.get(url, headers)
        # html = response.text
        # content = re.compile(r".[^ =]+" + self.url)
        # co = content.findall(html)
        # for i in co:
        #     i = i.replace('<TD>', "").replace('<BR>', "\n").strip()
        #     mySet.add(i)
        #
        # l = list(mySet)
        # with open(self.file_path, 'a+', encoding='utf8') as wf:
        #     for x in l:  # 对数据进行去除多余符号
        #         x = x.replace("*.", "").replace("'", "")
        #         wf.write(x)
        #         wf.write('\n')















            # with open("../store/a.txt",mode="a",encoding="utf8") as af:
            #     print(2)
            #     af.write(str(self.row_index) + self.url + "\n")
            #     print(3)
        # print(1)
        # with open('dic.txt', mode='r', encoding='utf8') as rf:
        #     print(11)
        #     key = rf.readline().strip()
        #     print(2)
        #     while key:
        #         print(3)
        #         url = key + "." + self.url
        #         try:
        #             print(4)
        #             response = requests.get(url)
        #             if response.status_code == 200:
        #                 self.success.emit(self.row_index,url)
        #                 with open(self.save_path, 'a+', encoding='utf8') as af:
        #                     af.write(url + '\n')
        #                     print(5)
        #         except Exception as e:
        #             self.error.emit(self.row_index,str(e))
        #         key = rf.readline().strip()
        #         print(6)

    # def __del__(self):
    #     self.wait()













# class NewTaskThread(QThread):
#     # 信号,触发信号，更新窗体中的数据
#     success = pyqtSignal(int,str)
#     error = pyqtSignal(int,str)

    # def __init__(self,window,row_index,url,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     self.url = url
    #     self.row_index = row_index
        # self.file_path = "./" + self.url + "_.txt"
        # self.save_path = "../store/" + self.url + ".txt"

    # def run(self):
        """具体线程应该做的事"""
        # self.success.emit(self.row_index,self.url)

        # with open('dic1.txt','r', encoding='utf8') as rf:
        #     key = rf.readline().strip()
        #     self.success.emit(self.row_index,key)
            # while key:
            #     url = key + "." + self.url


        # self.success.emit(1,"xxx")
        # print("1111")
        # with open('dic.txt', 'r', encoding='utf8') as rf:
        #     key = rf.readline().strip()
        #     while key:
        #         url = key + "." + self.url
        #         try:
        #             response = requests.get(url, headers)
        #             if response.status_code == 200:
        #                 self.success.emit(self.row_index,url)
        #                 with open(self.save_path, 'a+', encoding='utf8') as af:
        #                     af.write(url + '\n')
        #         except Exception as e:
        #             self.error.emit(self.row_index,str(e))
        #         key = rf.readline().strip()

    # def __del__(self):
    #     self.wait()

# if __name__ == '__main__':
#     d =