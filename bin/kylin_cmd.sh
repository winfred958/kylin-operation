#!/bin/bash

# 获取项目根目录
PROJECT_ROOT_PATH=$(cd "$(dirname "$0")";cd ..; pwd)
# 设置项目目录到 PYTHONPATH
ENV_FILE_PATH=${PROJECT_ROOT_PATH}/config/env.sh
source ${ENV_FILE_PATH} ${PROJECT_ROOT_PATH}

echo `date +"%Y-%m-%d %H:%M:%S"`

cd ${PROJECT_ROOT_PATH}
python ${PROJECT_ROOT_PATH}/kylin_cmd.py $*
THREAD_STATUS=$?
echo `date +"%Y-%m-%d %H:%M:%S"`

exit ${THREAD_STATUS}
