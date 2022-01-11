#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 作者       : shengbw
# 创建时间    : 2022/1/11 10:19
# 文件名     : detetime_util.py
# 软件       : PyCharm
# 邮箱       : ch_sheng5@163.com
from datetime import datetime


def str_to_time(text):
    """将字符串转换成时间类型"""
    if ':' in text:
        result = datetime.strptime(text, '%Y-%m-%d %H:%M')
    else:
        result = datetime.strptime(text, '%Y-%m-%d')
    return result
