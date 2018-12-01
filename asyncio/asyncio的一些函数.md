* async def 用来定义异步函数，其内部有异步操作。每个线程有一个事件循环，主线程调用asyncio.get_event_loop()时会创建事件循环，你需要把异步的任务丢给这个循环的run_until_complete()方法，事件循环会安排协同程序的执行。
* await 关键字加在需要等待的操作前面。
* 如果我们需要请求多个URL该怎么办呢，同步的做法访问多个URL只需要加个for循环就可以了。但异步的实现方式并没那么容易，在之前的基础上需要将hello()包装在asyncio的Future对象中，然后将Future对象列表作为任务传递给事件循环。
* 如果不预激,那么协程没什么用，调用g.send(x)之前。记住一定要调用next(g)。

在Python中，一个异步的函数我们通常叫它协程。


1, class asyncio.AbstractEventLoop  事件循环的抽象基类。

2, AbstractEventLoop.run_until_complete(future)
```
Run until the Future is done. 运行直到 Future 完成。

If the argument is a coroutine object, it is wrapped by ensure_future(). 
如果参数是 协同对象，它被 ensure_future() 包装。

Return the Future’s result, or raise its exception. 
返回未来的结果，或提出它的异常。
```

3, AbstractEventLoop.close()
```
Close the event loop. The loop must not be running. Pending callbacks will be lost.　
关闭事件循环。循环不能运行。待处理(挂起)的回调将丢失。

This clears the queues and shuts down the executor, but does not wait for the executor to finish.
这会清除队列并关闭执行程序，但不会等待执行程序完成。

This is idempotent and irreversible. No other methods should be called after this one.
这是幂等的，不可逆转的。在此之后不应该调用其他方法。
```

4, AbstractEventLoop.create_future()
```
Create an asyncio.Future object attached to the loop.
创建一个附加到循环的asyncio.Future对象。

This is a preferred way to create futures in asyncio, as event loop implementations can provide alternative implementations of the Future class (with better performance or instrumentation).
这是在asyncio中创建future的首选方法，因为事件循环实现可以提供Future类的替代实现（具有更好的性能或工具）。
```

5, AbstractEventLoop.create_task(coro)
```
Schedule the execution of a coroutine object: wrap it in a future. Return a Task object.
安排coroutine对象的执行：在future中包装它。返回一个Task对象。

Third-party event loops can use their own subclass of Task for interoperability. In this case, the result type is a subclass of Task.
第三方事件循环可以使用它们自己的Task子类来实现互操作性。在这种情况下，结果类型是Task的子类。
```

6, AbstractEventLoop.call_soon(callback, *args, context=None)
```
Arrange for a callback to be called as soon as possible. The callback is called after call_soon() returns, when control returns to the event loop.
安排一个callback被尽快调用。当控制返回到事件循环时，在call_soon（）返回后callback被调用。

This operates as a FIFO queue, callbacks are called in the order in which they are registered. Each callback will be called exactly once.
它作为FIFO队列运行，回调按照它们的注册顺序调用。每个回调将被调用一次。

Any positional arguments after the callback will be passed to the callback when it is called.
回调后的任何位置参数都会在调用时传递给回调。

An optional keyword-only context argument allows specifying a custom contextvars.Context for the callback to run in. The current context is used when no context is provided.

An instance of asyncio.Handle is returned, which can be used to cancel the callback.

Use functools.partial to pass keywords to the callback.
```

7, (18.5.2.4. 事件循环策略和默认策略)(不是很理解)

事件循环管理被抽象为 policy 模式，为自定义平台和框架提供最大的灵活性。在进程的整个执行过程中，单个全局策略对象基于调用上下文来管理对进程可用的事件循环。策略是实现 AbstractEventLoopPolicy 接口的对象。

对于 asyncio 的大多数用户，策略从不必显式地处理，因为默认全局策略是足够的。

**默认策略将上下文定义为当前线程，并且管理与 asyncio 交互的每个线程的事件循环。模块级函数 get_event_loop() 和 set_event_loop() 提供对由默认策略管理的事件循环的方便访问。**

8, asyncio.get_event_loop(): Equivalent to calling get_event_loop_policy().get_event_loop().

**class asyncio.AbstractEventLoopPolicy**

Event loop policy.
```
get_event_loop()
Get the event loop for the current context.
获取当前上下文的事件循环。

Returns an event loop object implementing the AbstractEventLoop interface. In case called from coroutine, it returns the currently running event loop.
返回实现AbstractEventLoop接口的事件循环对象。在从coroutine调用的情况下，它返回当前运行的事件循环。

Raises an exception in case no event loop has been set for the current context and the current policy does not specify to create one. It must never return None.
如果没有为当前上下文设置事件循环并且当前策略未指定创建一个事件，则引发异常。它绝不能返回None。
```

9, coroutine

coroutine can do:
协同程序可以执行的操作：
```
result = await future 或 result = yield from future - 挂起协程直到future完成，然后返回future的结果，或引发一个异常，它将被传播。（如果future被取消，它将引发一个 CancelledError异常。）注意Task是future，关于future的一切也适用于task。

result = await coroutine 或 result = yield from coroutine - 等待另一个协程生成结果（或引发异常，这将被传播）。coroutine表达式必须是对另一个协程的调用。

return expression - 使用 await 或 yield from 向正在等待此协程的协程产生结果。

raise exception - 在使用 await 或 yield from 等待此协程的协程中引发异常。
```

调用协程不会启动其代码运行 - 调用返回的协程对象在您安排其执行之前不会执行任何操作。**有两种基本方法来启动它运行：从另一个协同程序调用 await coroutine 或 yield from coroutine （假设另一个协程已经运行！），或者使用 ensure_future() 函数或 AbstractEventLoop.create_task() 方法调度它的执行。**

Coroutines (and tasks) can only run when the event loop is running.(协程（和任务）只能在事件循环运行时运行。)
