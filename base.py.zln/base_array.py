# -*- coding:utf-8 -*-

'''
python 内置的一种数据类型是 list
list 是有序集合,可以添加和删除其中元素
列表中的数据可以是数字、字符串和集合
并且同一个列表中数据可以不是同一种类型
列表中的数据可以重复
'''
list = ['t', '1', 'test', ['a', 'b']]
print(list)
# 显示列表的第一个数据
print(list[0])

# 显示列表的最后一个数据
print(list[-1])

# 甚至可以显示最后一个列表中的最后一个数据
print(list[-1][-1])

# 列表也可以和字符串一样进行截取, 截取完返回一个列表
test = list[0: -2]
print(test)

# 列表之间还可以和字符串一样进行拼接
print(list + test)

# 列表与字符串不能进行拼接, 会报错
# print(list[0] + test)

# list 中的元素可以改变
list[0] = 'a'
print(list)

# len 方法可以统计 list 的长度
print(len(list))

# 通过 append 给 list 添加元素
list.append('append')
print(list)

# 通过 pop 删除 list 中的元素
list.pop(1)
print(list)

'''
元组与 list 类似, 区别是元组中的数据不可以修改
'''
tuple = (1, 2, ('a', 'b'))
print(tuple)

# 空元组
tuple_none = ()

# 只有一个元素的元组写法有点特殊
tuple_one = ('one',)
print(tuple_one)

# 元组与 list 用法类似

# 显示元组第一个数据
print(tuple[0])

# 显示元组最后一个数据
print(tuple[-1])

# 元组切片
tuple_test = tuple[0: -1]
print(tuple_test)

# 元组拼接
print(tuple + tuple_test)

# 虽然说元组内容不可变, 但是可以在元组中加一个可变的元组, 让元组变的可变
tuple_change = (1, "t", [1, "test"])

print(tuple_change)

tuple_change[-1][1] = 2
print(tuple_change)