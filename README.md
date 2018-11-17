# Python
## 一，遇到的一些函数
### 1 eval函数 
1, eval() 函数用来执行一个字符串表达式，并返回表达式的值。
```
eval('pow(2,2)')
4
>>> eval('2 + 2')
4
```
2, 将**字符串**转成相应的对象（如list、tuple、dict和string之间的转换）
```
>>> a = "[[1,2], [3,4], [5,6], [7,8], [9,0]]"
>>> b = eval(a)
>>> b
[[1, 2], [3, 4], [5, 6], [7, 8], [9, 0]]
>>> a = "{1:'xx',2:'yy'}"
>>> c = eval(a)
>>> c
{1: 'xx', 2: 'yy'}
>>> a = "(1,2,3,4)"
>>> d = eval(a)
>>> d
(1, 2, 3, 4)
```
3, 利用反引号转换的字符串再反转回对象
```
>>> list1 = [1,2,3,4,5]
>>> `list1`
'[1, 2, 3, 4, 5]'
>>> type(`list1`)
<type 'str'>
>>> type(eval(`list1`))
<type 'list'>
>>> a = eval(`list1`)
>>> a
[1, 2, 3, 4, 5]
```

### 2 round函数 round(number[, ndigits])， round 对传入的数据进行四舍五入，如果ngigits不传，默认是0（就是说保留整数部分）.ngigits<0 的时候是来对整数部分进行四舍五入，返回的结果是浮点数.
### 3 raw_input() 用来获取控制台的输入。 raw_input() 将所有输入作为字符串看待，返回字符串类型。
### 4 find() 检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1。 str.find(str, beg=0, end=len(string))
### 5 pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
### 6 Python Socket模块中的IP转换函数： ntohl()之类的 http://blog.csdn.net/fan_hai_ping/article/details/8435140
### 7 这个网站是有关Ｕｂｕｎｔｕ上使用pyenv对Ｐｙｔｈｏｎ各版本进行整合：https://qiita.com/uryyyyyyy/items/268f8dc0d6ec3d7da7e3
### 8 https://www.cnblogs.com/chengd/articles/7287528.html  https://blog.csdn.net/CLHugh/article/details/75000104 (有关讲解Python类，讲得比较细)
>* 类Class：鸟; 类的方法（函数）：（鸟）会飞 ; 类的属性（变量）：爪子，翅膀
>* 实例：对象：麻雀，是（类Class）鸟 的一种 ; 对象方法（函数）：麻雀会飞 ; 对象的变量：麻雀有2个爪子，一对翅膀

>* 由于类起到模板的作用，因此，可以在创建实例的时候，把我们认为必须绑定的属性强制填写进去。这里就用到Python当中的一个内置方法__init__方法，例如Student类时，把name、score等属性绑上去。
>* __init__方法的第一参数永远是self，表示创建的类实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
>* 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器会自己把实例变量传进去
>* self.name = name的意思就是把外部传来的参数name的值赋值给Student类自己的属性变量self.name。
>* 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问.例如self.__name = name
>* 但是如果外部代码要获取name和score怎么办？可以给Student类增加get_name和get_score这样的方法：
```
def get_name(self):
        return self.__name
```
如果又要允许外部代码修改score怎么办？可以给Student类增加set_score方法：
```
def set_score(self, score):
        self.__score = score
```

>* 需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。

>* 有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”



### 9 https://blog.csdn.net/sun_wangdong/article/details/44428077 (有关讲解如何调用类中的构造函数，需要再看)
### 10 https://www.cnblogs.com/ToDoToTry/p/5635863.html (有关format函数的讲解)
### 11 https://blog.csdn.net/yilovexing/article/details/80577510   （*args 和 **kwargs的讲解）
### 12 http://lib.csdn.net/article/python/62942  (装饰器的讲解，从这个开始看)
### 13 http://python.jobbole.com/81683/ （从函数开始讲起到装饰器，一步一步非常细，以后可以多看，对函数理解很有帮助，）

1， 
```
def outer():
     def inner():
         print "Inside inner"
     return inner # 1
 
foo = outer() #2
foo # doctest:+ELLIPSIS
<function inner at 0x>
foo()
Inside inner
```
在#1处我把恰好是函数标识符的变量inner作为返回值返回出来。这并没有什么特殊的语法："把函数inner返回出来，否则它根本不可能会被调用到。"还记得变量的生存周期吗？每次函数outer被调用的时候，函数inner都会被重新定义，如果它不被当做变量返回的话，每次执行过后它将不复存在。

在#2处我们捕获住返回值 – 函数inner，将它存在一个新的变量foo里。我们能够看到，当对变量foo进行求值，它确实包含函数inner，而且我们能够对他进行调用。

2, Python支持一个叫做函数闭包的特性，用人话来讲就是，嵌套定义在非全局作用域里面的函数能够记住它在被定义的时候它所处的封闭命名空间。这能够通过查看函数的func_closure属性得出结论，这个属性里面包含封闭作用域里面的值。
```
def outer():
     x = 1
     def inner():
         print x # 1
     return inner
foo = outer()
foo.func_closure # doctest: +ELLIPSIS
(<cell at 0x: int object at 0x>,)
```
所有的东西都在python的作用域规则下进行工作：“x是函数outer里的一个局部变量。当函数inner在#1处打印x的时候，python解释器会在inner内部查找相应的变量，当然会找不到，所以接着会到封闭作用域里面查找，并且会找到匹配。

但是从变量的生存周期来看，该怎么理解呢？我们的变量x是函数outer的一个本地变量，这意味着只有当函数outer正在运行的时候才会存在。根据我们已知的python运行模式，我们没法在函数outer返回之后继续调用函数inner，在函数inner被调用的时候，变量x早已不复存在，可能会发生一个运行时错误。

万万没想到，返回的函数inner居然能够正常工作。Python支持一个叫做**函数闭包**的特性，用人话来讲就是，嵌套定义在非全局作用域里面的函数能够记住它在被定义的时候它所处的封闭命名空间。这能够通过查看函数的func_closure属性得出结论，这个属性里面包含封闭作用域里面的值（只会包含被捕捉到的值，比如x，如果在outer里面还定义了其他的值，封闭作用域里面是不会有的)

我的理解就是，inner里只调用了X的值，外部要是有别的值，就不会存在了。

每次函数outer被调用的时候，函数inner都会被重新定义。现在变量x的值不会变化，所以每次返回的函数inner会是同样的逻辑，假如我们稍微改动一下呢？
```
def outer(x):
     def inner():
         print x # 1
     return inner
print1 = outer(1)
print2 = outer(2)
print1()
1
print2()
2
```
从这个例子中你能够看到闭包 – 被函数记住的封闭作用域 – 能够被用来创建自定义的函数，本质上来说是一个硬编码的参数。事实上我们并不是传递参数1或者2给函数inner，我们实际上是创建了能够打印各种数字的各种自定义版本。

**闭包单独拿出来就是一个非常强大的功能， 在某些方面，你也许会把它当做一个类似于面向对象的技术：outer像是给inner服务的构造器，x像一个私有变量。使用闭包的方式也有很多：你如果熟悉python内置排序方法的参数key，你说不定已经写过一个lambda方法在排序一个列表的列表的时候基于第二个元素而不是第一个。现在你说不定也可以写一个itemgetter方法，接收一个索引值来返回一个完美的函数，传递给排序函数的参数key。**

不过，我们现在不会用闭包做这么low的事(⊙o⊙)…！相反，让我们再爽一次，写一个高大上的装饰器!
