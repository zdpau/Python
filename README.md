# Python
## 一，遇到的一些函数
### 1 eval函数 eval() 函数用来执行一个字符串表达式，并返回表达式的值。
### 2 round函数 round(number[, ndigits])， round 对传入的数据进行四舍五入，如果ngigits不传，默认是0（就是说保留整数部分）.ngigits<0 的时候是来对整数部分进行四舍五入，返回的结果是浮点数.
### 3 raw_input() 用来获取控制台的输入。 raw_input() 将所有输入作为字符串看待，返回字符串类型。
### 4 find() 检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1。 str.find(str, beg=0, end=len(string))
### 5 pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
### 6 Python Socket模块中的IP转换函数： ntohl()之类的 http://blog.csdn.net/fan_hai_ping/article/details/8435140
### 7 这个网站是有关Ｕｂｕｎｔｕ上使用pyenv对Ｐｙｔｈｏｎ各版本进行整合：https://qiita.com/uryyyyyyy/items/268f8dc0d6ec3d7da7e3
### 8 https://www.cnblogs.com/chengd/articles/7287528.html (有关讲解Python类，讲得比较细)
### 9 https://blog.csdn.net/sun_wangdong/article/details/44428077 (有关讲解如何调用类中的构造函数，需要再看)
### 10 https://www.cnblogs.com/ToDoToTry/p/5635863.html (有关format函数的讲解)
### 11 https://blog.csdn.net/itlance_ouyang/article/details/52489674 （Python命令行命令getopt,argparse）
### 12 https://blog.csdn.net/a1964543590/article/details/69791760 （这篇有关argparse讲得比较细）
### 13 https://blog.csdn.net/ei1990/article/details/76423277 (flags的对比，argparse,tf两种)
**总结起来的话，tf.app.flags.DEFINE_xxx()就是添加命令行的optional argument（可选参数），而tf.app.flags.FLAGS可以从对应的命令行参数取出参数。**
