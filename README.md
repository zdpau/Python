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
### 11 https://blog.csdn.net/yilovexing/article/details/80577510   *args 和 **kwargs的讲解
