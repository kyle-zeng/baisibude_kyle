# coding:utf-8

from CrawlXpath import CrawlXpath


class Main(object):

    @staticmethod
    def query_data():
        print '开始爬取数据\n\n'
        crawl = CrawlXpath()
        crawl.get_html()

if __name__ == '__main__':
    Main().query_data()