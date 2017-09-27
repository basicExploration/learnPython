#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def file():
    print('step1')
    yield 1
    print('step2')
    yield 2
    return '应该停止了'
    print('2')
    yield 123

m = 0
while m < 10:
    try:
        x = file()
        j = next(x)
        print('数据：', j)
    except StopIteration as e:
        print('数据是:', e.value)
    m = m + 1
