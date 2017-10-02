# 面向对象进阶
## [目录](./summary.md)
## 本单元是Python3中面向对象的一个进阶

上一章只是简单的介绍了一下类的继承，多态等特种本章介绍内容如下:

- 多重继承
- 元类
- 定制类

## 具体介绍

### 接下来演示，如何给类或者是实例对象添加新的属性和方法

实例对象

```py

class Person(object):
    pass
a = Person()
a.name = '12'
```
这样就在这个实例对象上增加了一个属性name，但是类并没有增加，所以其它 的实例对象也没有这个属性

如果是想在这个类上添加也是很容易的

```py
class Person(object):
    pass
Person.name = '12'
```
这样的话它的实例对象都可以取到这个属性了。

### __slots__

也就是说这个变量指向一个tuple，在这个tuple中是允许这个对象可以添加的新的属性，如果不在这个序列中，是无法绑定的，
并且它仅仅对于本类的实例对象有效，对于继承它的类来说并没有什么用。

```py

__author__ = 'ThomasHuke'

class Person(object):
    __slots__ = ('name', 'year')

p = Person()

p.name = 12
p.year = 12
p.bbt = 12


./slots.py
Traceback (most recent call last):
  File "./slots.py", line 13, in <module>
    p.bbt = 12
AttributeError: 'Person' object has no attribute 'bbt'

```

假如我们取消了p.bbt

```py
12 12
```
一切恢复正常。

这既是__slots__的功能，可以限制类的实例对象添加的属性。

### @property

Python内置的@property装饰器就是负责把一个方法变成属性调用

```py

class Person(object):
    @property
    def width(self):
        return self.width
    @width.setter
    def width(self, value):
        self.width = value

```

```py
p = Person()
p.name = 12
p.name
>>> 12

```
如果再使用p.name= xxx 就会报错。


其实也就是说让你在给类或者是实例对象添加属性的时候使用@property 添加的时候有所限制。

## 多重继承

### 概念

如tile，

```py

class Animal(object, World):
    pass
```

其实这就是多重继承。

使用都充继承就避免了继承树那种庞大的继承关系，需要什么功能继承就是了，简单明了。
