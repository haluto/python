#!/usr/bin/python
#coding=utf-8




def main():
    print 'main'
    '''
BaseException	所有异常的基类
SystemExit	解释器请求退出
KeyboardInterrupt	用户中断执行(通常是输入^C)
Exception	常规错误的基类
StopIteration	迭代器没有更多的值
GeneratorExit	生成器(generator)发生异常来通知退出
StandardError	所有的内建标准异常的基类
ArithmeticError	所有数值计算错误的基类
FloatingPointError	浮点计算错误
OverflowError	数值运算超出最大限制
ZeroDivisionError	除(或取模)零 (所有数据类型)
AssertionError	断言语句失败
AttributeError	对象没有这个属性
EOFError	没有内建输入,到达EOF 标记
EnvironmentError	操作系统错误的基类
IOError	输入/输出操作失败
OSError	操作系统错误
WindowsError	系统调用失败
ImportError	导入模块/对象失败
LookupError	无效数据查询的基类
IndexError	序列中没有此索引(index)
KeyError	映射中没有这个键
MemoryError	内存溢出错误(对于Python 解释器不是致命的)
NameError	未声明/初始化对象 (没有属性)
UnboundLocalError	访问未初始化的本地变量
ReferenceError	弱引用(Weak reference)试图访问已经垃圾回收了的对象
RuntimeError	一般的运行时错误
NotImplementedError	尚未实现的方法
SyntaxError	Python 语法错误
IndentationError	缩进错误
TabError	Tab 和空格混用
SystemError	一般的解释器系统错误
TypeError	对类型无效的操作
ValueError	传入无效的参数
UnicodeError	Unicode 相关的错误
UnicodeDecodeError	Unicode 解码时的错误
UnicodeEncodeError	Unicode 编码时错误
UnicodeTranslateError	Unicode 转换时错误
Warning	警告的基类
DeprecationWarning	关于被弃用的特征的警告
FutureWarning	关于构造将来语义会有改变的警告
OverflowWarning	旧的关于自动提升为长整型(long)的警告
PendingDeprecationWarning	关于特性将会被废弃的警告
RuntimeWarning	可疑的运行时行为(runtime behavior)的警告
SyntaxWarning	可疑的语法的警告
UserWarning	用户代码生成的警告
    '''
    
    try:
        fh = open('testfile', 'w')
        fh.write("test")
    except IOError:
        print 'Error, failed to write'
    else:
        print 'write succeeded'
        fh.close()
    #事先将testfile的写权限去掉，则会运行到except中。


    #使用except而不带任何异常类型
    #try:
    #except:
    #else:
    #捕获所有的异常，不推荐这种处理方式。
    
    
    #使用except而带多种异常类型
    #try:
    #except(Exception1[, Exception2[,...ExceptionN]]]):
    #else:
    
    #try-finally语句
    #try-finally 语句无论是否发生异常都将执行最后的代码。
    
    
    ########
    ##异常的参数
    ########
    #一个异常可以带上参数，可作为输出的异常信息参数。
    def temp_convert(var):
        try:
            return int(var)
        except ValueError, Argument:
            print "var doesn't inlcude numeric\n", Argument
    
    temp_convert('xyz')
    
    
    ########
    ##触发异常
    ########
    #可以使用raise语句自己触发异常
    #raise [Exception [, args [, traceback]]]
    #语句中Exception是异常的类型（例如，NameError）参数是一个异常参数值。该参数是可选的，如果不提供，异常的参数是"None"。
    #最后一个参数是可选的（在实践中很少使用），如果存在，是跟踪异常对象。
    
    #实例  
    #一个异常可以是一个字符串，类或对象。 Python的内核提供的异常，大多数都是实例化的类，这是一个类的实例的参数。
    #定义一个异常：
    def mye(level):
        if level < 1:
            raise Exception("Invalid level!", level)
    
    #注意：为了能够捕获异常，"except"语句必须有用相同的异常来抛出类对象或者字符串。
    try:
        mye(1)
    except "Invalid level!":
        print 'run into exception'
    else:
        print 'everything runs ok.'
    #mye(0),则输出如下
    '''    
  Traceback (most recent call last):
  File "l018_exception.py", line 122, in <module>
    main()
  File "l018_exception.py", line 115, in main
    mye(0)
  File "l018_exception.py", line 111, in mye
    raise Exception("Invalid level!", level)
  Exception: ('Invalid level!', 0)
    '''
    
    
    ########
    ##用户自定义异常
    ########
    '''
    通过创建一个新的异常类，程序可以命名它们自己的异常。异常应该是典型的继承自Exception类，通过直接或间接的方式。
以下为与RuntimeError相关的实例,实例中创建了一个类，基类为RuntimeError，用于在异常触发时输出更多的信息。
在try语句块中，用户自定义的异常后执行except块语句，变量 e 是用于创建Networkerror类的实例。
    '''
    class Networkerror(RuntimeError):
        def __init__(self, arg):
            self.args = arg
    
    try:
        raise Networkerror("Bad hostname")
    except Networkerror, e:
        print e.args
    
if __name__ == "__main__":
    main()
