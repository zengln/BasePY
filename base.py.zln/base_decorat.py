# -*- coding:utf-8 -*-
import functools

'''
装饰器
'''

# 函数也是对象,函数对象可以赋值给变量,通过变量也能调用该函数
def now():
    print('2018-09-18')

f = now
f()

# 函数对象有一个__name__属性,可以拿到函数的名字
# print(now.__name__)
# print(f.__name__)

# 如果要修改 now 函数的功能,但又不希望修改 now 函数的定义,那么需要用上装饰器

def log(func):
    def wrapper(*arg, **kw):
        print("call %s:" %func.__name__)
        return func(*arg, **kw)
    return wrapper

# log 就是一个 decorator，接收一个函数作为参数,并返回一个函数
# 借助 python 的 @ 语法, 把 decorator 置于函数的定义处
@log
def n_now():
    print('2019-09-18')

n_now()

# 这种定于与直接调用 log 函数并运行其返回的函数结果一致
log(now)()

# 一个本身就需要参数的 decorator
def log1(text):
    def decorator(func):
        def wrapper(*arg, **kw):
            print("%s %s()" %(text, func.__name__))
            return func(*arg, **kw)
        return wrapper
    return decorator

@log1('test')
def nn_now():
    print('2018-09-18')

nn_now()
# nn_now 的属性已经变成了 wrapper
print(nn_now.__name__)

# python 内置的 functools.wraps 的作用就是将使用了装饰器的函数__name__的值属性不变

def log2(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print("call %s()" %func.__name__)
        return func(*args, **kw)
    return wrapper

@log2
def nnn_now():
    print('2018-9-18')

nnn_now()
print(nnn_now.__name__)