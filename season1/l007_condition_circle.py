#!/usr/bin/python
#coding=utf-8


def run_condition_code():
    num = 9
    if num >= 0 and num <= 10:
        print 'hello'
        
    num = 10
    if num < 0 or num > 10:
        print 'hello'
    else:
        print 'undefine'
    
    num = 21
    if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):    
        print 'hello'
    elif (num >= 20 and num <= 25):
        print 'world'
    else:
        print 'undefine'

def run_circle_while_code():
    count = 0
    while (count < 9):
        print 'the count is:', count
        count += 1
    
    i = 1
    while i < 10:   
        i += 1
        if i%2 > 0:     # 非双数时跳过输出
            continue
        print i         # 输出双数2、4、6、8、10
 
    i = 1
    while 1:            # 循环条件为1必定成立
        print i         # 输出1~10
        i += 1
        if i > 10:     # 当i大于10时跳出循环
            break
    
    
    #在 python 中，while … else 在循环条件为 false 时执行 else 语句块
    count = 0
    while count < 5:
        print count, " is  less than 5"
        count = count + 1
    else:
        print count, " is not less than 5"

def run_circle_for_code():
    for letter in 'Python':     # 第一个实例
        print u'当前字母 :', letter
 
    fruits = ['banana', 'apple',  'mango']
    for fruit in fruits:        # 第二个实例
        print u'当前水果 :', fruit
 
    print "Good bye!"
    
    
    #for ... else
    for num in range(10,20):  # 迭代 10 到 20 之间的数字
        for i in range(2,num): # 根据因子迭代
            if num%i == 0:      # 确定第一个因子
                j=num/i          # 计算第二个因子
                print u'%d 等于 %d * %d' % (num,i,j)
                break            # 跳出当前循环
        else:                  # 循环的 else 部分
            print num, u'是一个质数'

def run_sample_enumerate_code():
    sequence = [12, 34, 34, 23, 45, 76, 89]
    for i, j in enumerate(sequence):
        print i, j

def run_sample_list_append_code():
    # 输出 2 到 100 简的质数
    prime = []
    for num in range(2,100):  # 迭代 2 到 100 之间的数字
        for i in range(2,num): # 根据因子迭代
            if num%i == 0:      # 确定第一个因子
                break            # 跳出当前循环
        else:                  # 循环的 else 部分
            prime.append(num)
    print prime

def run_sample_triangle_code():
    rows = int(raw_input('Input Line Num: '))
    for i in range(0, rows):
        for k in range(0, 2 * rows - 1):
            if (i != rows - 1) and (k == rows - i - 1 or k == rows + i - 1):
                print " * ",
            elif i == rows - 1:
                if k % 2 == 0:
                    print " * ",
                else:
                    print "   ",
            else:
                print "   ",
        print "\n"

def run_bubble_sort_code():
    arays = [1,8,2,6,3,9,4]
    for i in range(len(arays)):
        for j in range(i+1):
            if arays[i] < arays[j]:
                # 实现两个变量的互换
                arays[i],arays[j] = arays[j],arays[i]
    print arays

    
def run_pass_code():
    for letter in 'Python':
        if letter == 'h':
            pass #这里如果没有pass，会报错。
        else:
            print 'current letter:', letter




def main():
    # Python条件语句
    # if, elif, else; and, or
    #run_condition_code()

    # Python循环语句
    # while, for; break, continue, pass
    #run_circle_while_code()

    # for循环
    #run_circle_for_code()
    
    # pass语句
    # Python pass是空语句，是为了保持程序结构的完整性。
    # pass 不做任何事情，一般用做占位语句。
    run_pass_code()
    
    
    # 案例：使用内置enumerate函数进行遍历
    #run_sample_enumerate_code()
    
    # 案例：使用list.append()对质数进行输出。
    #run_sample_list_append_code()
    
    # 案例：打印空心等边三角形
    #run_sample_triangle_code()
    
    # 案例：冒泡排序
    #run_bubble_sort_code()



if __name__ == "__main__":
    main()


