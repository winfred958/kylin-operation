# encoding: utf-8

"""

@author: kevin

@contact: kevin_678@126.com


@file: kylin_service.py

@time: 2018/3/23 16:08

@desc:

"""
import datetime

import time

import json

from config import config
from core import job_entity
from oprate.kylin_cube_rest import KylinCubeRest
from oprate.kylin_job_rest import KylinJobRest

from utils.logging_util import LogUtil


class KylinCubeService(object):
    log = LogUtil()
    kylinJobRest = KylinJobRest()

    def cube_build(self, parameter):
        start_time = self.get_timestamp(parameter.start_time)
        end_time = self.get_timestamp(parameter.end_time)

        cube_name = parameter.cube_name
        kylinCubeRest = KylinCubeRest(cube_name=cube_name)
        # start build cube
        result = kylinCubeRest.build_cube(
            start_time=start_time,
            end_time=end_time,
            build_type=config.KYLIN_CUBE_BUILD_TYPE.BUILD
        )
        if result is None or result.uuid is None:
            self.log.error("CUBE BUILD FAILED: {} , kylin server error".format(cube_name))
            return -1

        # echo rebuild info
        self.echo_rebuild_info(result)

        job_id = result.uuid
        while True:
            cube_job_info = self.get_cube_job_info(job_id=job_id)
            if cube_job_info is None:
                self.log.error("GET CUBE JOB INFO FAILED: {} , kylin server error".format(cube_name))
            self.log.info("CUBE BUILDING: {} >>>>>>>>>> {}".format(cube_name, cube_job_info.progress))
            if cube_job_info.progress < 100:
                pass
            else:
                self.log.info("CUBE BUILD SUCCESS: {}".format(cube_name))
                # break
                return 0
            time.sleep(config.KYLIN_REST_POLLING_SECOND)

    def get_cube_job_info(self, job_id):
        return self.kylinJobRest.get_job_info_by_job_id(job_id)

    def get_timestamp(self, data_str):
        """

        :param data_str:
        :return:
        """

        da = datetime.datetime.strptime(data_str, "%Y-%m-%d")
        return int(time.mktime(da.timetuple())) * 1000

    def echo_rebuild_info(self, result):
        self.log.info("""
        rebuild info : %s
        """, result)


if __name__ == '__main__':
    da = datetime.datetime.strptime("2018-03-26", "%Y-%m-%d")
    print da
    print type(da)
    print int(time.mktime(da.timetuple())) * 1000
