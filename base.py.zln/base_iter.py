# -*- coding:utf-8 -*-
import sys
'''
迭代器是一个记住遍历位置的对象
字符串、列表或元组对象都可以用于创建迭代器
'''
# list = [1, 2, 3, 4]
# 创建迭代器
# it = iter(list)
# print(next(it))
# print(next(it))

# 用 for 遍历迭代器对象
# for x in it:
#     print(x, end=" ")

# 用 next 函数遍历迭代器对象
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         print("遍历结束")
#         sys.exit()


class MyNumber:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

# myclass = MyNumber()
# myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# for x in myiter:
#     print(x)

'''
调用一个生成器函数,返回的是一个迭代器对象

生成器的意义:通过列表生成式可以直接创建一个列表,但是这种创建方法收到了内存的限制,通过这种方式只能创建出元素个数有限的列表
而生成器可以按照某种算法推算出下一个元素的值,不必在一开始就创建出一个完整的 list, 从而节省了大量的空间。

python 中这种一边循环,一边计算的机制称为生成器
'''
# def fibonacci(n):
#     a, b, counter = 0, 1, 0
#     while True:
#         if(counter > n):
#             return
#         yield a
#         a, b = b, a + b
#         counter += 1
#
# f = fibonacci(10)
#
# while True:
#     try:
#         print(next(f), end= " ")
#     except StopIteration:
#         sys.exit()

# 一个简单的生成器
g = (x * x for x in range(10))
print(next(g))