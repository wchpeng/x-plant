import requests


def alarm(msg):
    # 企业微信 webhook 报警
    url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=4fsdfsdfsdfsdfbbe0-03d223cee'
    jsn = {"msgtype": "text", "text": {"content": msg}}
    requests.post(url, json=jsn)


if __name__ == '__main__':
    import asyncio
    alarm('测试请求2')
