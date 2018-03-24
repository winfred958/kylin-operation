# encoding: utf-8

"""

@author: kevin

@contact: kevin_678@126.com


@file: kylin_cube_rest.py

@time: 2018/3/23 8:34

@desc:

"""
import json

from config import config
from core import job_entity
from oprate.kylin_base_rest import KylinBaseRest
from utils.http_util import EnmuHttpSchema


class KylinCubeRest(KylinBaseRest):
    def __init__(self, cube_name, uuid=None):
        super(KylinCubeRest, self).__init__(method=None, path=None, da=None)
        self.cube_name = cube_name
        self.uuid = uuid

    def set_config(self, path, method, data=None):
        """

        :param path:
        :param method:
        :param data:
        """
        self.path = path
        self.method = method
        self.data = data

    def build_cube(self, start_time, end_time, build_type):
        """
        cube rebuild
        :param start_time:
        :param end_time:
        :param build_type:
        :return:
        """
        data = {
            "startTime": start_time,
            "endTime": end_time,
            "buildType": build_type
        }
        # 设置请求参数
        self.set_config(
            path=config.KYLIN_CUBE_BUILD_PATH.format(cubeName=self.cube_name),
            method=EnmuHttpSchema.PUT,
            data=json.dumps(data)
        )
        return self.parse_to_object(self.get_kylin_response())

    def parse_to_object(self, kylin_response):
        """
        kylin json 转化为对象
        :param kylin_response:
        :return:
        """
        return job_entity.passe_to_kylin_object(kylin_response)


if __name__ == '__main__':
    cube_rest = KylinCubeRest(cube_name="order_test_cube")
    res = cube_rest.build_cube(start_time=1519833600000, end_time=1521475200000,
                               build_type=config.KYLIN_CUBE_BUILD_TYPE.BUILD)

    print res
