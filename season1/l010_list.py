#!/usr/bin/python
#coding=utf-8


    ########
    ##
    ########

def main():
    ########
    ##Python列表（List）
    ########
    list1 = ['physics', 'chemistry', 1997, 2000];
    list2 = [1, 2, 3, 4, 5 ];
    list3 = ["a", "b", "c", "d"];
    print list1
    print list2
    print list3


    ########
    ##访问列表中的值
    ########
    list1 = ['physics', 'chemistry', 1997, 2000];
    list2 = [1, 2, 3, 4, 5, 6, 7 ];
    print "list1[0]: ", list1[0]
    print "list2[1:5]: ", list2[1:5]


    ########
    ##更新列表
    ########
    list = ['physics', 'chemistry', 1997, 2000];
    print "Value available at index 2 : "
    print list[2];
    list[2] = 2001;
    print "New value available at index 2 : "
    print list[2];


    ########
    ##删除列表元素
    ########
    list1 = ['physics', 'chemistry', 1997, 2000];
    print list1;
    del list1[2];
    print "After deleting value at index 2 : "
    print list1;


    ########
    ##Python列表脚本操作符
    ########
    print len([1,2,3])
    print ([1,2,3]+[4,5,6])
    print ['Hi!']*4
    print (3 in [1,2,3])
    for x in [1,2,3]: print x


    ########
    ##Python列表截取
    ########
    L = ['Google', 'Runoob', 'Taobao']
    print L[2]
    print L[-2]
    print L[1:]


    ########
    ##Python列表函数&方法
    ########
    #函数
    '''
    cmp(list1, list2)
        比较两个列表的元素
    len(list)
        列表元素个数
    max(list)
        返回列表元素最大值
    min(list)
        返回列表元素最小值
    list(seq)
        将元组转换为列表
    '''
    #方法
    '''
    list.append(obj)
        在列表末尾添加新的对象
    list.count(obj)
        统计某个元素在列表中出现的次数
    list.extend(seq)
        在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
    list.index(obj)
        从列表中找出某个值第一个匹配项的索引位置
    list.insert(index, obj)
        将对象插入列表
    list.pop(obj=list[-1])
        移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
    list.remove(obj)
        移除列表中某个值的第一个匹配项
    list.reverse()
        反向列表中元素
    list.sort([func])
        对原列表进行排序
    '''

    #二维列表
    #list_2d = [[0 for col in range(cols)] for row in range(rows)]
    list_2d = [[0 for i in range(5)] for i in range(4)]
    list_2d[3][4] = 1
    print list_2d

if __name__ == "__main__":
    main()













