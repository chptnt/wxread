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
cookies = {
    'RK': 'oxEY1bTnXf',
    'ptcz': '53e3b35a9486dd63c4d06430b05aa169402117fc407dc5cc9329b41e59f62e2b',
    'pac_uid': '0_e63870bcecc18',
    'iip': '0',
    '_qimei_uuid42': '183070d3135100ee797b08bc922054dc3062834291',
    'wr_avatar': 'https%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FeEOpSbFh2Mb1bUxMW9Y3FRPfXwWvOLaNlsjWIkcKeeNg6vlVS5kOVuhNKGQ1M8zaggLqMPmpE5qIUdqEXlQgYg%2F132',
    'wr_gender': '0',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ko;q=0.5',
    'baggage': 'sentry-environment=production,sentry-release=dev-1730698697208,sentry-public_key=ed67ed71f7804a038e898ba54bd66e44,sentry-trace_id=1ff5a0725f8841088b42f97109c45862',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
}


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


def convert(curl_command):
    """提取bash接口中的headers与cookies"""
    # 提取 headers
    for match in re.findall(r"-H '([^:]+): ([^']+)'", curl_command):
        headers[match[0]] = match[1]

    # 提取 cookies
    cookies = {}
    cookie_string = headers.pop('cookie', '')
    for cookie in cookie_string.split('; '):
        key, value = cookie.split('=', 1)
        cookies[key] = value

    return headers, cookies


headers, cookies = convert(curl_str) if curl_str else (headers, cookies)
