# encoding: utf-8

"""

@author: kevin

@contact: kevin_678@126.com


@file: kylin_query_rest.py

@time: 2018/3/23 14:52

@desc:

"""
from oprate.kylin_base_rest import KylinBaseRest


class KylinQueryRest(KylinBaseRest):
    def __init__(self):
        super(KylinQueryRest, self).__init__(method=None, path=None, da=None)

    def set_config(self, path, method, data):
        """

        :param path:
        :param method:
        :param data:
        :return:
        """
        self.path = path
        self.method = method
        self.data = data

    def query(self, sql):
        pass


class QueryEntity(object):
    test = ""
    sql = ""

    def __init__(self, sql, project, acceptPartial=True, offset=0, limit=100):
        self.acceptPartial = acceptPartial
        self.sql = sql
        self.offset = offset
        self.limit = limit
        self.project = project


if __name__ == '__main__':
    queryEntity = QueryEntity(
        sql="SELECT GOODS_ID FROM  DIM_COMM.DIM_V_GOODS_INFO ",
        project="kevin_test"
    )
    print queryEntity.sql
    print QueryEntity.__dict__.iteritems()

    for i in QueryEntity.__dict__.iteritems():
        print i
        print type(i)

    # print json.loads(queryEntity)
