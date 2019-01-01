https://www.cnblogs.com/elie/p/5876210.html

Python中3种方式定义类方法, 常规方式, @classmethod修饰方式, @staticmethod修饰方式.
```
class A(object):
    def foo(self, x):
        print("executing foo(%s,%s)" % (self, x))
        print('self:', self)
    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s,%s)" % (cls, x))
        print('cls:', cls)
    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % x)    
a = A()
```

**普通的类方法foo()需要通过self参数隐式的传递当前类对象的实例。 @classmethod修饰的方法class_foo()需要通过cls参数传递当前类对象。@staticmethod修饰的方法定义与普通函数是一样的。** 

**self和cls的区别不是强制的，只是PEP8中一种编程风格，slef通常用作实例方法的第一参数，cls通常用作类方法的第一参数。即通常用self来传递当前类对象的实例，cls传递当前类对象。** 

问题：@staticmethod修饰的方法函数与普通的类外函数，为什么不直接使用普通函数？

@staticmethod是把函数嵌入到类中的一种方式，函数就属于类，同时表明函数不需要访问这个类。通过子类的继承覆盖，能更好的组织代码。
