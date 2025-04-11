# config.py 自定义配置,包括阅读次数、推送token的填写
import os
import re

"""
可修改区域
默认使用本地值如果不存在从环境变量中获取值
"""

# 阅读次数 默认120次/60分钟
READ_NUM = int(os.getenv('READ_NUM') or 120)
# 需要推送时可选，可选pushplus、wxpusher、telegram
PUSH_METHOD = "" or os.getenv('PUSH_METHOD')
# pushplus推送时需填
PUSHPLUS_TOKEN = "" or os.getenv("PUSHPLUS_TOKEN")
# telegram推送时需填
TELEGRAM_BOT_TOKEN = "" or os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = "" or os.getenv("TELEGRAM_CHAT_ID")
# wxpusher推送时需填
WXPUSHER_SPT = "" or os.getenv("WXPUSHER_SPT")
# read接口的bash命令，本地部署时可对应替换headers、cookies
curl_str = os.getenv('WXREAD_CURL_BASH')

# headers、cookies是一个省略模版，本地或者docker部署时对应替换
cookies = {}
headers = {}


"""
建议保留区域|默认读三体，其它书籍自行测试时间是否增加
"""
data = {
    "appId": "wb115321887466h1181663836",
    "b": "2bb32ff0813ab6ffcg014315",
    "c": "70532b302e3705f21728e67",
    "ci": 9,
    "co": 2039,
    "sm": "而促进其内部的分解。也必须这样，才能真正",
    "pr": 6,
    "rt": 30,
    "ts": 1743077298355,
    "rn": 867,
    "sg": "c364f27bde3fbb4ecbb28ec9f932db5928b157cfa98c7bd50b14b10c4597bae3",
    "ct": 1743077298,
    "ps": "f8032ca07a63b98bg01277b",
    "pc": "04a326807a63b98bg0138c9",
    "s": "b0b9136a",
}

# 章节内位置，对应参数co
cos = [389,609,745,803,981,1154]

# 章节目录，每个数组内参数依次为ci、c、pr
# 这里的书籍，参数b="2bb32ff0813ab6ffcg014315"
chapters = [
    [4,  "bcb32dd02debcbe3365eb9c", 0],
    [5, "115328e02df115f89503b27", 0],
    [6, "13f32f302e013fe9d843f64", 0],
    [7, "d1c32af02e1d1c38a09a24a", 0],
    [8, "9cf32d102e29cfdf10e885f", 0],
    [9, "70532b302e3705f21728e67", 0],
    [10, "74d32eb02e474db120f0d68", 0],
    [11, "57a32cf02e557aeee35c5bc", 0],
    [12, "6da325702e66da9003b7590", 0],
    [13, "9b0329402e79b04d15288d0", 0]
]


def convert(curl_command):
    """提取bash接口中的headers与cookies
    支持 -H 'Cookie: xxx' 和 -b 'xxx' 两种方式的cookie提取
    """
    # 提取 headers
    headers_temp = {}
    for match in re.findall(r"-H '([^:]+): ([^']+)'", curl_command):
        headers_temp[match[0]] = match[1]

    # 提取 cookies
    cookies = {}
    
    # 从 -H 'Cookie: xxx' 提取
    cookie_header = next((v for k, v in headers_temp.items() 
                         if k.lower() == 'cookie'), '')
    
    # 从 -b 'xxx' 提取
    cookie_b = re.search(r"-b '([^']+)'", curl_command)
    cookie_string = cookie_b.group(1) if cookie_b else cookie_header
    
    # 解析 cookie 字符串
    if cookie_string:
        for cookie in cookie_string.split('; '):
            if '=' in cookie:
                key, value = cookie.split('=', 1)
                cookies[key.strip()] = value.strip()
    
    # 移除 headers 中的 Cookie/cookie
    headers = {k: v for k, v in headers_temp.items() 
              if k.lower() != 'cookie'}

    return headers, cookies


headers, cookies = convert(curl_str) if curl_str else (headers, cookies)
