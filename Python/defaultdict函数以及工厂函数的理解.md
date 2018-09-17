https://blog.csdn.net/real_ray/article/details/17919289 

https://blog.csdn.net/the_little_fairy___/article/details/80551538

### 1，defaultdict的作用是在于，当字典里的key不存在但被查找时，返回的不是keyError而是一个默认值。

defaultdict(function_factory)接受一个工厂函数作为参数，构建的是一个类似dictionary的对象，其中keys的值，自行确定赋值，但是values的类型，是function_factory的类实例，而且具有默认值。比如defaultdict(int)则创建一个类似dictionary对象，里面任何的values都是int的实例，而且就算是一个不存在的key, d[key] 也有一个默认值，这个默认值是int类型值0. 

factory_function可以是list、set、str等等，作用是当key不存在时，返回的是工厂函数的默认值，比如list对应[ ]，str对应的是空字符串，set对应set( )，int对应0

### 2，dict.setdefault()方法来设置默认值：dict.setdefault()方法接收两个参数，第一个参数是健的名称，第二个参数是默认值。假如字典中不存在给定的键，则返回参数中提供的默认值；反之，则返回字典中保存的值。**collections.defaultdict(list)使用起来效果和运用dict.setdefault()比较相似。**

### 3，什么是工厂函数： 
来自python 核心编程的解释： 

  Python 2.2 统一了类型和类， 所有的内建类型现在也都是类， 在这基础之上， 原来的所谓内建转换函数像int(), type(), list() 等等， 现在都成了工厂函数。 也就是说虽然它们看上去有点象函数， 实质上他们是类。当你调用它们时， 实际上是生成了该类型的一个实例， 就像工厂生产货物一样。 

看这篇： https://blog.csdn.net/universe_ant/article/details/51245931
