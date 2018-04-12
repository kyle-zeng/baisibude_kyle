# coding:utf-8

import abc
import os
import time
import urllib2, urllib
from ExcelUtils import ExcelUtils
from CrawlException import CrawlException


class BaisiCrawl(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.row_title = [u'发布者昵称',u'发布时间',u'发布内容',u'发布图片', u'本地路径']
        sheet_name = u'baisibudejie_动态'
        return_excel = ExcelUtils.create_excel(sheet_name, self.row_title)
        self.excel = return_excel[0]
        self.sheet_info = return_excel[1]
        self.content_info = []
        self.count = 0

    def get_html(self):

        try:
            for i in range(1, 3):
                url = 'http://www.budejie.com/pic/{0}'.format(i)
                headers ={
                    'Referer': 'http://www.budejie.com/',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4549.400 QQBrowser/9.7.12900.400'
                }

                req = urllib2.Request(url, headers=headers)
                response = urllib2.urlopen(req).read()
                self.parse_list(response)

                time.sleep(1)
        except CrawlException as e1:
            raise e1
        except Exception as e:
            print '\n\n出现错误,错误信息是:{}\n\n'.format(e.message)

    def save_pic(self, nick_name, push_data, img_url):

        filename = u'{}_{}.jpg'.format(nick_name, filter(str.isdigit, push_data))
        try:
            tag = push_data[0:10]
            img_path = u'F:/python/pic/{}'.format(tag)

            if not os.path.exists(img_path):
                os.makedirs(img_path)
                print  img_path + u' 创建成功'

            with open(img_path + '/' + filename, 'wb') as f:
                f.write(urllib.urlopen(img_url).read())

            return u'{}/{}'.format(img_path, filename)
        except CrawlException as e1:
            raise e1
        except Exception as e:
            ex = CrawlException('save_pic 保存图片出现错误,错误信息是：{}'.format(e.message))
            raise ex

    @abc.abstractmethod
    def parse_list(self, response):

        pass