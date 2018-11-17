https://zhuanlan.zhihu.com/p/43581980

### 1， __ future__模块允许用户导入新版 Python 的功能: from __future__ import print_function
### 2, Python 通过许多内置功能支持函数式编程。map() 函数是最有用的函数之一——特别是当它与 lambda 函数结合使用时。
```
x = [1, 2, 3]
y = map(lambda x : x + 1 , x)
# prints out [2,3,4]
print(list(y))
```
map() 将一个简单的 lambda 函数应用于 x 中的每个元素。它返回一个 map 对象，该对象可以被转换成可迭代的对象，如列表或元组。
### 3,用两个列表来组成一部词典吗?
```
keys = ['a', 'b', 'c']
vals = [1, 2, 3]
zipped = dict(zip(keys, vals))

zipped = {'a': 1, 'b': 2, 'c': 3}
```
zip() 内置函数使用多个可迭代对象作为输入并返回元组列表。每个元组按位置索引对输入对象的元素进行分组。
## 几种高级的数据结构 http://blog.jobbole.com/65218/
### 1, Counter()
1，统计一个list中出现的各个item的次数；2，统计一个list中不同item的数目；3，1之后的结果，对结果进行分组；4，找出一个字符串中出现频率最高的单词
```
from collections import Counter
 
li = ["Dog", "Cat", "Mouse", 42, "Dog", 42, "Cat", "Dog"]
a = Counter(li)
1, print a # Counter({'Dog': 3, 42: 2, 'Cat': 2, 'Mouse': 1})
2, print len(set(li)) # 4
3, print "{0} : {1}".format(a.values(),a.keys())  # [1, 3, 2] : ['Mouse', 'Dog', 'Cat']
 print(a.most_common(3)) # [('Dog', 3), ('Cat', 2), ('Mouse', 1)]
```
### 2, deque()是一种由队列结构扩展而来的双端队列(double-ended queue)，队列元素能够在队列两端添加或删除。因此它还被称为头尾连接列表(head-tail linked list)

Deque支持线程安全的，经过优化的append和pop操作，在队列两端的相关操作都能够达到近乎O(1)的时间复杂度。虽然list也支持类似的操作，但是它是对定长列表的操作表现很不错，而当遇到pop(0)和insert(0, v)这样既改变了列表的长度又改变其元素位置的操作时，其复杂度就变为O(n)了。

```
from collections import deque
q = deque(range(5))
q.append(5)
q.appendleft(6)
print q
print q.pop()
print q.popleft()
print q.rotate(3) # 调用rotate，不返回结果；正数就是往右移三个
print q
print q.rotate(-1) # 负数，就是往左移几个
print q
 
# deque([6, 0, 1, 2, 3, 4, 5])
# 5
# 6
# None
# deque([2, 3, 4, 0, 1])
# None
# deque([3, 4, 0, 1, 2])
```
### 3，defaultdict()：这个类型除了在处理不存在的键的操作之外与普通的字典完全相同。当查找一个不存在的键操作发生时，它的default_factory会被调用，提供一个默认的值，并且将这对键值存储下来。其他的参数同普通的字典方法dict()一致。

defaultdict对象在当你希望使用它存放追踪数据的时候很有用。

### 还有很多看网站
### 
