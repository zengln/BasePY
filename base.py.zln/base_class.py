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

'''
python 内置的 @property 装饰器把一个方法编程属性调用 
'''
class Student2(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("score must be an interge")
        if value < 0 or value > 100:
            raise ValueError("score must between 0 ~ 100")
        self._score = value


s = Student2()
s.score = 60
print(s.score)
# s.score = 900


class Student3(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2018 - self._birth


s = Student3()
s.birth = 2000
print(s.age)
