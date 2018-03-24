# encoding: utf-8

"""

@author: kevin

@contact: kevin_678@126.com


@file: kylin_cmd.py

@time: 2018/3/23 15:28

@desc:

"""
from core import parameter_handle
from service import kylin_handler
from utils.logging_util import LogUtil

if __name__ == '__main__':
    log = LogUtil()
    parameter = parameter_handle.get_parse_args()
    log.info("--operation {}".format(parameter.operation))
    if parameter.operation is None:
        log.info("--operation {}, is None exit -1".format(parameter.operation))
        exit(-1)
    else:
        return_code = kylin_handler.operation_request(parameter)
        log.info("exit {}".format(return_code))
        exit(return_code)
