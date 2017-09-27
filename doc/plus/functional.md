# 函数式编程
## [目录](./summary.md)
## 解释含义

大概就是允许你将函数传来传去。

## 解释高阶函数

意思就是说，函数名可以像一般的变量一样可以传递，看例子：

```python
abs(-1) #求绝对值的全局函数
f = abs
f(-1)
>>> 1
```
这说明了，函数名可以像变量一样正常的传递。于此向对应的js

```javascript
const a = () => {
  console.log('hello world')
}
let b = a
b()
```
效果是一样的，这就是高阶函数的方式(只不过js中的this是有问题的，不过=>并没有this，所以也就没有这个烦恼了)

### 举个例子

```python

def add(x, y, f):
    return f(x) + f(y)

```

```javascript
 function age(f, z) {
   z(f)
 }
```

也就是传说中的回调函数。



`age(12,x => {something}`


把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式

## map && reduce

- map

```python
def file(x):
    return x * x

a = map(file,[1, 2, 3])

```

说明：

第一个参数是一个函数

第二个函数式一个interable

返回值是一个interator

在这里我们要介绍另一个函数list，它可以将一个惰性数据变成一个list

```python
list(a)
[1, 4, 9]

```

类似js中的array中的map等高级函数
`[].map((r) => {})`

#### 小技巧

如果从数字变成字符串？

```python
a = [1, 2, 3]
list(map(str,a))


>>> a = [1, 2, 3]
>>> list(map(str,a))
['1', '2', '3']

```

## 强调⚠️

`less is more ,或者是 enough is more`是一个很重要的理论。代码应该精炼，用最少的字做更多的活就是目的。
