https://www.jianshu.com/p/004553ac771a

1,协程有四个状态，可以使用inspect.getgeneratorstate(...)函数确定：
* GEN_CREATED    # 等待开始执行
* GEN_RUNNING    # 解释器正在执行（只有在多线程应用中才能看到这个状态）
* GEN_SUSPENDED  # 在yield表达式处暂停
* GEN_CLOSED     # 执行结束
```
import inspect

# 协程使用生成器函数定义：定义体中有yield关键字。
def simple_coroutine():
    print('-> coroutine started')
    # yield 在表达式中使用；如果协程只需要从客户那里接收数据，yield关键字右边不需要加表达式（yield默认返回None）
    x = yield
    print('-> coroutine received:', x)


my_coro = simple_coroutine()
my_coro # 和创建生成器的方式一样，调用函数得到生成器对象。
# 协程处于 GEN_CREATED (等待开始状态)
print(inspect.getgeneratorstate(my_coro))

my_coro.send(None)
# 首先要调用next()函数，因为生成器还没有启动，没有在yield语句处暂停，所以开始无法发送数据
# 发送 None 可以达到相同的效果 my_coro.send(None) 
next(my_coro)
# 此时协程处于 GEN_SUSPENDED (在yield表达式处暂停)
print(inspect.getgeneratorstate(my_coro))

# 调用这个方法后，协程定义体中的yield表达式会计算出42；现在协程会恢复，一直运行到下一个yield表达式，或者终止。
my_coro.send(42)
print(inspect.getgeneratorstate(my_coro))
```
send方法的参数会成为暂停yield表达式的值，所以，仅当协程处于暂停状态是才能调用send方法。
如果协程还未激活（GEN_CREATED 状态）要调用next(my_coro) 激活协程，也可以调用my_coro.send(None)
