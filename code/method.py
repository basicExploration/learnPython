#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 测试类中的方法。

class Student(object):
    def __init__(self, name, yaar, className):
        self.name = name
        self.yaar = yaar
        self.className = className
    def run(self):
        print('我们的名字是%s,并且我们的年龄是%s,我们来自于%s班级' % (self.name, self.yaar, self.className))

number1 = Student('thomashuke', 21, 4)

number1.run()
