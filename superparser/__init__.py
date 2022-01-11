#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 作者       : shengbw
# 创建时间    : 2022/1/11 12:13
# 文件名     : __init__.py.py
# 软件       : PyCharm
# 邮箱       : ch_sheng5@163.com
from superparser.index_parser import IndexParser
from superparser.page_parser import PageParser
from superparser.photo_parser import PhotoParser
from superparser.album_parser import AlbumParser

__all__ = [IndexParser, PageParser, PhotoParser, AlbumParser]