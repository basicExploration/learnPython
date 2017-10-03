# io
## [目录](./summary.md)

操作系统运行用户进行读写，并不是直接的读写，而是提供给你一个接口，你通过这个对象来实现读 和 写。

## open()
```py
a = open('url', 'r')
```
url 就是你要传入的地址。opinions就是参数。

## read()

当你已经open了文件后 就开始使用 read来读文件了，然后在read()后，就需要人为的关闭close()文件。

## with语句

```py
with open('url',o) as f:
    print(f.read())
```
这时候你无须使用f.close来关闭文件了，with语句已经自动帮你解决了这个问题。


使用read(size)是每次读取一定的数量的数据，尽量不要直接使用read()这样有可能一次读取过多，内存爆掉。

readlines()是每次读取一行的数据。

> line.strip()) 把末尾的'\n'删掉

## 'rb'

后面的opinions如果是rb的话，那么读取的时候就是读二进制文件。

open还可以传入第三个数据，就是`coding='' ` 这样的如果不是utf8的话也是有办法处理好编码的。

## open的第四个参数errors=

指定发生错误的默认条件。


## 写文件

写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：

```py
>>> f = open('/Users/michael/test.txt', 'w')
>>> f.write('Hello, world!')
>>> f.close()
```
你可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件。当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以，还是用with语句来得保险：

```py
with open('/Users/michael/test.txt', 'w') as f:
    f.write('Hello, world!')

```
要写入特定编码的文本文件，请给open()函数传入encoding参数，将字符串自动转换成指定编码。


所以读取的话，都是

1. 打开文件(区别是opinions 是 r还是w)
2. 都可以使用with语句来简略close这句话。
3. 读是read() 写是write()

使用with语句操作文件IO是个好习惯~!

## stringIO和byteIO

顾名思义，stringIO和byteIO就是在内存之中读取信息前者是读取str后者是读取二级制信息。

写入。


```python
from io import StringIO
f = StringIO()
f.write('hello')
print(f.getvalue())
```

读取

```py
f = StringIO('dddd')
f.read()
```

ByteIO方法类似于StringIO

```py
from io import ByteIO
b = ByteIO()
b.write('abb'.encode('utf-8'))
print(b.getvalue())
```
读取时一样的。

```
b = ByteIO('b'xe4xb8xadxe6x96x87')
b.read(size)

```

## os

其实无论是shell还是nodejs还是golang还是如今的Python它调用的os都是系统底层给它的接口，是你的操作系统的作用，语言是没有这个能耐的。毕竟你的操作系统才是你运行的根本。

- os.name()能显示出来是类unix还是win

- os.uname()能准确的显示出来是你的操作系统，不过用之前应该先用os.name因为这个apiwin不提供。

- os.environ 提供了环境变量。
