#!/usr/bin/python
#coding=utf-8

def main():
    #Python算术运算符
    # +
    # -
    # *
    # /
    # %
    # **
    # //
    print 5%3  #取模 - 返回除法的余数
    print 3**4 #幂 - 返回x的y次幂
    print 5//3 #取整除 - 返回商的整数部分


    #Python比较运算符
    '''
    ==
    != 
    <>  #familiar with !=
    >
    <
    >=
    <=
    '''


    #Python赋值运算符
    '''
    = 
    +=
    -=
    *=
    /=
    %=
    **=
    //=
    '''


    #Python位运算符
    '''
    & - 按位与
    | - 按位或
    ^ - 按位异或
    ~ - 按位取反
    << - 左移
    >> - 右移
    '''


    #Python逻辑运算符
    '''
    and 
    or 
    not
    '''

    #Python成员运算符
    '''
    in
    not in
    '''
    a = 10
    list = [1,2,3,4,5]
    if (a in list):
        print 'a is in list'
    else:
        print 'a is not in list'


    #Python身份运算符
    '''
    is
    is not
    '''
    a = [1,2,3]
    b = a
    if (b is a):
        print 'b is a'
    else:
        print 'b is not a'

    c = a[:]
    if (c is a):
        print 'c is a'
    else:
        print 'c is not a'
    if (c == a):
        print 'c == a'
    else:
        print 'c != a'


    #Python运算符优先级
    #略，记不住的用小括号

if __name__ == "__main__":
    main()
