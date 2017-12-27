#!/usr/bin/python
#coding=utf-8


def main():
    a = 100 #整型
    b = 1000.0 #浮点
    c = "John" #字符串
    print a;print b;print c

    #多个变量赋值
    a = b = c = 1
    print a;print b;print c

    a,b,c = 1,2,"John"
    print a;print b;print c


    #Python支持的五个标准数据类型：
    #--Numbers（数字）
    #--String（字符串）
    #--List（列表）
    #--Tuple（元组）
    #--Dictionary（字典）
    #
    #---小括号-元组，中括号-列表，大括号-字典


    #Numbers
    #--int（有符号整型）
    #--long（长整型）
    #--float（浮点型）
    #--complex（复数）
    a = 1
    b = 1L
    c = 1.0
    d = 1+2j
    print type(a);print type(b);print type(c);print type(d)


    #String
    #从左到右索引默认0开始的，最大范围是字符串长度少1
    #从右到左索引默认-1开始的，最大范围是字符串开头
    #
    #使用以冒号分隔的字符串，python返回一个新的对象，结果包含了以这对偏移标识的连续的内容，左边的开始是包含了下边界。
    #加号（+）是字符串连接运算符，星号（*）是重复操作。
    str = 'Hello World!'
    #
    print str           # 输出完整字符串
    print str[0]        # 输出字符串中的第一个字符
    print str[2:5]      # 输出字符串中第三个至第五个之间的字符串
    print str[2:]       # 输出从第三个字符开始的字符串
    print str * 2       # 输出字符串两次
    print str + "TEST"  # 输出连接的字符串


    #List
    #列表用 [ ] 标识，是 python 最通用的复合数据类型。
    #列表中值的切割也可以用到变量 [头下标:尾下标] ，就可以截取相应的列表，从左到右索引默认 0 开始，从右到左索引默认 -1 开始，下标可以为空表示取到头或尾。
    #加号 + 是列表连接运算符，星号 * 是重复操作。
    list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
    tinylist = [123, 'john']
    #
    print list               # 输出完整列表
    print list[0]            # 输出列表的第一个元素
    print list[1:3]          # 输出第二个至第三个元素
    print list[2:]           # 输出从第三个开始至列表末尾的所有元素
    print tinylist * 2       # 输出列表两次
    print list + tinylist    # 打印组合的列表


    #Tuple
    #元组用"()"标识。内部元素用逗号隔开。
    #元组不能二次赋值，相当于只读列表。####################
    tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
    tinytuple = (123, 'john')
    #
    print tuple               # 输出完整元组
    print tuple[0]            # 输出元组的第一个元素
    print tuple[1:3]          # 输出第二个至第三个的元素 
    print tuple[2:]           # 输出从第三个开始至列表末尾的所有元素
    print tinytuple * 2       # 输出元组两次
    print tuple + tinytuple   # 打印组合的元组


    #Dictionary
    #字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。
    #列表是有序的对象集合，字典是无序的对象集合。
    #两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
    #字典用"{ }"标识。字典由索引(key)和它对应的值value组成。
    dict = {}
    dict['one'] = "This is one"
    dict[2] = "This is two"
    #
    tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
    #
    print dict['one']          # 输出键为'one' 的值
    print dict[2]              # 输出键为 2 的值
    print tinydict             # 输出完整的字典
    print tinydict.keys()      # 输出所有键
    print tinydict.values()    # 输出所有值



    #python中的数据类型转换
'''
    int(x [,base])
        将x转换为一个整数
    long(x [,base] )
        将x转换为一个长整数
    float(x)
        将x转换到一个浮点数
    complex(real [,imag])
        创建一个复数
    str(x)
        将对象 x 转换为字符串
    repr(x)
        将对象 x 转换为表达式字符串
    eval(str)
        用来计算在字符串中的有效Python表达式,并返回一个对象
    tuple(s)
        将序列 s 转换为一个元组
    list(s)
        将序列 s 转换为一个列表
    set(s)
        转换为可变集合
    dict(d)
        创建一个字典。d 必须是一个序列 (key,value)元组。
    frozenset(s)
        转换为不可变集合
    chr(x)
        将一个整数转换为一个字符
    unichr(x)
        将一个整数转换为Unicode字符
    ord(x)
        将一个字符转换为它的整数值
    hex(x)
        将一个整数转换为一个十六进制字符串
    oct(x)
        将一个整数转换为一个八进制字符串
'''

if __name__ == "__main__":
    main()

