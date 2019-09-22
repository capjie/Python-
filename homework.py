# 编写一个程序，输出你的姓名和学号，例如： 张三 201633424。
# id,name =  17271223,'L'
# print(name,id)
# id,name =  17271223,'L'
# print(name,id)
# ​
# L 17271223



# 用程序计算下列表达式的计算结果：
# 10除3的商
# 10除3的余数
# 二进制11110000的值
# sin(30) #30度
# import math
# i0 = 10//3
# i1 = 10%3
# i2 = 0b11110000
# i3 = math.sin(math.pi/6)
# print('1.{}\n2.{}\n3.{}\n4.{}'.format(i0,i1,i2,i3))
# 1.3
# 2.1
# 3.11110000
# 4.0.49999999999999994



# 计算1~100的和及平均数。
# sum = 0
# for i in range(101):#range（100），只循环到99
#     sum +=i
# print(sum)
# ​
# 5050

# 随机获取10个100以内的整数，求其中的最大值以及其第一次出现的位置。
# import random
# #for i in range(10):
#     #print(random.randint(0,100),end=' ')以空格的形式结尾输出
# value = [random.randint(0,100) for x in range(10)]#将数据存储在列表中
# print(value)



# 编写程序，用户输入一个4位整数，输出其每一位上的数之和。例如：用户输入 1234，计算1+2+3+4，程序输出 10。
"""
input函数返回的是string格式,python中字符串中的数据不可变。
将字符串转化成int类型的列表在一个个提取出来。
"""
# num = input('输入一个4位整数:\n')
# single_digit = list(map(int,list(num)))[0]     #个
# tens         = list(map(int,list(num)))[1]     #十
# hundred      = list(map(int,list(num)))[2]     #百
# kilobit      = list(map(int,list(num)))[3]     #千
# sum1 = single_digit+tens+hundred+kilobit
# print("{}".format(sum1))
'''
map函数：会根据提供的函数对指定序列做映射。
第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
map(function, iterable, ...)
···function -- 函数
···iterable -- 一个或多个序列
'''
# num = '1234'
# num1=map(int,list(num)) #将字符串转化成列表，并且将列表中的数据通过int()函数将列表的数据转化成整型！
# print(type(num1))
# sum1 = sum(num1)#只会将int类型的数据相加，参数可以是：列表，集合，元组
# print(sum1)



# 编写功能函数num=function_name(input)
# 统计下面这句话The Zen of Python中，单词'is'出现的次数
# 提示，help(str.split)

zen = "The Zen of Python, by Tim Peters\
Beautiful is better than ugly.\
Explicit is better than implicit.\
Simple is better than complex.\
Complex is better than complicated.\
Flat is better than nested.\
Sparse is better than dense.\
Readability counts.\
Special cases aren't special enough to break the rules.\
Although practicality beats purity.\
Errors should never pass silently.\
Unless explicitly silenced.\
In the face of ambiguity, refuse the temptation to guess.\
There should be one-- and preferably only one --obvious way to do it.\
Although that way may not be obvious at first unless you're Dutch.\
Now is better than never.\
Although never is often better than *right* now.\
If the implementation is hard to explain, it's a bad idea.\
If the implementation is easy to explain, it may be a good idea.\
Namespaces are one honking great idea -- let's do more of those!"

def Statistics(str1):
    sub = 'is'
    return str1.count(sub)

if __name__ =='__main__':
    num=Statistics(zen)
    print('is出现的次数:',num)
