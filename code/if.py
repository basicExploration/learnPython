#!/usr/bin/env python3
# -*- coding:utf-8 -*-

name = input()
name = int(name)
if name < 50:
    print('穷x')
elif name > 50 and name <= 60:
    print('小资')
elif name > 60 and name <= 100:
    print('大资')
else:
    print('土豪~~~~')
