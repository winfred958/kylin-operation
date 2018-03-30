# encoding: utf-8

"""

@author: kevin

@contact: kevin_678@126.com


@file: config.py.py

@time: 2018/3/21 17:36

@desc:

"""
from enum import Enum

HADOOP_HOME = ""

LOG_DIR = "log"

KYLIN_CONFIG = {
    "schema": "http",
    "host": "172.16.1.36",
    "port": 7070,
    "contextPath": "kylin",
    "username": "ADMIN",
    "passwd": "KYLIN"
}


class KYLIN_CUBE_BUILD_STATUS(Enum):
    RUNNING = 2
    FINISHED = 4


class KYLIN_CUBE_BUILD_TYPE(Enum):
    BUILD = "BUILD"
    MERGE = "MERGE"
    REFRESH = "REFRESH"


KYLIN_REST_POLLING_SECOND = 30

###############################################
# KYLIN REST
# http://kylin.apache.org/docs/howto/howto_use_restapi.html
###############################################


##############
# QUERY REST
##############
KYLIN_QUERY_REST_PATH = "query"

# tables: GET
# http://47.254.42.95:7070/kylin/api/tables?ext=true&project=kevin_test

# cube: GET
# http://47.254.42.95:7070/kylin/api/cubes?limit=15&offset=0&projectName=kevin_test


##############
# CUBE REST
##############
KYLIN_CREATE_CUBE_REST_PATH = ""

# List cubes
# GET
# http://47.254.42.95:7070/kylin/api/cubes?limit=15&offset=0&projectName=kevin_test
KYLIN_CUBE_LIST_PATH = "api/cubes"

# Build cube
# PUT: data: {"buildType":"BUILD","startTime":1519862400000,"endTime":1521072000000}
KYLIN_CUBE_BUILD_PATH = "api/cubes/{cubeName}/build"

##############
# JOB REST
##############
KYLIN_CUBE_JOB_INFO_PATH = "api/jobs/{jobId}"
# 查看所有cube的job进度
#    private List<Integer> status;
#    private String cubeName;
#    private String projectName;
#    private Integer offset;
#    private Integer limit;
#    private Integer timeFilter;
#    private String jobSearchMode; CUBING_ONLY, CHECKPOINT_ONLY, ALL
KYLIN_CUBE_JOBS_INFO_PATH = "api/jobs"

# Resume Job
# PUT /kylin/api/jobs/{jobId}/resume
