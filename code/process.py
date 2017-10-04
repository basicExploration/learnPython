#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

print(os.getpid())
g = os.fork()
if g == 0:
    print("大家好我是子进程 %s,我的父进程是%s" % (os.getpid(), os.getpid()))
else:
    print("我是父进程 %s, 子进程是 %s" % (g, os.getpid()))


#  15642
# 我是父进程 15643, 子进程是 15642
# 大家好我是子进程 15643,我的父进程是15643
