# coding:utf-8
"""

@author: kevin

@contact: kevin_678@126.com

@file: config.py

@time: 2017/6/15 18:11

@desc:

@Software: data-analysis

"""

from execute_shell import ExecuteShell
import config


class HdfsUtil(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''

    def createDirectory(self, path):
        return_code = -2
        cmd = "{hadoopHome}/bin/hadoop fs -mkdir {path}".format(
            hadoopHome=config.HADOOP_HOME,
            path=path
        )
        if self.isDirectory(path):
            print "---directory is already exist---:{}".format(path)
            return_code = 0
        else:
            execute_shell = ExecuteShell()
            return_code = execute_shell.executeShell(cmd)
        if return_code != 0:
            return_code = self.createDirectory_p(path)
        return return_code

    def createDirectory_p(self, path):
        return_code = -2
        cmd = "{hadoopHome}/bin/hadoop fs -mkdir -p {path}".format(
            hadoopHome=config.HADOOP_HOME,
            path=path
        )
        if self.isDirectory(path):
            return_code = 0
        else:
            execute_shell = ExecuteShell()
            return_code = execute_shell.executeShell(cmd)
        return return_code

    def createFile(self, path):
        return_code = -2
        cmd = "{hadoopHome}/bin/hadoop fs -touchz {path}".format(
            hadoopHome=config.HADOOP_HOME,
            path=path
        )
        if self.isFile(path):
            return_code = 0
        else:
            execute_shell = ExecuteShell()
            return_code = execute_shell.executeShell(cmd)
        return return_code

    def deleteDirectory(self, path):
        return_code = -2
        cmd = "{hadoopHome}/bin/hadoop fs -rmr {path}".format(
            hadoopHome=config.HADOOP_HOME,
            path=path
        )
        if self.isDirectory(path):
            execute_shell = ExecuteShell()
            return_code = execute_shell.executeShell(cmd)
        else:
            return_code = 0
        return return_code

    def deleteFile(self, path):
        return_code = -2
        cmd = "{hadoopHome}/bin/hadoop fs -rm {path}".format(
            hadoopHome=config.HADOOP_HOME,
            path=path
        )
        if self.isDirectory(path):
            return_code = 0
        else:
            execute_shell = ExecuteShell()
            return_code = execute_shell.executeShell(cmd)
        return return_code

    def isDirectory(self, path):
        cmd = "{hadoopHome}/bin/hadoop fs -test -d {path}".format(
            hadoopHome=config.HADOOP_HOME,
            path=path
        )
        execute_shell = ExecuteShell()
        return_code = execute_shell.executeShell(cmd)
        if return_code == 0:
            return True
        return False

    def isExist(self, path):
        cmd = "{hadoopHome}/bin/hadoop fs -test -e {path}".format(
            hadoopHome=config.HADOOP_HOME,
            path=path
        )
        execute_shell = ExecuteShell()
        return_code = execute_shell.executeShell(cmd)
        if return_code == 0:
            return True
        return False
