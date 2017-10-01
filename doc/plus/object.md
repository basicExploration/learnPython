# Python中的面向对象
## [目录](./summary.md)
## 解释面向对象

所谓面向对象是跟面向过程有区别的，面向对象简称是oop，
简单来说面向过程就是各种函数，大函数变小函数，调用小函数等等，然而面向对象就是一切皆对象，各种对象互相调用。

记住一件事：类是抽象的模板，实例才是具象的表现。类似于**你的DNA和你的性状的表达。**

## 举例说明定义方式。

```Py
class Student(object):
  """docstring for Student."""
  def __init__(self, arg):
    self.arg = arg
  def method1():
        pass


```


class特殊关键字表明了这是一个类。然后（）内部的object表示这个类是继承于**object类**，然后def的第一个通常就是这个__init__的方法，可以说是构造函数。

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

#### 三大特征

- 封装
- 继承
- 多态

## 类实现实例

```Python
class Stuent(object):
  """docstring for Stuent."""
  def __init__(self, arg):
    self.arg = arg

me =  Stuent(12)

```

这就实现了一个实例了，完全不需要new关键字，并且class也不能直接使用。并且在__init__中第一个参数self，在实现实例的时候是不需要注意到的，就是累中不需要第一个参数写self第一个参数写__init__()中的第二个数据就OK了。

下面看js中的类实现实例

```js

class Stuent{
  construct(name, year){
    this.name = name
    this.year = year
  }
}

const me = new Student(thomas, 12)
```
当然可以看得出来还是有很大的不同的地方的。其实我个人认为Python确实比js要来的典雅。更加的简洁。不过，说起来es6中的类也是很简洁的，也是很舒服的，不得不说编程语言的确是有了一定的发展的。


#### 和普通的函数相比，

在类中定义的函数只有一点不同，就是**第一个参数永远是实例变量self**，并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数

举例子

```py

class BaseAdapter(object):
    """The Base Transport Adapter"""

    def __init__(self):
        super(BaseAdapter, self).__init__()

    def send(self, request, stream=False, timeout=None, verify=True,
             cert=None, proxies=None):

```

## 数据的封装

```py

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

```
可以看得很清楚，这里面是有属性和方法的，而且分工很明确，属性的定义，方法的运用(并且运用了属性的值)是非常的明了的。


```py

class Student(object):
    def __init__(self, name, yaar, className):
        self.name = name
        self.yaar = yaar
        self.className = className
    def run(self):
        print('我们的名字是%s,并且我们的年龄是%s,我们来自于%s班级' % (self.name, self.yaar, self.className))

number1 = Student('thomashuke', 21, 4)

number1.run()

```


要注意这一段`print('我们的名字是%s,并且我们的年龄是%s,我们来自于%s班级' % (self.name, self.yaar, self.className))` 注意在前面使用了占位符%s后前后的连接使用的是% 至于后面那个括号，可有可无。最好有，这样更加分层简介。


## 再次提及访问限制

- 有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

- 双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量

所以来讲啊，Python中并没有像java中那种什么私有属性或者是private 被保护的属性这个实质性的东西，它能做的就是尽量的提醒你什么是什么，但是本质还是没变，所有的变量(包括常亮)其本质都是一个样子的。

所以

**老老实实的按照规矩来，什么问题都不会发生~~~！！！**

## 判断实例

`isinstance()`

```py

a = [1, 2]
isinstance(a, list)
>>> True

```
## 多态

调用方只管调用，不管细节，而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则：

对扩展开放：允许新增Animal子类；

对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。

## 继承树

继承还可以一级一级地继承下来，就好比从爷爷到爸爸、再到儿子这样的关系。而任何类，最终都可以追溯到根类object，这些继承关系看上去就像一颗倒着的树。比如如下的继承树

## 静态语言和动态语言

`不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子` 这是动态语言中的比较灵活的地方，比如说定义一个参数，这个参数要求是这个类的实例对象，因为下一步就是要求这个实例对象运行它的run()方法，但是如果传入进入一个对象它并不是实例对象，但是它也拥有run方法，系统也是认可的，这就是鸭子类型，长得像就是一样。但是Java等静态类型则不是，它要求的很严格，说是啥就是啥一点也不能有马虎。

## type()

判断这个对象拥有什么属性什么方法等

```py

type(123)
<class 'int'>
>>> type(a)
<class 'list'>
>>> type('12')
<class 'str'>

```
```py

>>> import types
>>> def fn():
...     pass
...
>>> type(fn)==types.FunctionType
True
>>> type(abs)==types.BuiltinFunctionType
True
>>> type(lambda x: x)==types.LambdaType
True
>>> type((x for x in range(10)))==types.GeneratorType
True

```

## isinstance()

```py

isinstance(a, list)
True

```

这个就是关于继承关系的。前者是后者的实例对象。
