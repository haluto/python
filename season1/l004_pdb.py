#!/usr/bin/python
#coding=utf-8

if __name__ == "__main__":
    a = 1
    import pdb
    pdb.set_trace()
    b = 2
    c = a + b
    print(c)
    
    for i in range(10):
        print i # use this code for demo gdb: b, condition, p, ...


'''

关于PDB：
1. 调试方式：
    1) 命令行启动目标程序，加上-m参数。
    python -m pdb myscript.py
    2) 在Python交互环境中启动调试
    >>> import pdb
    >>> import mymodule
    >>> pdb.run('mymodule.test()')
    3) 在程序中插入一段程序
    如上述代码中，
        import pdb
        pdb.set_trace()

2. 常用命令：
h(elp)，会打印当前版本pdb可用的命令；如要查询某个命令，可以输入h [command]，例如：“h l”查看list命令。
l(ist)，可以列出当前将要运行的代码块。
b(reak)，设置断点，
        例如“b 65”，就是在第65行打断点；
        输入函数名作为参数，断点打到函数入口；
        只输入b，显示设置的所有断点。
condition bpnumber [condition]，在设置过的breakpoint number上加条件，
        例如：
        (Pdb) condition 2 i==6
        在第2个断点加上条件"i==6"，只在满足条件是断下来。
cl(ear)，清除所有断点；带参数清除指定断点。
disable/enable，禁用/激活断点，参数为断点编号。
n(ext)，让程序运行下一行，若当前语句是函数调用，直接运行完函数，不会进入函数内。
s(tep)，类似于next，遇到函数会进入函数中。
c(ont(inue))，让程序正常运行，直到遇到断点。
j(ump)，让程序跳转到指定的行数，参数为行数。

a(rgs)，打印当前函数的参数
p，打印某个变量，参数为变量名。
!，感叹号后面跟着语句，可以直接改变某个变量。
q(uit)，退出调试。
其余命令可用h查询。

'''
