#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 作者       : shengbw
# 创建时间    : 2022/1/11 13:39
# 文件名     : album_parser.py
# 软件       : PyCharm
# 邮箱       : ch_sheng5@163.com

from superparser.superparser import SuperParser
from superparser.util import handle_html


class AlbumParser(SuperParser):
    def __init__(self, cookie, album_url):
        self.cookie = cookie
        self.url = album_url
        self.selector = handle_html(self.cookie, self.url)

    def extract_pic_urls(self):
        # <img src="http://wx2.sinaimg.cn/wap180/76102133ly8fwr33wpn8fj20v90v9tbw.jpg" alt="" class="c">
        pic_list = self.selector.xpath('//div[@class="c"]//img/@src')
        for i, pic in enumerate(pic_list):
            if "?" in pic:
                pic = pic[:pic.index("?")]
            pic_list[i] = pic
        return pic_list