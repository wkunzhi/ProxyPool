# -*- coding: utf-8 -*-
# __author__ = zok 
# Email = 362416272@qq.com
# Date: 2019/3/9  Python: 3.7

import re

from utils.utils import get_page

"""
ProxyMetaClass为元类，实现了，自动获取并调用 方法名前缀为 crawl_的方法
"""


class ProxyMetaClass(type):
    """
    元类
    判断方法开头是否是crawl,是就将其加入__CrawlFunc__属性中
    """
    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k, v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__))'].append(k)  # 将方法名添加到 属性中
                count += 1
        attrs['__CrawlFuncCount__'] = count  # 方法数量
        return type.__new__(cls, name, bases, attrs)


class Crawler(object, metaclass=ProxyMetaClass):

    def get_proxies(self, callback):
        """
        获取代理
        :param callback:
        :return:
        """
        proxies = []
        for proxy in eval("self.{}()".format(callback)):
            print('成功获取到代理', proxy)
            proxies.append(proxy)
        return proxies

    def crawl_ip3366(self):
        for page in range(1, 4):
            start_url = 'http://www.ip3366.net/free/?stype=1&page={}'.format(page)
            html = get_page(start_url)
            ip_address = re.compile('<tr>\s*<td>(.*?)</td>\s*<td>(.*?)</td>')
            # \s * 匹配空格，起到换行作用
            re_ip_address = ip_address.findall(html)
            for address, port in re_ip_address:
                result = address + ':' + port
                yield result.replace(' ', '')

    def crawl_kuaidaili(self):
        for i in range(1, 4):
            start_url = 'http://www.kuaidaili.com/free/inha/{}/'.format(i)
            html = get_page(start_url)
            if html:
                ip_address = re.compile('<td data-title="IP">(.*?)</td>')
                re_ip_address = ip_address.findall(html)
                port = re.compile('<td data-title="PORT">(.*?)</td>')
                re_port = port.findall(html)
                for address, port in zip(re_ip_address, re_port):
                    address_port = address + ':' + port
                    yield address_port.replace(' ', '')
