# Python中的面向对象
## [目录](./summary.md)
## 解释面向对象
所谓面向对象是跟面向过程有区别的，面向对象简称是oop，
简单来说面向过程就是各种函数，大函数变小函数，调用小函数等等，然而面向对象就是一切皆对象，各种对象互相调用。
## 举例说明定义方式。

```Py
class Student(object):
  """docstring for Student."""
  def __init__(self, arg):
    self.arg = arg
  def method1():
        pass


```
首先class特殊关键字表明了这是一个类。然后def的第一个通常就是这个__init__的方法，可以说是构造函数。

然后剩余的函数称之为方法。

也就是说在__init__中定义的是属性，然后其余函数就是方法。

```js
class Stuent {
  constructor(name, year) {

    this.name = name
    this.yar = year
  }
  method1() {
    console.log(`本次输出的名字是${this.name},并且输出的年龄是${this.year}`)
  }
}
```

这两种是脚本语言Python， 脚本语言js的两种面向对象的两种方式，可以看出来其实很类似，不过，这里使用的js是**es6+** 如果你考虑兼容问题可以考虑渣软的**typescript**。

#### 总结一下面向对象的两大要素

- 属性
- 方法
