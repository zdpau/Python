https://www.cnblogs.com/xhcdream/p/8304953.html


1, 第一种创建生成器的方法:使用()创建生成器，如果使用[]则创建列表。然后可以通过next一直产生新的数据，直到最后一个报异常，通过for遍历不会报异常, 也可以使用a.__next__(), 就是next(a)=a.__next__(), 也可以通过for遍历生成器.**最开始next(t)=t.send(None)**

其实next()和send()在一定意义上作用是相似的，区别是send()可以传递yield表达式的值进去，而next()不能传递特定的值，只能传递None进去。因此，我们可以看做
c.next() 和 c.send(None) 作用是一样的。
```
a = (x**2 for x in range(1, 5))

第一种输出：
print(next(a)) #输出1
print(a.__next__()) #输出4
print(next(a)) #输出9

第二种输出：
for i in a:
    print(i) #输出1,4,9,16，不想上面那样一个一个出来
```
第二种创建生成器的方法：
```
def createNum(n):
    for i in range(n):
        yield i**2

第一种输出：
for i in createNum(5):
    print(i)  #输出0,1,4,9,16，因为用的for循环，所以全部出来
    
第二种输出：
t = createNum(n) # 这一步很重要，
t.__next__() 或者 next(t) 或者 t.send(None) 
```
第一步一般先用next方法，用send（None）也行，但不好。所以，在调用send方法之前，还是先调用一次next方法为好。详细的可以看下面。

2, generator.send(value): send方法有一个参数，该参数指定的是上一次被挂起的yield语句的返回值。send的作用相当于使生成器继续运行，并且传递的参数为yield的返回值。
```
def h():
    print 'Wen Chuan'
    yield 5
    print 'Fighting!'

c = h()
c.next()
```
输出结果：
```
Wen Chuan
Fighting!
```
当我们再调用c.next()：
```
Traceback (most recent call last):
  File "/home/evergreen/Codes/yidld.py", line 11, in <module>
    c.next()
StopIteration
```
由于后面没有yield了，因此会拋出异常.

**又一个例子，这个很关键**：
```
def h():
    print("1")
    m = yield 5  
    print(m)
    d = yield 12
    print ('We are together!')

c = h()
next(c)
```
输出结果：
```
1
5
```
再输入c.send("666")**（(yield 5)表达式被赋予了'666'）**，输出结果:
```
666
12
```

再来个例子：
```
def test():
    i = 1
    while i < 5:
        temp = yield i**2
        print(temp)
        i += 1

t = test()
```
```
next(t)
1
next(t) # 这里按理说不应该用next()，应该用send(""),
None
4
next(t)
None
9

next(t)
1
t.send("a")
a
4
t.send(23)
23
9
```


