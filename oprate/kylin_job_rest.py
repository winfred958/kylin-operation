# encoding: utf-8

"""

@author: kevin

@contact: kevin_678@126.com


@file: kylin_job_rest.py

@time: 2018/3/23 10:01

@desc:

"""
from config import config
from core import job_entity
from oprate.kylin_base_rest import KylinBaseRest
from utils.http_util import EnmuHttpSchema


class KylinJobRest(KylinBaseRest):
    def __init__(self):
        super(KylinJobRest, self).__init__(method=None, path=None, da=None)

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

    def get_jobs_running(self, project_name):
        """

        :param project_name:
        :return:
        """
        data = {
            "jobSearchMode": "ALL",
            "limit": 15,
            "offset": 0,
            "projectName": project_name,
            "status": ["2"]
        }
        # 设置请求参数
        self.set_config(
            path=config.KYLIN_CUBE_JOBS_INFO_PATH,
            method=EnmuHttpSchema.GET,
            data=data
        )
        return self.parse_to_object(self.get_kylin_response())

    def get_jobs_running_and_success(self, project_name):
        """

        :param project_name:
        :return:
        """
        data = {
            "jobSearchMode": "ALL",
            "limit": 15,
            "offset": 0,
            "projectName": project_name,
            "status": ["2", "4"]
        }
        # 设置请求参数
        self.set_config(
            path=config.KYLIN_CUBE_JOBS_INFO_PATH,
            method=EnmuHttpSchema.GET,
            data=data
        )
        return self.parse_to_list(self.get_kylin_response())

    def get_job_info_by_cube(self, project_name, cube_name):
        """
        获取cube的build信息
        :param project_name: kylin project name
        :param cube_name: kylin cube name
        :return:
        """
        data = {
            "jobSearchMode": "ALL",
            "limit": 15,
            "offset": 0,
            "projectName": project_name,
            "cubeName": cube_name
        }
        # 设置请求参数
        self.set_config(
            path=config.KYLIN_CUBE_JOBS_INFO_PATH,
            method=EnmuHttpSchema.GET,
            data=data
        )
        return self.parse_to_list(self.get_kylin_response())

    def get_job_info_by_job_id(self, job_id):
        """
        获取cube的build信息
        :param job_id: kylin job id (uuid)
        :return:
        """
        data = None
        # 设置请求参数
        self.set_config(
            path=config.KYLIN_CUBE_JOB_INFO_PATH.format(jobId=job_id),
            method=EnmuHttpSchema.GET,
            data=data
        )
        return self.parse_to_object(self.get_kylin_response())

    def parse_to_object(self, kylin_response):
        """
        kylin json 转化为对象
        :param kylin_response:
        :return:
        """
        return job_entity.passe_to_kylin_object(kylin_response)

    def parse_to_list(self, kylin_response):
        """
        kylin json 转化为对象
        :param kylin_response:
        :return:
        """
        lis = list()
        for response in kylin_response:
            lis.append(job_entity.passe_to_kylin_object(response))
        return lis


if __name__ == '__main__':
    kjr = KylinJobRest()
    # job_response = kjr.get_job_info_by_cube("kevin_test", "order_test_cube")
    job_response = kjr.get_job_info_by_job_id("0f6c8fbb-2f0c-47be-beac-d685392722e0")
    print job_response
    print type(job_response)
    if isinstance(job_response, list):
        for job in job_response:
            print "cube: {cube} , uuid = {uuid} -> {progress}".format(cube=job.related_cube,
                                                                      uuid=job.uuid,
                                                                      progress=job.progress
                                                                      )
    else:
        print "cube: {cube} , uuid = {uuid} -> {progress}".format(cube=job_response.related_cube,
                                                                  uuid=job_response.uuid,
                                                                  progress=job_response.progress
                                                                  )
