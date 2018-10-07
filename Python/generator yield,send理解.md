https://www.cnblogs.com/xhcdream/p/8304953.html

1, 第一种创建生成器的方法:使用()创建生成器，如果使用[]则创建列表。然后可以通过next一直产生新的数据，直到最后一个报异常，通过for遍历不会报异常, 也可以使用a.__next__(), 就是next(a)=a.__next__(), 也可以通过for遍历生成器.
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
