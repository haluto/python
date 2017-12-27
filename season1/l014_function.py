#!/usr/bin/python
#coding=utf-8

    ########
    ##
    ########

def ChangeInt(a):
    a = 10
    print "in ChangeInt function: ", a
    
def changeme(mylist):
    mylist.append([1,2,3,4])
    print "in changeme function: ", mylist
    return
    
def printinfo(name, age):
    print "Name: ", name
    print "Age: ", age
    return
    
def printinfo2(name, age = 35):
    print "Name: ", name
    print "Age: ", age
    return
    
def printinfo3(arg1, *vartuple):
    print arg1
    for var in vartuple:
        print var
    return
    
def main():
    ########
    ##参数传递
    ########
    #在 python 中，类型属于对象，变量是没有类型的：
    a=[1,2,3]
    b="Runoob"
    #以上代码中，[1,2,3] 是 List 类型，"Runoob" 是 String 类型，
    #而变量 a 是没有类型，她仅仅是一个对象的引用（一个指针），可以是 List 类型对象，也可以指向 String 类型对象。

    ####
    #可更改(mutable)与不可更改(immutable)对象
    ####
    '''
在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
    不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。
    可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

python 函数的参数传递：
    不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
    可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响
python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
    '''

    
    #实例 传不可变对象
    b = 2
    ChangeInt(b)
    print "out ChangeInt function: ", b #结果是2
    
    #实例 传可变对象
    mylist = [10,20,30]
    changeme(mylist)
    print "out changeme function: ", mylist
    
    
    ########
    ##参数
    ########
    #调用函数时可使用的正式参数类型：
    '''
    必备参数
    关键字参数
    默认参数
    不定长参数
    '''
    
    #必备参数
    #必备参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。
    #changeme() #会报错：TypeError: changeme() takes exactly 1 argument (0 given)
    
    #关键字参数
    #关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
    #使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
    printinfo(age=50, name='miki')
    
    #缺省参数
    #调用函数时，缺省参数的值如果没有传入，则被认为是默认值。
    printinfo2(age=50, name='miki')
    printinfo2(name='wiki')
    
    #不定长参数
    #def functionname([formal_args,] *var_args_tuple ):
    printinfo3(10)
    printinfo3(70,60,50)
    
    
    ########
    ##匿名函数
    ########
    '''
    python 使用 lambda 来创建匿名函数。
    lambda只是一个表达式，函数体比def简单很多。
    lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
    lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
    虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
    '''
    #lambda [arg1 [,arg2,.....argn]]:expression
    #实例
    sum = lambda arg1, arg2: arg1+arg2
    print sum(10, 20)
    print sum(20, 20)
    
    
    ########
    ##return语句
    ########
    #return语句[表达式]退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None。
    
    
    ########
    ##变量作用域
    ########
    #全局变量和局部变量
    #global -- 将变量定义为全局变量。
    
if __name__ == "__main__":
    main()
