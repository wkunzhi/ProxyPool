# -*- coding: utf-8 -*-
# __author__ = zok 
# Email = 362416272@qq.com
# Date: 2019/3/9  Python: 3.7
import sys

from db.redis_clent import RedisClient
from get_proxy.crawler import Crawler
from setting import *


class Getter(object):
    """
    将爬虫加入到数据库中
    """

    def __init__(self):
        self.redis = RedisClient()  # 实例化redis类
        self.crawler = Crawler()  # 实例化爬虫类

    def is_over_threshold(self):
        """
        判断是否达到了代理池限制
        """
        if self.redis.count() >= POOL_UPPER_THRESHOLD:
            return True
        else:
            return False

    def run(self):
        print('获取器开始执行')
        if not self.is_over_threshold():
            for callback_label in range(self.crawler.__CrawlFuncCount__):
                callback = self.crawler.__CrawlFunc__[callback_label]
                # 获取代理
                proxies = self.crawler.get_proxies(callback)
                sys.stdout.flush()  # 强制刷新缓冲区
                for proxy in proxies:
                    self.redis.add(proxy)


"""
__CrawlFuncCount__ 为ProxyMetaClass类，含有crawl_方法名的方法个数
__CrawlFunc__ 为ProxyMetaClass类，的方法名列表
ProxyMetaClass实现了，自动获取并调用 方法名前缀为 crawl_的方法
"""
