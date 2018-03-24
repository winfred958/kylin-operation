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
        # 设置 http header
        for key, value in self.headers.items():
            self.request.add_header(key, value)
        # 设置 http request method
        self.request.get_method = lambda: self.method
        # 设置 http data
        if self.data is not None:
            if self.method == EnmuHttpSchema.GET:
                self.request.add_data(urllib.urlencode(self.data))
            else:
                self.request.add_data(self.data)
        # 发送请求
        try:
            # self.log.info("request url = %s, data = %s", self.url, json.dumps(self.data).__str__())
            self.log.info("curl -X{method} {url} -d '{data}'".format(
                method=self.method,
                url=self.url,
                data=json.dumps(self.data).__str__()
            ))
            result = urllib2.urlopen(self.request)
        except urllib2.HTTPError as e:
            self.log.error("request url error: %s : %s", self.url, e.__str__())
        return result


if __name__ == '__main__':
    data = """
    {"sql":"SELECT GOODS_ID FROM  DIM_COMM.DIM_V_GOODS_INFO ", "offset":1000, "limit":"100", "acceptPartial":true, "project": "EDW_CUBE"}
    """

    hcu = HttpClientUtil(
        schema="http",
        host="47.88.50.90",
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

    response = json.loads(hcu.get_response().read())
    print(response)

    results = response.get("results")
    for i in results:
        print(i[0])
        break
    if response.get("partial"):
        print(response.get("partial"))

    print "+++++++++++++++++++++++++++++"
