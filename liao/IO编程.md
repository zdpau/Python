由于程序和运行时数据是在内存中驻留，由CPU这个超快的计算核心来执行，涉及到数据交换的地方，通常是磁盘、网络等，就需要IO接口。

通常，程序完成IO操作会有Input和Output两个数据流。当然也有只用一个的情况，比如，从磁盘读取文件到内存，就只有Input操作，反过来，把数据写到磁盘文件里，就只是一个Output操作。

IO编程中，Stream（流）是一个很重要的概念，可以把流想象成一个水管，数据就是水管里的水，但是只能单向流动。Input Stream就是数据从外面（磁盘、网络）流进内存，Output Stream就是数据从内存流到外面去。对于浏览网页来说，浏览器和新浪服务器之间至少需要建立两根水管，才可以既能发数据，又能收数据。

**同步和异步的区别就在于是否等待IO执行的结果**。很明显，使用异步IO来编写程序**性能会远远高于同步IO**，但是异步IO的**缺点是编程模型复杂**。想想看，你得知道什么时候通知你“汉堡做好了”，而通知你的方法也各不相同。如果是服务员跑过来找到你，这是**回调模式**，如果服务员发短信通知你，你就得不停地检查手机，这是**轮询模式**。总之，异步IO的复杂度远远高于同步IO。

操作IO的能力都是由操作系统提供的，每一种编程语言都会把操作系统提供的低级C接口封装起来方便使用，Python也不例外。我们后面会详细讨论Python的IO编程接口。

### 文件读写
在磁盘上读写文件的功能都是由操作系统提供的，现代操作系统不允许普通的程序直接操作磁盘，所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），或者把数据写入这个文件对象（写文件）。

代码看原文f.read(里面的参数记一下) 然后 f.close(). Python引入了with语句来自动帮我们调用close()方法：

调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。

如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：



### 操作文件和目录
```
>>> import os

>>> os.name # 操作系统类型
'posix' # 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。

>>> os.uname() # 要获取详细的系统信息

>>> os.environ # 环境变量

要获取某个环境变量的值，可以调用os.environ.get('key')
>>> os.environ.get('PATH')
'/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/opt/X11/bin:/usr/local/mysql/bin'
>>> os.environ.get('x', 'default')
'default'


查看、创建和删除目录可以这么调用：

# 查看当前目录的绝对路径:
>>> os.path.abspath('.')
'/Users/michael'

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
>>> os.path.join('/Users/michael', 'testdir')
'/Users/michael/testdir'

# 然后创建一个目录:
>>> os.mkdir('/Users/michael/testdir')

# 删掉一个目录:
>>> os.rmdir('/Users/michael/testdir')

# 对文件重命名:
>>> os.rename('test.txt', 'test.py')

# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数
# 要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
>>> os.path.split('/Users/michael/testdir/file.txt')
('/Users/michael/testdir', 'file.txt')

# os.path.splitext()可以直接让你得到文件扩展名
>>> os.path.splitext('/path/to/file.txt')
('/path/to/file', '.txt')

# 删掉文件:
>>> os.remove('test.py')
```

要列出当前目录下的所有目录:
```
 [x for x in os.listdir('.') if os.path.isdir(x)]
```

要列出所有的.py文件，也只需:
```
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
```
