# 生成器
## [目录](./summary)
## generator 也就是生成器的英文拼写，它的主要作用是生成大批量的数据

- 方法一 (x for x in ['a', 'v'])

其实也就是把上一章迭代方法中的[]换成了()，那么返回的对象就不同了，前者是生成了一个list后者是生成了一个生成器。

其实跟js中的generator是一样的，打印出来这个生成器的内容只需要使用`next()`方法就OK了

```python
l = ( x for x in ['1','a','b'])
next(l)
>>> 1
next(l)
>>> a
next(l)
>>> b

```

直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。

```python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

## generator 函数

如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：

> js中需要将函数名前面添加 * 例如 \*function age(){}

```python
def file():
    while n < 100:
        yield

```


## 定义一个generator，依次返回数字1，3，5：

```python

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
    ```


调用该generator时，首先要生成一个generator对象，然后用next()函数不断获得下一个返回值：

```python

>>> o = odd()
>>> next(o)
step 1
1
>>> next(o)
step 2
3
>>> next(o)
step 3
5
>>> next(o)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration

```

也就是说它每次使用next方法当做容器并且运行到yield就停止，再次调用next接着上次的继续运行。跟js中是一样的。

定义的函数，其次每次返回的都是generator对象。


我们基本上从来不会用next()来获取下一个返回值，而是直接使用for循环来迭代

```python

def file():
    print('step1')
    yield 1
    print('step2')
    yield 2
    return '应该停止了'
    print('2')
    yield 123


for a in file():
    pass

```

证明了几点

- return后面肯定要停止。
- yield要停止一次
- for循环可以直接遍历generator无需再使用next
- 使用for循环无法取得return和yield返回的值

对于最后一个问题，我们可以使用这个办法解决。

```python

while true:
    try:
        x = file()
        print('数据是：',x)
    except StopIteration as e:
        print('数据是:',e.value)
        break

```
