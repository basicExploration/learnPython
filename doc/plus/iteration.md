# 迭代
## [目录](./summary.md)
## 什么是迭代？

例子：

```python
for a in b.value():
    pass

for x, y in de.items():
    pass


```

## 字符串也可以😀

```python

for a in 'abcv':
    pass
```

## 如何判断是否可以迭代

请看代码

```python
from collections import Iterable

isinstance('abc', Iterable)
True
```

### 这里就引出了模块这个东西，稍后会继续写，这里先简单的说一下

使用方法请看
```python
from source import something

```

注意

- source 不能加后缀名

## 双变量

```python
for x, y in list:
    pass
```
这种行为在Python中很常见，就如同Python可以返回多个return 参数一样(返回的其实是一个省略的tuple)，Python的双变量也是很常见，并且很好用的行为。

#### 类比golang

```golang

for i := 0; i < count; i++ {

}

但是同时还可以，

for _, r := range s {
fmt.Printf("%c,", r)
    }
}
这也是一种多变量遍历的实例

```
