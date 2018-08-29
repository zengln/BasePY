# -*- coding:utf-8 -*-
'''
    python 中字典类型
    python 中的字典中的数据是以键值对的形式存储， 类似于 map 的概念
    这个键可以看成是 list 中的索引, 字典通过这个键能得到对应的值
    这么一说, 又和 list 相似了, 但还有些不同
'''

# 定义一个字典
dict = {'number': 1, 'array': ['1', '2'], 'str': 'test'}
print(dict)
# 通过键取值
print(dict['array'])

# dict 通过键取值, list 通过索引取值, 两者有什么不同？
# list 取值的时候是顺序查找, 从第一个数据开始, 直到找到所需要的值为止, 因此当 list 存储的数据越多时, 查找速度越慢
# dict 通过键来取值, dict 通过键计算出值的地址, 然后直接通过地址在内存中取出值, 因此查找速度不受存储数据量的影响

# dict 中由于通过键取值, 因此键是唯一的, 给存在的键赋值, 则会把之前的值给覆盖掉
print(dict['number'])
dict['number'] = 2
print(dict['number'])

# 给一个不存在的键取值则报错
# print(dict['test'])

# 可以预先判断键是否存在
print('number' in dict)
print('test' in dict)

# 或者取值时给没取到值的键附上一个默认值
print(dict.get('test', 't'))

# dict 中规定键是不可变的, 因此字符串和数字可以作为key, 而 list 由于可变则不行

# set 是一个无序不重复元素的序列
# set 中重复的元素会被过滤
set = {1, 2, 4, 4, 3}
print(set)

# set 最重要的用于是用于集合运算
a = {1, 3, 6, 7, 0}
b = {2, 4, 7, 9, 6}

# a与b的差集
print(a - b)

# a与b的并集
print(a | b)

# a与b的交集
print(a & b)

# a与b中不同时存在的元素
print(a ^ b)