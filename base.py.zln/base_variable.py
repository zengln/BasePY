# -*- coding:utf-8 -*-

# python 基础变量

# 字符串
# '' 与 "" 只是 python 中字符串表达的不同的两种方式,除了在字符串中要对相同的字符进行转义以外,并没有任何的区别
print('I\'m "OK"')
print("I'm \"OK\"")

# 除了上述的方式外, python 中也可以使用 r''表示字符串不需要转移
print(r'\n')
print('\n')
print(r'I\'m Ok')

# 多行内容
print('''1.第一行
2.第二行
3.第三行''')

print(r'''1.第一行\n
2.第二行
''')

# 布尔值, 布尔值只有 True 和 False 两种, 可以直接使用 True 和 False 表示或者使用运算标识
print(True)
print(False)
print(1>3)
print(3>1)

# 布尔值可以用 and、or 和 not 运算
# and 运算与运算， 必须全部为 True, 结果才是 True
# or 运算或运算, 只需要有一个为 True, 结果就是 True
# not 运算非运算, 是单目运算符, 后面只能跟一个值,　结果与值相反
print(True and True)
print(False and True)
print(False and False)
print(False or True)
print(not False)
print(not 1 > 2)

# 空值
None
