#!/usr/bin/python
#coding=utf-8

import shlex
import subprocess
import time

########################################################################
# function name: str2ms
# description: transfer string to time in ms.
# return: time in ms.
########################################################################
def str2ms(str, format='%d-%m %H:%M:%S'):
    #01-06 08:28:57.273 -> str
    #01-06 08:28:57 -> s
    s = str[:-4]
    #str --> struct time tuple
    t = time.strptime(s, format)
    #struct time tuple --> float
    ms1 = (time.mktime(t)) * 1000
    ms2 = int(str[-3:])
    return (ms1 + ms2)

########################################################################
# LogStatus class
########################################################################
class LogStatus:
    openCameraStart = 0.0
    openCameraEnd = 0.0
    
    def __init__(self, openCameraStart, openCameraEnd):
        self.openCameraStart = openCameraStart
        self.openCameraEnd = openCameraEnd

########################################################################
# function name: parseLog
########################################################################
def parseLog(log, logStatus):
    #open camera start?
    if log.find('[KPI Perf]: E PROFILE_OPEN_CAMERA') > 0:
        logTimeStr = log[:18]
        logStatus.openCameraStart = str2ms(logTimeStr)
        #print "open camera start is %d" % logStatus.openCameraStart
        
    #open camera end?
    if log.find('[KPI Perf] : PROFILE_FIRST_PREVIEW_FRAME') > 0:
        logTimeStr = log[:18]
        logStatus.openCameraEnd = str2ms(logTimeStr)
        #print "open camera end is %d" % logStatus.openCameraEnd
        
    #TODO: other logs by tag.
    
    
    #Do some print.
    if logStatus.openCameraEnd != 0.0 and logStatus.openCameraStart != 0.0:
        print "Open camera used: %d ms" % (logStatus.openCameraEnd-logStatus.openCameraStart)
        logStatus.openCameraStart = 0.0
        logStatus.openCameraEnd = 0.0
    

########################################################################
# function name: main
########################################################################
def main():
    shell_cmd = 'adb logcat'
    cmd = shlex.split(shell_cmd)
    p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    
    logStatus = LogStatus(0.0, 0.0)
    
    while p.poll() is None:
        line = p.stdout.readline()
        line = line.strip()
        
        if line:
            parseLog(line, logStatus)
            
            
    if p.returncode == 0:
        print('Subprogram success')
    else:
        print('Subprogram failed')

if __name__ == "__main__":
    main()
