#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 作者       : shengbw
# 创建时间    : 2022/1/11 13:45
# 文件名     : info_parser.py
# 软件       : PyCharm
# 邮箱       : ch_sheng5@163.com

import os,sys
sys.path.append(os.getcwd())


import logging
import sys

from user import User
from superparser.superparser import SuperParser
from superparser.util import handle_html

logger = logging.getLogger('spider.info_parser')


class InfoParser(SuperParser):
    def __init__(self, cookie, user_id):
        self.cookie = cookie
        self.url = 'https://weibo.cn/%s/info' % (user_id)
        self.selector = handle_html(self.cookie, self.url)

    # 网页数据分析
    def extract_user_info(self):
        """提取用户信息"""
        try:
            user = User()
            nickname = self.selector.xpath('//title/text()')[0]
            nickname = nickname[:-3]
            if nickname == u'登录 - 新' or nickname == u'新浪':
                logger.warning(u'cookie错误或已过期,请按照README中方法 https://weibo.cn 重新获取 ')
                sys.exit()
            user.nickname = nickname

            basic_info = self.selector.xpath("//div[@class='c'][3]/text()")
            zh_list = [u'性别', u'地区', u'生日', u'简介', u'认证', u'达人']
            en_list = [
                'gender', 'location', 'birthday', 'description',
                'verified_reason', 'talent'
            ]
            for i in basic_info:
                if i.split(':', 1)[0] in zh_list:
                    setattr(user, en_list[zh_list.index(i.split(':', 1)[0])],
                            i.split(':', 1)[1].replace('\u3000', ''))

            experienced = self.selector.xpath("//div[@class='tip'][2]/text()")
            if experienced and experienced[0] == u'学习经历':
                user.education = self.selector.xpath(
                    "//div[@class='c'][4]/text()")[0][1:].replace(
                    u'\xa0', u' ')
                if self.selector.xpath(
                        "//div[@class='tip'][3]/text()")[0] == u'工作经历':
                    user.work = self.selector.xpath(
                        "//div[@class='c'][5]/text()")[0][1:].replace(
                        u'\xa0', u' ')
            elif experienced and experienced[0] == u'工作经历':
                user.work = self.selector.xpath(
                    "//div[@class='c'][4]/text()")[0][1:].replace(
                    u'\xa0', u' ')
            return user
        except Exception as e:
            logger.exception(e)
