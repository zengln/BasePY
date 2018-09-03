# -*- coding:utf-8 -*-

'''
python 中函数的定义与调用非常简单,
但是 python 中函数的参数却非常有趣
'''

# 一个正常的函数定义
def funA(a, b):
    return a + b

# 在这时候调用函数就需要传入 a,b 两个参数, 如果想在调用时只传入一个参数

# 默认参数
def funB(a, b=1):
    return a + b

# 这时候只需要传入一个参数 a 即可调用 funB 函数, 此时参数 b 取默认值 1,要给 b 赋其他值只需要正常调用函数即可

# 1、默认参数简化了函数的调用, 在函数有多个参数的时候可以只传入少量参数即可, 在我们需要完整赋值参数时, 又能像正常函数一样赋值

# 默认参数也有坑
def funC(L = []):
    L.append('T')
    print(L)

funC()
funC()

# 在第二次调用时, 结果不一样了。
# 在函数定义时, 默认参数已经确定了即是变量L, 最开始 L 指向的是一个空 list,
# 在第一次调用后, L 指向的 list 已经发生了变化, 而此时默认参数还是 L 不变, 因此在第二次调用时, 默认参数即为第一次调用的结果
# 因此在使用默认参数时, 应该使用不变对象作为参数例如 str、None 等

# 可变参数即函数传递的参数个数是可变的
def funD(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum

# 在调用时即可直接传入多个参数
print(funD(1, 2, 3, 4))

# 这种做法其实将参数设置为 tuple 相似。在直接将参数设置为 tuple 后同样可以实现
# 但是使用可变参数可以传入 0 个参数, 而设置 tuple 为变量则需要传入一个空 tuple
print(funD())

def funE(list):
    sum = 0
    for n in list:
        sum += n
    return sum

print(funE((1, 2, 3, 4)))
print(funE(()))

# 对于 D 函数, 如果我们想直接传一个 tuple 变量, 并且想让效果和传多个参数相同
test = (1, 2, 3, 4)
print(funD(*test))
# 只把 test 作为参数传过去则报错, 因为 test 被看作是一个变量而不是一个 tuple
# print(funD(test))

# 可变参数将传入的多个参数封装成一个 list, 而关键字参数将多个参数封装成一个 dict
def funF(**kw):
    print(kw)

funF(test = 1, hello = 'h')
# 和可变参数的应用类似, 如果想将一个  dict 变量作为参数传递
dict = {'test':1, 'hello': 'h'}
funF(**dict)

# 命名关键字参数
# 如果限制希望传递的关键字参数
def funG(*, test):
    print(test)

funG(test=1)
# 这时候再传入 hello 就开始报错
# funG(test=1, hello='h')
# 命名关键字参数用 * 与其他参数分隔

# 如果参数中包含一个可变参数, 则可不需要 *
def funH(*num, test):
    print(num, test)

funH(1, 2, 3,4, test=1)