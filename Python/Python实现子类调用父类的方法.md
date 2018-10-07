```
class A:
    def __init__(self):
        self.namea="aaa"
    def funca(self):
        print "function a : %s"%self.namea
class B(A):
    def __init__(self):
        self.nameb="bbb"
    def funcb(self):
        print "function b : %s"%self.nameb
b=B()
print b.nameb
b.funcb()
b.funca()
```
运行后会报错：
```
bbb
function b : bbb
Traceback (most recent call last):
  File "D:workbenchpythonMyPythonProjectteststudyoverwrite_method.py", line 19, in <module>
    print b.funca()
  File "D:workbenchpythonMyPythonProjectteststudyoverwrite_method.py", line 6, in funca
    print "function a : %s"%self.namea
AttributeError: B instance has no attribute 'namea'
```
两种方法解决：第一种（一处变化）
```
class A:
    def __init__(self):
        self.namea="aaa"
    def funca(self):
        print "function a : %s"%self.namea
class B(A):
    def __init__(self):
        # 这一行解决了问题
        A.__init__(self)
        self.nameb="bbb"
    def funcb(self):
        print "function b : %s"%self.nameb
```
第二种：(两处变化)
```
#父类需要继承object对象
class A(object):
    def __init__(self):
        self.namea="aaa"
    def funca(self):
        print "function a : %s"%self.namea
class B(A):
    def __init__(self):
        #这一行解决问题
        super(B,self).__init__()
        self.nameb="bbb"
    def funcb(self):
        print "function b : %s"%self.nameb
```
让类A继承自object类，这样才能使用super函数，因为这是python的“新式类”支持的特性。当前的class和对象可以作为super函数的参数使用，调用函数返回的对象的任何方法都是调用超类的方法，而不是当前类的方法。

优劣： 
- 方法一更直观，方法二可以一次初始化所有超类 
- super函数比在超类中直接调用未绑定方法更直观，但是其最大的优点是如果子类继承了多个父类，它只需要使用一次super函数就可以。然而如果没有这个需求，直接使用A.init(self)更直观一些。
