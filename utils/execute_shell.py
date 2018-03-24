# coding:utf-8

"""
@author: kevin

@contact: kevin_678@126.com

@file: config.py

@time: 2017/6/15 18:11

@desc:

@Software: data-analysis

"""
import subprocess
import sys


class ExecuteShell(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''

    def executeShell(self, shell_cmd):
        returncode = -2
        try:
            process = subprocess.Popen(shell_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            (stdoutput, erroutput) = process.communicate()
            returncode = process.poll()
        except Exception as e:
            print "--- executeSell() --- : {}".format(e)
            raise e

        print "[ SHELL ] ------------------------- ERROR-START -------------------------"
        print erroutput
        print "[ SHELL ] ------------------------- ERROR-END -------------------------"
        print "[ SHELL ] ------------------------- INFOMATION-START -------------------------"
        print stdoutput
        print "[ SHELL ] ------------------------- INFOMATION-END -------------------------"

        return returncode

    def getStdOutList_out(self, shell_cmd):

        resut_list = []
        process = subprocess.Popen(shell_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

        (stdoutput, erroutput) = process.communicate()

        print "[ SHELL ] ------------------------- ERROR-START -------------------------"
        print erroutput
        print "[ SHELL ] ------------------------- ERROR-END -------------------------"
        print "[ SHELL ] ------------------------- INFOMATION-START -------------------------"
        print stdoutput
        print "[ SHELL ] ------------------------- INFOMATION-END -------------------------"

        sss = str(stdoutput)

        lis = sss.strip().split('\n')

        #         print type(lis)
        #
        for s in lis:
            resut_list.append(s)
        # print '({0})'.format(s)

        return resut_list

    def getStdOutList_err(self, shell_cmd):

        resut_list = []
        process = subprocess.Popen(shell_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

        (stdoutput, erroutput) = process.communicate()

        print "[ SHELL ] ------------------------- ERROR-START -------------------------"
        print erroutput
        print "[ SHELL ] ------------------------- ERROR-END -------------------------"
        print "[ SHELL ] ------------------------- INFOMATION-START -------------------------"
        print stdoutput
        print "[ SHELL ] ------------------------- INFOMATION-END -------------------------"

        sss = str(erroutput)

        lis = sss.strip().split('\n')

        #         print type(lis)
        #
        for s in lis:
            resut_list.append(s)
        # print '({0})'.format(s)

        return resut_list

    def getStdOutList_all(self, shell_cmd):

        resut_list_stdout = []
        process = subprocess.Popen(shell_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

        (stdoutput, erroutput) = process.communicate()

        strstdoutput = str(stdoutput)
        strerroutput = str(erroutput)

        list_sdtoutput = strstdoutput.strip().split('\n')
        list_erroutput = strerroutput.strip().split('\n')
        #         print type(lis)
        #
        for so in list_sdtoutput:
            resut_list_stdout.append(so)

        for eo in list_erroutput:
            resut_list_stdout.append(eo)

        return resut_list_stdout

    def getStdOutList_status_all(self, shell_cmd):

        statusMap = {}
        resut_list_stdout = []
        try:
            process = subprocess.Popen(shell_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            (stdoutput, erroutput) = process.communicate()
            returnCode = process.poll()
            print "[ SHELL ] ------------------------- ERROR-START -------------------------"
            print erroutput
            print "[ SHELL ] ------------------------- ERROR-END -------------------------"
            print "[ SHELL ] ------------------------- INFOMATION-START -------------------------"
            print stdoutput
            print "[ SHELL ] ------------------------- INFOMATION-END -------------------------"
        except Exception, e:
            print "--- executeSell() --- : {}".format(e)
            raise e

        strstdoutput = str(stdoutput)
        strerroutput = str(erroutput)

        list_sdtoutput = strstdoutput.strip().split('\n')
        list_erroutput = strerroutput.strip().split('\n')

        for so in list_sdtoutput:
            resut_list_stdout.append(so)

        for eo in list_erroutput:
            resut_list_stdout.append(eo)
        statusMap[returnCode] = resut_list_stdout
        return statusMap


if __name__ == '__main__':

    ex = ExecuteShell()

    cmd = 'ping www.baidu.com'
    #     lis=ex.getStdOutList_out(cmd)
    ma = ex.getStdOutList_status_all(cmd)
    print ma

    for k, v in ma.items():
        print "______"
        print k
        print "______"
        for l in v:
            print str(l).decode("gbk")

    print sys.getfilesystemencoding()
    print sys.getdefaultencoding()
