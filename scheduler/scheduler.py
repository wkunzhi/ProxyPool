# -*- coding: utf-8 -*-
# __author__ = zok 
# Email = 362416272@qq.com
# Date: 2019/3/9  Python: 3.7

import time
from multiprocessing import Process
from web_api.api import app
from get_proxy.getter import Getter
from check.check_proxy import Tester
from setting import *


class Scheduler(object):
    def schedule_tester(self, cycle=TESTER_CYCLE):
        """
        定时测试代理
        """
        tester = Tester()
        while True:
            print('测试器开始运行')
            tester.run()
            time.sleep(cycle)

    def schedule_getter(self, cycle=GETTER_CYCLE):
        """
        定时获取代理
        """
        getter = Getter()
        while True:
            print('开始抓取代理')
            getter.run()
            time.sleep(cycle)

    def schedule_api(self):
        """
        开启API
        """
        app.run(API_HOST, API_PORT)

    def run(self):
        print('代理池开始运行')

        if TESTER_ENABLED:  # 检测模块
            tester_process = Process(target=self.schedule_tester)
            tester_process.start()

        if GETTER_ENABLED:  # 获取模块
            getter_process = Process(target=self.schedule_getter)
            getter_process.start()

        if API_ENABLED:  # webAPI模块
            api_process = Process(target=self.schedule_api)
            api_process.start()
