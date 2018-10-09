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
### 
### 
### 
### 
