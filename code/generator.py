#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def file():
    print('step1')
    yield 1
    print('step2')
    yield 2

a = file()

print(next(file()))
