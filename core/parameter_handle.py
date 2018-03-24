# encoding: utf-8

"""

@author: kevin

@contact: kevin_678@126.com

@file: ParameterHandle.py

@time: 2017/7/5 10:02

@desc:

@Software: data-etl

"""
import argparse


class Parameter(object):
    def __init__(self, start_time, end_time, username, passwd, project_name, cube_name, operation, job_status, debug):
        self.start_time = start_time
        self.end_time = end_time
        self.username = username
        self.passwd = passwd
        self.project_name = project_name
        self.cube_name = cube_name
        self.operation = operation
        self.job_status = job_status.split(",")
        self.debug = debug

    def __str__(self):
        return """
        start_time = {start_time}
        end_time = {end_time}
        username = {username}
        passwd = {passwd}
        project_name = {project_name}
        cube_name = {cube_name}
        operation = {operation}
        job_status = {job_status}

        """.format(
            start_time=self.start_time,
            end_time=self.end_time,
            username=self.username,
            passwd=self.passwd,
            project_name=self.project_name,
            cube_name=self.cube_name,
            operation=self.operation,
            job_status=self.job_status
        )


def get_parse_args():
    # 获取参数
    parser = argparse.ArgumentParser(description="kylin 交互")
    parser.add_argument("-st", "--start-time", help="start time (yyyy-MM-dd)", action="store",
                        type=str, default=None)
    parser.add_argument("-et", "--end-time", help="end time (yyyy-MM-dd)", action="store", type=str)
    parser.add_argument("-u", "--username", help="kylin user name", action="store", type=str,
                        default="ADMIN")
    parser.add_argument("-pw", "--passwd", help="kylin user passwd", action="store", type=str,
                        default="KYLIN")
    parser.add_argument("-p", "--project-name", help="kylin project name", action="store", type=str,
                        default=None)
    parser.add_argument("-c", "--cube-name", help="kylin cube name", action="store", type=str,
                        default=None)
    parser.add_argument("-o", "--operation", help="operation: rebuild, jobs", action="store", type=str,
                        default=None)
    parser.add_argument("-js", "--job-status", help="job status list [0-6], eg: 2,4", action="store", type=str,
                        default="2,4")
    parser.add_argument("-d", "--debug", help="debug", action="store", type=str,
                        default="debug")

    args = parser.parse_args()
    # 组装参数
    parameter_obj = Parameter(
        start_time=args.start_time,
        end_time=args.end_time,
        username=args.username,
        passwd=args.passwd,
        project_name=args.project_name,
        cube_name=args.cube_name,
        operation=args.operation,
        job_status=args.job_status,
        debug=args.debug
    )
    return parameter_obj


if __name__ == '__main__':
    parameter = get_parse_args()
    print parameter.__str__()
