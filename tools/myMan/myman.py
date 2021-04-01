#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os

HiliteRed = '\033[1;31m'
HiliteGreen = '\033[1;32m'
HiliteRedWhite = '\033[1;31;47m'
HiliteStop = '\033[0m'

HELP_lsof = '''
lsof -i -n -P | grep <port>
    * -i: list IP sockets.
    * -n: Do not resolve hostnames(no DNS). 如果去掉-n，127.0.0.1会显示成localhost.
    * -P: Do not resolve port names(list port number instead of its name).

lsof -U             List Unix Sockets
lsof -i:8080        查看8080端口占用
lsof abc.txt        显示开启文件abc.txt的进程
lsof -c abc         显示abc进程现在打开的文件
lsof -c -p 1234     列出进程号为1234的进程所打开的文件
lsof -g gid         显示归属gid的进程情况
lsof +d /usr/local  显示目录下被进程开启的文件
lsof +D /usr/local  同上，但是会搜索目录下的目录，时间较长
lsof -d 4           显示使用fd为4的进程
lsof -i -U          显示所有打开的端口和UNIX domain文件
'''

HELP_netstat = '''
netstat -tunlp | grep <port>
    * -t (tcp) 仅显示tcp相关选项
    * -u (udp) 仅显示udp相关选项
    * -n 拒绝显示别名，能显示数字的全部转化为数字
    * -l 仅列出在Listen（监听）的服务状态
    * -p 显示建立相关链接的程序名

netstat -ntlp               查看当前所有tcp端口
netstat -ntulp | grep 80    查看所有80端口使用情况
netstat -ntulp | grep 3306  查看所有3306端口使用情况
'''

def main():
  if(len(sys.argv) < 2):
    print("usage: myman <cmd>")
    return

  cmd = sys.argv[1]
  if(cmd == "lsof"):
    print(HELP_lsof)
  elif(cmd == "netstat"):
    print(HELP_netstat)
  else:
    print("Not supported yet, try 'man' please.")



if __name__ == '__main__':
  main()
