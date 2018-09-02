# coding=utf-8
class urlmanager(object):

    def __init__(self):
        self.new_url_list=set()
        self.old_url_list=set()

    def has_new_url(self):
        """
        return if there are new urls
        :return:
        """
        return len(self.new_url_list)!=0

    def get_new_url(self):
        """
        return a new url
        :return:
        """
        if self.has_new_url():
            new_url=self.new_url_list.pop()
            self.old_url_list.add(new_url)
            return new_url

    def add_new_url(self,url):
        """
        add a new url into new url list
        :param url: new url found
        :return:
        """
        if url not in self.new_url_list and url not in self.old_url_list:
            self.new_url_list.add(url)

    def add_new_urls(self,urls):
        if urls is  None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url)