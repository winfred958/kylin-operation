# encoding: utf-8

"""

@author: kevin

@contact: kevin_678@126.com


@file: kylin_base_rest.py

@time: 2018/3/22 14:00

@desc:

"""
import abc
import base64
import json
import six

from config import config
from utils.http_util import HttpClientUtil
from utils.logging_util import LogUtil


@six.add_metaclass(abc.ABCMeta)
class KylinBaseRest(object):
    log = LogUtil()

    def __init__(self, method, path, da):
        self.method = method
        self.path = path
        self.data = da
        self.schema = config.KYLIN_CONFIG.get("schema")
        self.host = config.KYLIN_CONFIG.get("host")
        self.port = config.KYLIN_CONFIG.get("port")
        self.context_path = config.KYLIN_CONFIG.get("contextPath")
        self.username = config.KYLIN_CONFIG.get("username")
        self.passwd = config.KYLIN_CONFIG.get("passwd")

    @abc.abstractmethod
    def set_config(self, path, method, data):
        """
        配置请求链接和参数
        :param path:
        :param method:
        :param data:
        :return:
        """

    def set_header(self, header):
        """
        设置请求头
        :param header:
        :return:
        """

    def get_kylin_response(self):
        """
        向kyin发起rest请求
        :return:
        """
        hcu = HttpClientUtil(
            schema=self.schema,
            host=self.host,
            port=self.port,
            context_path=self.context_path,
            path=self.path,
            data=self.data,
            headers={
                "Content-Type": "application/json",
                "Authorization": self.get_base_auth()
            },
            method=self.method
        )
        response = hcu.get_response()
        response_str = json.dumps(dict())
        response_dict = dict()
        if response is not None:
            response_str = response.read()
            response_dict = json.loads(response_str)
        self.log.info("http response: %s", response_str)
        return response_dict

    def get_base_auth(self):
        """

        :return:
        """
        str = "{username}:{passwd}".format(
            username=self.username,
            passwd=self.passwd
        )
        return "Basic {auth}".format(auth=base64.encodestring(str)).replace("\n", "")
