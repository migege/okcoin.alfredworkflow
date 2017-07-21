#!/usr/bin/env python
# -*- coding:utf8 -*-
import sys
import os
import requests
import time
from alfred.feedback import Feedback

reload(sys)
sys.setdefaultencoding('utf8')


def run():
    try:
        url = 'https://www.okcoin.cn/real/ticker.do?random=%s' % int(time.time() * 1000)
        headers = {
            'Host': 'www.okcoin.cn',
            'Referer': 'https://www.okcoin.cn/',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36',
        }
        data = {
            'symbol': 1,
        }
        link = 'https://www.okcoin.cn'

        r = requests.post(url, headers=headers, data=data)
        res = r.json()

        rows = []
        rows.append({'name': 'BTC/CNY', 'price': res['btcLast']})
        rows.append({'name': 'ETH/CNY', 'price': res['ethLast']})
        rows.append({'name': 'LTC/CNY', 'price': res['ltcLast']})

        fb = Feedback()
        for row in rows:
            kwargs = {'title': '{name}: {price}'.format(**row), 'subtitle': '', 'arg': link}
            fb.addItem(**kwargs)
        fb.output()
    except Exception, e:
        print 'EXCEPT:', e
        pass


if __name__ == '__main__':
    run()
