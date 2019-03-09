# -*- coding: utf-8 -*-
# __author__ = zok 
# Email = 362416272@qq.com
# Date: 2019/3/9  Python: 3.7


class PoolEmptyError(Exception):

    def __init__(self):
        Exception.__init__(self)

    def __str__(self):
        return repr('代理池干了..该进货了')
