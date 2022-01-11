#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 作者       : shengbw
# 创建时间    : 2022/1/11 10:15
# 文件名     : writer.py
# 软件       : PyCharm
# 邮箱       : ch_sheng5@163.com
from abc import ABC, abstractmethod


class Writer(ABC):
    def __init__(self):
        """根据需要，初始化结果路径、初始化表头、初始化数据库等"""
        pass

    @abstractmethod
    def write_weibo(self, weibo):
        """给定微博信息，写入对应文本或数据库"""
        pass

    @abstractmethod
    def write_user(self, user):
        """给定用户信息，写入对应文本或数据库"""
        pass
