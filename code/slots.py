#!/usr/bin/env Python3
# -*- coding: utf-8 -*-

__author__ = 'ThomasHuke'

class Person(object):
    __slots__ = ('name', 'year')

p = Person()

p.name = 12
p.year = 12
# p.bbt = 12

print(p.name, p.year)
