# coding=utf-8
import pymysql


class SaveData(object):
    def coneect(self):
        self.db = pymysql.connect(host="192.168.11.129", port=3306,user="root", passwd="123456", db="Movies")
    def save(self,name,star,releasetime,nation):

        cur=self.db.cursor()
        sql="insert into movieinfo (name,star,time,nation) values('"+name+"','"+star+"','"+releasetime+"','"+nation+"')"
        print(sql)

        try:
          cur.execute(sql)
          self.db.commit()
        except:
          self.db.rollback()

    def close(self):
       self.db.close()