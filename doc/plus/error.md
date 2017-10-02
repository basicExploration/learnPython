# 错误处理
## [目录](./summary.md)
我们要知道这几种错误
- bug
- 用户带来的错误
- 无法预知的系统带来的错误

第一种不用说一定要解决，第二种，想办法检测出来指引用户改正，第三种比如说网络断了，这种错误我们还是要有一定的处理方式的。

## try except finally体制

当然你也能在js中看到这套错误处理机制。这在高级语言中是很常见的错误处理机制。不过js中是catch

```py
try:
    print(....)
except ZeroDivisionError as e:
    print(e)
finally:
    print(...)
print('fdfdfd')

```
这个就是大致的过程。

## logging 模块

内置的logging模块，相当强大，不错不错。
