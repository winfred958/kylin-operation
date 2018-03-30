# encoding: utf-8

"""

@author: kevin

@contact: kevin_678@126.com


@file: kylin_service.py

@time: 2018/3/23 16:08

@desc:

"""
from oprate.kylin_job_rest import KylinJobRest
from utils.logging_util import LogUtil


class KylinJobService(object):
    log = LogUtil()

    def __init__(self):
        pass

    def get_job_info(self, parameter):
        result = self.get_job_info_by_cube(project_name=parameter.project_name, cube_name=parameter.cube_name)
        return result

    def get_job_info_by_cube(self, project_name, cube_name):
        """
        获取job 信息
        :param project_name:
        :param cube_name:
        :return:
        """
        kylinjob = KylinJobRest()
        job_instance = kylinjob.get_job_info_by_cube(project_name=project_name, cube_name=cube_name)
        for re in job_instance:
            self.log.info(
                "{{uuid: {uuid}, cube_name: {cube_name},  progress: {progress}, last_modified: {last_modified} ({date})}}".format(
                    uuid=re.uuid,
                    cube_name=re.related_cube,
                    progress=re.progress,
                    last_modified=re.last_modified,
                    date=""
                )
            )
        return job_instance


if __name__ == '__main__':
    kjs = KylinJobService()
    lis = kjs.get_job_info_by_cube(project_name="kevin_test", cube_name="order_test_cube")
    for i in lis:
        print ("{}: {}".format(i.uuid, i.progress))
