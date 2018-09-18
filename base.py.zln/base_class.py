# -*- coding:utf-8 -*-
from types import  MethodType


# 定义一个普通的class
class Student(object):
    pass

'''
给实例绑定一个属性
'''
s = Student()
s.name = 'zln'
print(s.name)

'''
给实例绑定一个方法
'''

# 定义一个函数作为实例方法
def set_age(self, age):
    self.age = age

# 给实例绑定一个方法
s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

'''
给class绑定方法
'''
def set_score(self, score):
    self.score = score

Student.set_score = set_score

s.set_score(100)
print(s.score)


# ========================================================

'''
限制实例属性
只允许对 Student1 的实例添加 name 和 age 属性
'''
class Student1(object):
    __slots__ = ('name', 'age')

s = Student1()
s.name = 'zln'
s.age = 25
# s.score = 90

'''
限制的属性仅对当前类实例起作用,对继承的自雷不起作用
'''
class GrandStudent(Student1):
    pass

gs = GrandStudent()
gs.score = 99


