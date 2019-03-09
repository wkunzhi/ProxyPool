# 自建代理池系统

- pip3 install asyncio
- pip3 install aiohttp
- pip3 install flask
- python3.7
> 以轻量级Flask作为服务端，提供接口调用

### 安装之后启动redis服务

### 配置代理池
`vim setting.py`

### 依赖安装
`pip3 install -r requirements.txt`

### 启动
`python3 run.py`

### 调用获取可用ip
```python
import requests

PROXY_POOL_URL = 'http://localhost:5555/random'  # 自己服务器网址

def get_proxy():
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        return None
```