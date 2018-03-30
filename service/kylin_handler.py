# encoding: utf-8

"""

@author: kevin

@contact: kevin_678@126.com


@file: kylin_handler.py

@time: 2018/3/23 17:15

@desc:

"""
# rebuild, jobs
from service.kylin_cube_service import KylinCubeService
from service.kylin_job_service import KylinJobService
from utils.logging_util import LogUtil

OPERATION_REBUILD = "rebuild"
OPERATION_JOBS = "jobs"
DEBUG = "debug"

kylinCubeService = KylinCubeService()
kylinJobService = KylinJobService()

log = LogUtil()


def operation_request(parameter):
    log.info("kylin operation start")
    if parameter.operation is None:
        log.info(" --operation {} :: 没有设置操作类型, 正常退出".format(parameter.operation))
        return -1
    if DEBUG == parameter.debug:
        return debug(parameter)
    else:
        return run(parameter)


def run(parameter):
    try:
        return debug(parameter)
    except Exception as e:
        log.error("operation error: %s", e)
        return -1


def debug(parameter):
    result = None
    if parameter.operation == OPERATION_REBUILD:
        log.debug(OPERATION_REBUILD)
        result = kylinCubeService.cube_build(parameter)
    elif parameter.operation == OPERATION_JOBS:
        log.debug(OPERATION_JOBS)
        result = kylinJobService.get_job_info(parameter)
    if result is not None:
        return 0
    return -1
