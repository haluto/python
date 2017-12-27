#!/usr/bin/python
#coding=utf-8
# -*- coding: UTF-8 -*-




def main():
    a=1; b=2; c=3 #Tip1
    print a
    print b, c #Tip2
    print 'a= ',
    print a,
    print ', b =',
    print b

    print 'a=',a,',b=',b,',c=',c

if __name__ == "__main__":
    main()



'''

中文注释：
    要输入中文，需要声明coding类型为utf-8，否则会运行报错

#!/usr/bin/python
    指定执行脚本的工具
    将脚本添加可执行权限：
    $ chmod +x test.py
    然后在命令行中可以直接运行脚本：
    $ ./test.py

Tip1
    在一行中执行多条语句，用分号隔开

Tip2
    print默认输出是换行的；如需要实现不换行，要在变量末尾加上逗号

'''
