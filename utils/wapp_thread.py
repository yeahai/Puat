# 2023/2/9 12:24
# 你好，夜嗨大帅比
from PyQt5.QtCore import QThread,pyqtSignal
import requests

from data_save.ua import headers
from utils.wapp import Cms
from data_save.text import DB

class WappThreads(QThread):
    success = pyqtSignal(list)

    def __init__(self,window,url,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.url = url
        self.window = window
        self.sql = 'select * from exp_poc_info where title like {}'
        self.result = []

    def run(self):
        #
        try:
            html = requests.get(url=self.url, headers=headers, timeout=4)
            cms_result = Cms(html.url, html.text, html.headers).info().get("apps")
            db = DB()
            for i in cms_result:
                a = db.search_all(i)
                self.result.append(a)
            #     print(a)
            # print(cms_result)
        # print(1)

            self.success.emit(self.result)
        except:
            pass