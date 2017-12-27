#!/usr/bin/python
#coding=utf-8

#模块
import mymodule
from mymodule2 import *

import math

#命名空间和作用域
Money = 2000
def ChangeMoney():
    global Money
    Money = 1

def main():
    print __doc__
    print __file__
    #模块
    mymodule.print_func('world')
    print_func2('john')
    
    #命名空间和作用域
    print Money
    ChangeMoney()
    print Money
    
    ########
    ##dir()函数
    ########
    content = dir(math)
    print content
    content = dir(mymodule)
    print content
    
    
    ########
    ##globals() 和 locals() 函数
    ########
    '''
    根据调用地方的不同，globals() 和 locals() 函数可被用来返回全局和局部命名空间里的名字。
    如果在函数内部调用 locals()，返回的是所有能在该函数里访问的命名。
    如果在函数内部调用 globals()，返回的是所有在该函数里能访问的全局名字。
    两个函数的返回类型都是字典。所以名字们能用 keys() 函数摘取。
    '''
    
    
    ########
    ##reload() 函数
    ########
    '''
    当一个模块被导入到一个脚本，模块顶层部分的代码只会被执行一次。
    因此，如果你想重新执行模块里顶层部分的代码，可以用 reload() 函数。
    该函数会重新导入之前导入过的模块。语法如下：
    reload(module_name)
    '''
    
    
    ########
    ##Python中的包
    ########
    '''
    包是一个分层次的文件目录结构，它定义了一个由模块及子包，和子包下的子包等组成的 Python 的应用环境。
    简单来说，包就是文件夹，但该文件夹下必须存在 __init__.py 文件, 该文件的内容可以为空。__int__.py用于标识当前文件夹是一个包。
    '''
    #实例 考虑一个在 package_runoob 目录下的 runoob1.py、runoob2.py、__init__.py 文件
    from package_runoob.runoob1 import runoob1
    from package_runoob.runoob2 import runoob2
    runoob1()
    runoob2()

if __name__ == "__main__":
    main()
