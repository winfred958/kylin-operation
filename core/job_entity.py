# encoding: utf-8

"""

@author: kevin

@contact: kevin_678@126.com


@file: job_entity.py

@time: 2018/3/23 16:29

@desc: kylin  cube job 公用实体类

"""


def passe_to_kylin_object(response):
    if response is None:
        return response
    return JobEntity(
        code=response.get("code"),
        msg=response.get("msg"),
        uuid=response.get("uuid"),
        last_modified=response.get("last_modified"),
        version=response.get("version"),
        name=response.get("name"),
        type=response.get("type"),
        duration=response.get("duration"),
        related_cube=response.get("related_cube"),
        related_segment=response.get("related_segment"),
        exec_start_time=response.get("exec_start_time"),
        exec_end_time=response.get("exec_end_time"),
        exec_interrupt_time=response.get("exec_interrupt_time"),
        mr_waiting=response.get("mr_waiting"),
        steps=response.get("steps"),
        submitter=response.get("submitter"),
        job_status=response.get("job_status"),
        progress=response.get("progress")
    )


class JobEntity(object):
    code = 200
    uuid = None
    last_modified = 0L
    version = None
    name = None
    type = None
    duration = 0
    related_cube = None
    related_segment = None
    exec_start_time = 0L
    exec_end_time = 0L
    exec_interrupt_time = 0L
    mr_waiting = 0L
    steps = list
    submitter = None
    job_status = None
    progress = 0

    def __init__(self, code, msg, uuid, last_modified, version, name, type, duration, related_cube, related_segment,
                 exec_start_time, exec_end_time, exec_interrupt_time, mr_waiting, steps, submitter, job_status,
                 progress):
        self.code = code
        self.msg = msg
        self.uuid = uuid
        self.last_modified = last_modified
        self.version = version
        self.name = name
        self.type = type
        self.duration = duration
        self.related_cube = related_cube
        self.related_segment = related_segment
        self.exec_start_time = exec_start_time
        self.exec_end_time = exec_end_time
        self.exec_interrupt_time = exec_interrupt_time
        self.mr_waiting = mr_waiting
        self.steps = steps
        self.submitter = submitter
        self.job_status = job_status
        self.progress = progress
