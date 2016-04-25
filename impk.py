#!/usr/bin/env python3

import re
import random
import urllib.request
import urllib.parse
import time
import argparse

parser = argparse.ArgumentParser(description = 'impk刷分工具')
parser.add_argument('cookie' , help='cookie值' , type=str)
args = parser.parse_args()

while True:
    passage = random.choice((
        '不错不错233~~~',
        '有点儿看不懂',
        '羡慕羡慕233',
        '不错不错，同意',
        'Hello Boy~~~',
        '看爱情公寓中。。。',
        '妈蛋，什么情况。。',
        '我勒个去。。',
        '惊讶。。什么鬼～',
        '我还有什么话可说呢',
        '我就是来打酱油的',
        '什么时候才能有好多好多钱啊～～～'))
    cookie = {'Cookie':args.cookie}
    req = urllib.request.Request('http://bbs.impk.cc/Forum-134.php?type=dyn' , headers = cookie)
    html = urllib.request.urlopen(req).read().decode('gbk')
    time.sleep(1)
    regexp = re.compile(r'<A class="Topic" href="([^"]+?)" title="[^"]+?">')
    urls = regexp.findall(html)[10:]
    data = urllib.parse.urlencode({'content':passage.encode('gbk')})
    data = data.encode('gbk')
    url = random.choice(urls)
    print('发帖地址：http://bbs.impk.cc/%s' % url)
    print('回帖内容：%s' % passage)
    url = 'ReplyPost-' + url.split('-')[1] + '-' + url.split('-')[2].split('.')[0]
    url = 'http://bbs.impk.cc/' + url
    req = urllib.request.Request(url, method = 'POST' , headers = cookie , data = data)
    html = urllib.request.urlopen(req).read().decode('gbk')
    time.sleep(30)
