#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 作者       : shengbw
# 创建时间    : 2022/1/11 13:46
# 文件名     : mblog_picAll_parser.py
# 软件       : PyCharm
# 邮箱       : ch_sheng5@163.com
from superparser.superparser import SuperParser
from superparser.util import handle_html


class MblogPicAllParser(SuperParser):
    def __init__(self, cookie, weibo_id):
        self.cookie = cookie
        self.url = 'https://weibo.cn/mblog/picAll/' + weibo_id + '?rl=1'
        self.selector = handle_html(self.cookie, self.url)

    def extract_preview_picture_list(self):
        return self.selector.xpath('//img/@src')
