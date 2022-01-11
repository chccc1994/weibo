#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 作者       : shengbw
# 创建时间    : 2022/1/11 10:14
# 文件名     : __init__.py.py
# 软件       : PyCharm
# 邮箱       : ch_sheng5@163.com
from downloader.origin_picture_downloader import OriginPictureDownloader
from downloader.retweet_picture_downloader import RetweetPictureDownloader
from downloader.avatar_picture_downloader import AvatarPictureDownloader
from downloader.video_downloader import VideoDownloader

__all__ = [
    OriginPictureDownloader, RetweetPictureDownloader, AvatarPictureDownloader,
    VideoDownloader
]
