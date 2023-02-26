# 2022/12/31 18:33
# 你好，夜嗨大帅比

import pymysql

insert = "insert into exp_poc_info (id,title,exploit_type,exploit_url,platform,author,published_time,download_url) values('%s', '%s' '%s' '%s' '%s' '%s' '%s' '%s')"
# insert = "insert into exp_poc_info values('%s', '%s' '%s' '%s' '%s' '%s' '%s' '%s')"

query_one = "select * from exp_poc_info where id=%s"
class DB(object):
    def __init__(self):
        try:
            self.conn = pymysql.connect(
                host='localhost',
                port=3306,
                user='root',
                password='root',
                db='exploit_info',
                charset='utf8'
            )
        except pymysql.Error as e:
            print("Error %d: %s" % (e.args[0],e.args[1]))
            exit()
        self.cursor = self.conn.cursor() # 创建游标

    # 增加信息
    def add_data(self,data):
        try:
            self.cursor.execute("insert into exp_poc_info (id,title,exploit_type,exploit_url,platform,author,published_time,download_url) values(%s,%s,%s,%s,%s,%s,%s,%s)",data)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print("Error",e.args[0])


    # 修改信息
    def update_data(self, sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print("Error",e.args[0])
    # 删除数据
    def del_data(self, sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print("Error", e.args[0])

    # 查询一条数据
    # 在搜索框中输入类似 id=1,title=xxx ,收到数据后利用分隔符分割然后变成k-v select k1，k2 from 表 where id=v1，title=v2
    def search_one(self,sql,Param=None):
        try:
            self.cursor.execute(sql,Param)
            res = self.cursor.fetchone()
        except Exception as e:
            return "Error" + e.args[0]

        return res
    # 是否存在相同的eid
    def is_exist_eid(self,eid):
        mysql_id = self.search_one('select id from exp_poc_info where id=%s',eid)
        if mysql_id is None:
            # return True
            return False
        else:
            return True

    # 查询所有信息
    def search_all(self,where=None):
        try:
            if where is None:
                self.cursor.execute("select * from exp_poc_info")
                res = self.cursor.fetchall()
            else:
                s='''select * from exp_poc_info where lower(title) like "%%"%s"%%"'''
                where_str = where.lower()
                self.cursor.execute(s,where_str)
                res = self.cursor.fetchall()

        except Exception as e:
            return "Error" + e.args[0]

        for r in res:
            yield r

    # 关闭游标和数据库连接
    def __del__(self):
        self.cursor.close()
        self.conn.close()

















