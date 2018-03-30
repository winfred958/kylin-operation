# encoding: utf-8

"""

@author: kevin

@contact: kevin_678@126.com


@file: http_utils.py

@time: 2018/3/21 17:49

@desc:

"""
import json
import urllib
import urllib2

import requests
from enum import Enum

from utils.logging_util import LogUtil


class EnmuHttpSchema(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"


class HttpClientUtil(object):
    log = LogUtil()

    def __init__(self, schema, host, port=80, context_path="", path="", data=None, headers={}, method="GET"):
        self.schema = schema
        self.host = host
        self.port = port
        self.context_path = context_path
        self.path = path
        self.data = data
        self.headers = headers
        self.unredirected_hdrs = {}
        self.method = method
        self.url = "{schema}://{host}:{port}/{context_path}/{path}".format(
            schema=self.schema,
            host=self.host,
            port=self.port,
            context_path=self.context_path,
            path=self.path
        )
        self.request = urllib2.Request(self.url)

    def get_response(self):
        """

        :return:
        """
        result = None
        # 发送请求

        self.log.info("=== http method ===: {}".format(self.method))
        self.log.info("=== http headers ===: {}".format(self.headers))
        self.log.info("=== http data ===: {}".format(self.data))

        try:
            self.echo_log()
            if self.method == EnmuHttpSchema.GET:
                result = requests.get(url=self.url, params=self.data, headers=self.headers)
            if self.method == EnmuHttpSchema.POST:
                result = requests.post(url=self.url, data=self.data, headers=self.headers)
            if self.method == EnmuHttpSchema.PUT:
                result = requests.put(url=self.url, data=self.data, headers=self.headers)
        except urllib2.HTTPError as e:
            self.log.error("request url error: %s : %s", self.url, e.__str__())
        if result is None:
            result = {}
        return result.json()

    def echo_log(self):
        self.log.info("curl -X{method} {url} -d '{data}'".format(
            method=self.method,
            url=self.url,
            data=json.dumps(self.data).__str__()
        ))


if __name__ == '__main__':
    data = """
    {
    "sql": "SELECT FACT_WEB_TRACK_APP_DOWNLOAD.ACTION_DATE, COUNT(*) AS \"二维码访问量\" FROM TRACK_DW_FACT.FACT_WEB_TRACK_APP_DOWNLOAD WHERE FACT_WEB_TRACK_APP_DOWNLOAD.ACTION_DATE > '2018-03-01' GROUP BY FACT_WEB_TRACK_APP_DOWNLOAD.ACTION_DATE ORDER BY ACTION_DATE",
    "offset": 0,
    "limit": 50000,
    "acceptPartial": true,
    "project": "ec_track_log_v1"
    }
    """.replace("\n", "")

    hcu = HttpClientUtil(
        schema="http",
        host="47.254.42.95",
        port=7070,
        context_path="kylin",
        path="api/query",
        data=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": "Basic QURNSU46S1lMSU4="
        },
        method="POST"
    )

    response = hcu.get_response()
    print(response)

    results = response.get("results")
    for i in results:
        print(i[0])
        break
    if response.get("partial"):
        print(response.get("partial"))

    print "+++++++++++++++++++++++++++++"

