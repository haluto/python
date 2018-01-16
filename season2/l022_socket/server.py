#!/usr/bin/python
#coding=utf-8

import socket               # 导入 socket 模块


def main():
    s = socket.socket()         # 创建 socket 对象
    host = socket.gethostname() # 获取本地主机名
    port = 12345                # 设置端口
    s.bind((host, port))        # 绑定端口

    s.listen(5)                 # 等待客户端连接
    while True:
        c, addr = s.accept()     # 建立客户端连接。
        print '连接地址：', addr
        c.send('欢迎访问菜鸟教程！')
        c.close()                # 关闭连接

if __name__ == "__main__":
    main()