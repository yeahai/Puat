# 2022/12/31 19:05
# 你好，夜嗨大帅比
class Table(object):
    def __init__(self):
        self.eid = 0
        self.title = ''
        self.author = ''
        self.published_time = ''
        self.platform = ''
        self.exploit_type = ''
        self.exploit_url = ''
        self.download_url = ''

    def __str__(self):
        return f"{self.title},{self.eid},{self.author},{self.platform}," \
               f"{self.published_time},{self.download_url},{self.exploit_url},{self.exploit_type}"