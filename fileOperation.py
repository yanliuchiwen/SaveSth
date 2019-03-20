import os
import time
import subprocess


def OpenLogFile():
    timestruct = time.localtime(time.time())
    time_str = time.strftime('%Y_%m_%d', timestruct)
    path = os.getcwd()
    paths = path + '\\log\\' + time_str + '.txt '
    if not os.path.exists(paths):
        return
    subprocess.call(paths, shell=True)


def SaveLogFile(content):
    timestruct = time.localtime(time.time())
    time_str = time.strftime('%Y_%m_%d', timestruct)
    path = os.getcwd()
    if not os.path.exists(path + '\\log'):
        os.makedirs(path + '\\log')
    paths = path + '\\log\\' + time_str + '.txt '
    data = open(paths, 'a+')
    data.read()
    data.write(content + '\n\n')
    data.close()