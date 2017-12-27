#!/usr/bin/python
#coding=utf-8

#本章只讲述所有基本的的I/O函数，更多函数请参考Python标准文档。


def main():
    ########
    ##打印到屏幕
    ########
    print 'main'
    
    
    ########
    ##读取键盘输入
    ########
    '''
    raw_input
    input
    '''
    #raw_input函数
    #raw_input([prompt]) 函数从标准输入读取一个行，并返回一个字符串（去掉结尾的换行符）
    print '***raw_input demo***'
    str = raw_input("Please input: ")
    #for example, input 'hello world'
    print 'What you input is: ', str
    
    #input函数
    #input 可以接收一个Python表达式作为输入，并将运算结果返回。
    print '***input demo***'
    str = input("Please input: ")
    #for example, input [x*5 for x in range(2,10,2)]
    print 'What you input is: ', str
    
    
    ########
    ##打开和关闭文件
    ########
    
    #open函数
    #file object = open(file_name [, access_mode][, buffering])
    '''
    file_name：file_name变量是一个包含了你要访问的文件名称的字符串值。
    access_mode：access_mode决定了打开文件的模式：只读，写入，追加等。
            所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
    buffering:如果buffering的值被设为0，就不会有寄存。
            如果buffering的值取1，访问文件时会寄存行。
            如果将buffering的值设为大于1的整数，表明了这就是的寄存区的缓冲大小。
            如果取负值，寄存区的缓冲大小则为系统默认。
    '''
    #不同模式打开文件的完全列表：
    '''
    r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
    rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
    r+	打开一个文件用于读写。文件指针将会放在文件的开头。
    rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
    w	打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
    wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
    w+	打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
    wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
    a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
    ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
    a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
    ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
    '''
    
    
    ########
    ##File对象的属性
    ########
    #一个文件被打开后，你有一个file对象，你可以得到有关该文件的各种信息。
    '''
    file.closed	返回true如果文件已被关闭，否则返回false。
    file.mode	返回被打开文件的访问模式。
    file.name	返回文件的名称。
    file.softspace	如果用print输出后，必须跟一个空格符，则返回false。否则返回true。
    '''
    
    print '***file io demo***'
    fo = open('foo.txt', 'wb')
    print u"文件名：", fo.name
    print u"是否已关闭：", fo.closed
    print u"访问模式：", fo.mode
    print u"末尾是否强制加空格 ： ", fo.softspace
    
    #close()方法
    fo.close()
    print u"是否已关闭：", fo.closed
    
    #write()方法
    fo = open('foo.txt', 'wb')
    fo.write('www.runoob.com!\nVery good site!\n')
    fo.close()
    
    #read()方法
    fo = open('foo.txt', 'r')
    str = fo.read(10)
    print u"读取的字符串是：", str
    fo.close()
    
    
    ########
    ##文件定位
    ########
    '''
    tell()方法告诉你文件内的当前位置；换句话说，下一次的读写会发生在文件开头这么多字节之后。
    seek（offset [,from]）方法改变当前文件的位置。Offset变量表示要移动的字节数。
            From变量指定开始移动字节的参考位置。
            如果from被设为0，这意味着将文件的开头作为移动字节的参考位置。
            如果设为1，则使用当前的位置作为参考位置。
            如果它被设为2，那么该文件的末尾将作为参考位置。
            os.SEEK_SET, os.SEEK_CUR, os.SEEK_END
    '''
    # 打开一个文件
    fo = open("foo.txt", "r+")
    str = fo.read(10);
    print u"读取的字符串是 : ", str
 
    # 查找当前位置
    position = fo.tell();
    print u"当前文件位置 : ", position
 
    # 把指针再次重新定位到文件开头
    position = fo.seek(0, 0);
    str = fo.read(10);
    print u"重新读取字符串 : ", str
    # 关闭打开的文件
    fo.close()
    
    
    ########
    ##重命名和删除文件
    ########
    #os.rename os.remove
    import os
    fo = open('1.txt', 'w')
    fo.close()
    os.rename('1.txt','2.txt')
    os.remove('2.txt')
    
    
    ########
    ##Python里的目录
    ########
    #os.mkdir()方法 创建目录
    #os.chdir()方法 改变当前目录
    #os.rmdir()方法 删除目录
    
    
if __name__ == "__main__":
    main()

    
    
    
    
    
    
    
    