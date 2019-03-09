# -*- coding: utf-8 -*-
# __author__ = zok 
# Email = 362416272@qq.com
# Date: 2019/3/9  Python: 3.7

# 代理测试API，抓什么网填什么
TEST_URL = 'http://www.baidu.com'

# 最大分值
MAX_SCORE = 100
# 最小分值
MIN_SCORE = 0
# 初始分值
INITIAL_SCORE = 10

# redis配置
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_PASSWORD = None
REDIS_KEY = 'proxies'  # redis有序集合键名

# 代理池最大IP承载量
POOL_UPPER_THRESHOLD = 10000

# 最大测试IP质量并发
BATCH_TEST_SIZE = 20

# 测试API，白名单响应
VALID_STATUS_CODES = [200, 302]

# 检查周期
TESTER_CYCLE = 20
# 获取周期
GETTER_CYCLE = 300

# API配置
API_HOST = '0.0.0.0'
API_PORT = 5555

# 开启测试
TESTER_ENABLED = True
# 开启获取ip
GETTER_ENABLED = True
# 开启API
API_ENABLED = True
