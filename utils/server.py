import requests

from utils.utils import w_log


class Server:
    def __init__(self, config: dict):
        key = config['push']['serverChan']['key']
        if key:
            self.key = key
        else:
            self.key = None

        self.host = 'sctapi.ftqq.com'

    def send(self, title) -> tuple:
        url = 'https://' + self.host + '/' + self.key + '.send'

        header = {
            'Content-Type': 'application/json;charset=utf-8',
        }

        try:
            r = requests.post(url, json={'title': title}, headers=header)
            res = r.json()
        except Exception as e:
            w_log('推送异常： ' + str(e))
        else:
            if not res.get('code'):
                w_log('推送请求发送成功')
                data = res.get('data')
                return data.get('pushid'), data.get('readkey')
            w_log('推送出错： ' + res.get('info'))




