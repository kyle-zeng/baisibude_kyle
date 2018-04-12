# coding:utf-8

from lxml import etree
from BaisiCrawl import BaisiCrawl
from CrawlException import CrawlException
from ExcelUtils import ExcelUtils


class CrawlXpath(BaisiCrawl):

    def __init__(self):
        super(CrawlXpath, self).__init__()

    def parse_list(self, response):

        try:
            f = etree.HTML(response)
            contents = f.xpath('//*/div[@class="j-r-list"]/ul/li')
            # 解析
            for content in contents:
                nick_name = content.xpath('./div[@class="j-list-user"]/div[@class="u-txt"]/a/text()')
                push_date = content.xpath('./div[@class="j-list-user"]/div[@class="u-txt"]/span/text()')
                # j-r-list-c
                push_content = content.xpath('./div[@class="j-r-list-c"]/div[@class="j-r-list-c-desc"]/a/text()')
                push_img_url = content.xpath('./div[@class="j-r-list-c"]/div[@class="j-r-list-c-img"]/a/img/@data-original')

                nick_name = nick_name[0]
                push_date = push_date[0]
                push_content = push_content[0]
                push_img_url = push_img_url[0]

                self.content_info.append(nick_name)
                self.content_info.append(push_date)
                self.content_info.append(push_content)
                self.content_info.append(push_img_url)

                self.count = self.count + 1
                file_path = self.save_pic(nick_name, push_date, push_img_url)
                self.content_info.append(file_path)

                ExcelUtils.write_excel(self.excel, self.sheet_info, self.count, self.content_info, u'xpath_bs.xlsx')

                print '采集了{}条信息'.format(self.count)
                self.content_info = []
        except CrawlException as e1:
            raise e1
        except Exception as e2:
            # 异常抛出调用处处理
            ex = CrawlException('parse_list 解析爬取的列表数据，异常信息：{}'.format(e2.message))
            raise ex