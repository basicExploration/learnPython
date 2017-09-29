#!/usr/bin/env python3
# -*- coding: utf-8 -*-

_author_ = 'ThomasHuke[thomashuke@icloud.com]'

def file(n):
    t = []
    while n < 99:
        t.append(n)
        n = n + 2
    print( t )

file(1)

#[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, #43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, #83, 85, 87, 89, 91, 93, 95, 97]
