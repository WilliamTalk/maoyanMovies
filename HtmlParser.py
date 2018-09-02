# coding=utf-8
from bs4 import BeautifulSoup

class HtmlParser(object):


    def Downloader(self):
        pass
    def parser(self,content):
        soup=BeautifulSoup(content,"lxml")
        movies=soup.select("div.board-item-main")
        for movie in movies:
            name=movie.select("p.name")[0].string.strip()
            star = movie.select("p.star")[0].string.strip()
            releasetime = movie.select("p.releasetime")[0].string.strip()
            yield  name,star,releasetime[5:15],releasetime[16:18]
