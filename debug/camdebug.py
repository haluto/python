#!/usr/bin/python
# -*- coding: UTF-8 -*-


##os.system
#该方法是直接调用标准C的system() 函数，仅仅在一个子终端运行系统命令，而不能获取命令执行后的返回信息。
#os.system("adb root")

##os.popen
#该方法不但执行命令还返回执行后的信息对象，是通过一个管道文件将结果返回。
#output = os.popen("adb devices")
#print output.read()

##commands.getstatusoutput
#import commands
#(status, output) = commands.getstatusoutput("cat /proc/cpuinfo")
#print status, output


import sys
import os
import xml.etree.ElementTree as ET
from optparse import OptionParser


HiliteE = '\033[1;31;47m'
HiliteX = '\033[0m'

########################################################################
# CommandItem class
########################################################################
class CommandItem:
    __name = ''
    __property = ''
    __valueon = 0
    __valueoff = 0
    __keyword = ''
    __description = ''

    def __init__(self, name, prop, valueon, valueoff, keyword, description):
        self.__name = name
        self.__property = prop
        self.__valueon = valueon
        self.__valueoff = valueoff
        self.__keyword = keyword
        self.__description = description

    def name(self):
        return self.__name
    def prop(self):
        return self.__property
    def valueon(self):
        return self.__valueon
    def valueoff(self):
        return self.__valueoff
    def keyword(self):
        return self.__keyword
    def description(self):
        return self.__description

########################################################################
# function name: readxml
# return: list of commandItem
########################################################################
def readxml(xml):
    tree = ET.parse(xml)
    root = tree.getroot()

    commandList = []
    for command in root.findall('command'):
        name = command.get('name')
        prop = command.find('property').text
        valueon = command.find('valueon').text
        valueoff = command.find('valueoff').text
        keyword = command.find('keyword').text
        description = command.find('description').text

        commandItem = CommandItem(name, prop, valueon, valueoff, keyword, description)
        commandList.append(commandItem)

    return commandList
'''
    for child in root:
        print child.tag, child.attrib

    for property in root.iter('property'):
        print property.text

    for command in root.findall('command'):
        property = command.find('property').text
        name = command.get('name')
        print name, property
'''


########################################################################
# function name: list_cmd
########################################################################
def list_cmd(commandList):
    for item in commandList:
        print item.name()
        print "        ", item.description().replace('"', '')
        print "        ", "Set %s to enable, set %s to disable." % (item.valueon(), item.valueoff())


########################################################################
# function name: has_device
# return: True if has device, False if no device.
########################################################################
def has_device():
    output = os.popen("adb devices")
    str = output.read()
    hasDevice = str.rstrip().endswith("device")

    if (not hasDevice):
        print "No device connected, please connect your device first."

    return hasDevice
    

########################################################################
# function name: is_cmd_in_commandList
# return: True if cmd is in commandList, False if not.
########################################################################
def is_cmd_in_commandList(cmd, commandList):
    for item in commandList:
        if item.name() == cmd:
            return True

    return False


########################################################################
# function name: run_command
########################################################################
def run_command(cmd, commandList, disable=False, specialValue=''):

    needRun = False

    if (has_device()):
        os.popen("adb root") 
        output = os.popen("adb root") # tricky, double call to make sure to get output of "adb root"
        outStr = output.read()
        if (outStr.find("already running as root") > 0):
            needRun = True

    if (needRun):
        for item in commandList:
            if item.name() == cmd:
                
                setValue = ''
                if disable:
                    setValue = item.valueoff()
                elif (specialValue == ''):
                    setValue = item.valueon()
                else:
                    setValue = specialValue

                #item.prop().replace('"','') is to remove " in string.
                cmdStr = "adb shell setprop " + item.prop().replace('"','') + " " + setValue

                print cmdStr
                os.popen(cmdStr)

                #check result
                cmdStr = "adb shell getprop " + item.prop().replace('"','')
                output = os.popen(cmdStr)
                outStr = output.read()
                if disable and outStr.rstrip() == setValue:
                    print "Set property succeeded."
                elif disable==False and outStr.rstrip() == setValue:
                    print "Set property succeeded."
                    #print "You can grep %s as keyword for %s to check the log now." % (item.keyword(), item.name())
                    print "keyword is",
                    print HiliteE,
                    print item.keyword(),
                    print HiliteX,
                    print "for %s." % item.name()
                else:
                    print "Set property failed."
                break


########################################################################
# function name: run_all_commands
########################################################################
def run_all_commands(xml, disable=False):
    commandList = readxml(xml)
    
    for item in commandList:
        cmd = item.name()
        run_command(cmd, commandList, disable)
    

########################################################################
# function name: main
########################################################################
def main():
    usage = '%prog [Options]'

    parser = OptionParser(usage)
    # action = "store_true", -l后面不需要带参数。[如果输入命令有-l，值是True，没有的话值是None][store_false同理]
    parser.add_option("-l", "--list", action = "store_true", 
                      dest = "listCmd", help = "list all supported commands")
    # action = "store" 表示-f后面必须带参数。[action选项：store, store_true, store_false]
    parser.add_option("-f", "--file", action = "store", default="info.xml",
                      dest = "xml", help = "set xml file for config")
    parser.add_option("-c", "--cmd", action = "store", default=None,
                      dest = "cmd", help = '''set your cmd list.
                                              use '-' behind the command string to disable the cmd
                                              use '=value' behind the command string to set special value''')
    parser.add_option("-a", "--all", action = "store_true", 
                      dest = "all", help = "run all commands supported in xml file.")
    parser.add_option("-d", "--disableall", action = "store_true", 
                      dest = "disableall", help = "disable all commands supported in xml file.")

    options, args = parser.parse_args()

    # Step 1, check whether the config file exists.
    if not os.path.isfile(options.xml):
        print "%s is not exist!" % options.xml
        return

    # Step 2, if -l/--list, it means user just want to view the supported command list, won't care other options.
    if options.listCmd is True:
        commandList = readxml(options.xml)
        list_cmd(commandList)
        return

    # Step 2.5, if -a and -d are configed together, means the user is stupid...
    if options.all is True and options.disableall is True:
        print "Hi man, are you crazy?"
        return

    # Step 3, if -a/--all, it means run all commands, so ignore -c/--cmd.
    if options.all is True:
        run_all_commands(options.xml)
        return

    # Step 4, if -D/--disable-all, it means disable all commands, so ignore -c/--cmd.
    if options.disableall is True:
        run_all_commands(options.xml, disable = True)
        return

    # Step 5, parse -c/--cmd string to run the commands.
    if (options.cmd is not None):
        cmdList = options.cmd.split(" ")
        for cmd in cmdList:
            if (cmd.isspace() or cmd == ""):
                continue
            else:
                # Suppose "showfps-" means disable showfps.
                disable = False
                real_cmd = cmd
                # Suppose "hal=4" means want to set hal as special value, here is 4, instead of valueon in xml.
                eqIndex = cmd.rfind('=')
                specialValue = ''

                if cmd[-1:] == "-":
                    real_cmd = cmd[:-1]
                    disable = True
                elif eqIndex > 0:
                    real_cmd = cmd[:eqIndex]
                    specialValue = cmd[eqIndex+1:]

                commandList = readxml(options.xml)

                if is_cmd_in_commandList(real_cmd, commandList):
                    print "OK, %s is supported" % real_cmd
                    run_command(real_cmd, commandList, disable, specialValue)
                else:
                    print "Sorry, %s is not supported." % real_cmd


if __name__ == '__main__':
    main()




