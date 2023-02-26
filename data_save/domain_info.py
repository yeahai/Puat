# 2023/1/31 15:29
# 你好，夜嗨大帅比

import requests
from ua import headers
import re

class DomainInfo:
    def __init__(self,url):
        self.url = url

        self.file_path = "./" + self.url + "_.txt"

    def spider_ssl(self):
        url = "https://crt.sh/?q=" + self.url
        l = []
        response = requests.get(url,headers)
        html = response.text
        content = re.compile(r".[^ =]+" + self.url)
        co = content.findall(html)
        for i in co:
            i = i.replace('<TD>', "").replace('<BR>', "\n").strip()
            l.append(i)

        with open(self.file_path,'a+',encoding='utf8') as wf:
            for x in l: # 对数据进行去除多余符号
                x = x.replace("*.", "").replace("'", "")
                wf.write(x)
                wf.write('\n')

    def fuzz(self):
        save_path = "../store/" + self.url + ".txt"
        with open('../utils/dic.txt', 'r', encoding='utf8') as rf:
            key = rf.readline().strip()

            while key:
                url = "http://" + key + "." + self.url
                try:
                    response = requests.get(url,headers)
                    if response.status_code == 200:
                        with open(save_path,'a+',encoding='utf8') as af:
                            print("ok")
                            af.write(url + '\n')
                except:
                    pass
                key = rf.readline().strip()



    def Deduplication(self):
        mys = set()
        with open(self.file_path,"r",encoding="utf8") as rf:
            f = rf.readline()
            while f:
                mys.add(f)
                f = rf.readline()

            l = list(mys)
            with open(self.file_path,"w",encoding="utf8") as wf:
                for line in l:
                    wf.write(line)
if __name__ == '__main__':
    url = "baidu.com"
    Domain = DomainInfo(url)
    # Domain.spider_ssl()
    Domain.fuzz()