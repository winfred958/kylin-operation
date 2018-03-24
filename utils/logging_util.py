# encoding: utf-8

"""

@author: kevin

@contact: kevin_678@126.com


@file: logging_util.py

@time: 2018/3/23 13:06

@desc:

"""
import logging

import sys

from config import config


class LogUtil(object):
    __log = None

    def __init__(self, name="kylin_operation", file_path="log/kylin_operation.log"):
        self.name = name
        self.file_path = file_path

    #     def __init__(self, name="kylin_operation", file_path="log/kylin_operation.log"):

    def __new__(cls, *args, **kwargs):
        if LogUtil.__log is None:
            LogUtil.__log = object.__new__(cls, *args, **kwargs)
            LogUtil.__log = logging.getLogger("kylin_operation")
            # 制定logger的输出格式.-12s是冒号对齐,从levelname变量五十位置数12个字节后开始输出message信息也就是：位置开始对齐
            # formater = logging.Formatter(
            #     "%(asctime)s %(levelname)-6s: [processId=%(process)d, threadName=%(threadName)s, threadId=%(thread)d ] [%(filename)s %(funcName)s %(lineno)d] :%(message)s")

            formater = logging.Formatter(
                "%(asctime)s %(levelname)-6s: [%(filename)s %(funcName)s %(lineno)d] :%(message)s")

            # 文件日志
            file_handler = logging.FileHandler("{}/kylin_operation.log".format(config.LOG_DIR))
            file_handler.setFormatter(formater)
            # 控制台日志
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.formatter = formater
            # 为logger添加日志处理器
            LogUtil.__log.addHandler(file_handler)
            LogUtil.__log.addHandler(console_handler)

            # 指定日志输出的最低等级，默认是Waring
            LogUtil.__log.setLevel(logging.DEBUG)
        return LogUtil.__log

    def info(self, msg, *args, **kwargs):
        self.__log.info(msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        self.__log.debug(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.__log.error(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.__log.warning(msg, *args, **kwargs)


if __name__ == '__main__':
    __log = LogUtil()
    __log.info("===============================")
