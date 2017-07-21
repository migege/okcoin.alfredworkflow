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
    symbols = [
        {
            'name': 'BTC/CNY',
            'symbol': 0,
            'key_price': 'btcLast',
        },
        {
            'name': 'ETH/CNY',
            'symbol': 2,
            'key_price': 'ethLast',
        },
        {
            'name': 'LTC/CNY',
            'symbol': 1,
            'key_price': 'ltcLast',
        },
    ]

    link = 'https://www.okcoin.cn'

    fb = Feedback()
    for symbol in symbols:
        url = 'https://www.okcoin.cn/real/ticker.do?random=%s' % int(time.time() * 1000)
        headers = {
            'Host': 'www.okcoin.cn',
            'Referer': 'https://www.okcoin.cn/',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36',
        }
        data = {
            'symbol': symbol['symbol'],
        }

        try:
            r = requests.post(url, headers=headers, data=data)
            res = r.json()

            kwargs = {
                'name': symbol['name'],
                'price': res[symbol['key_price']],
                'low': res['low'],
                'high': res['high'],
                'change': res['change'],
                'coinBalance': res['coinBalance'],
                'money': res['money'],
                'changeSign': '+' if float(res['change']) > 0 else '-',
            }

            item = {
                'title': '{name}: {price} ({changeSign}{change}%)'.format(**kwargs),
                'subtitle': 'Low: {low}, High: {high}'.format(**kwargs),
                'arg': link,
            }
            fb.addItem(**item)
        except Exception, e:
            print 'EXCEPT:', e
            continue

    fb.output()


if __name__ == '__main__':
    run()
