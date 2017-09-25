#!/usr/bin/env Python
# -*- coding:utf-8 -*-

# 尾递归

def filePluss(n,result = 1):
    if n == 1:
        return result
    return filePluss(n - 1,result * n )

print(filePluss(12))

# 479001600
