#coding=utf-8

from HtmlParser import HtmlParser
from SaveData import SaveData
import  requests

class SpiderManager:

    def __init__(self):
        self.parser=HtmlParser()
        self.save=SaveData()

    def prcocess(self):
        self.save.coneect()
        for page in range(10):
            url="http://maoyan.com/board/4?offset="+str(page*10)
            res=requests.get(url)
            if res.status_code==200:
                movies=self.parser.parser(res.text)
                for name,star,releasetime,nation in movies:
                    self.save.save(name,star,releasetime,nation)
        self.save.close()

if __name__=="__main__":
    s=SpiderManager()
    s.prcocess()
