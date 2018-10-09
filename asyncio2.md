http://masnun.com/2015/11/20/python-asyncio-future-task-and-the-event-loop.html

### Event loop
On any platform, when we want to do something asynchronously, it usually involves an event loop. An event loop is a loop that can register tasks to be executed, execute them, delay or even cancel them and handle different events related to these operations. Generally, we schedule multiple async functions to the event loop. The loop runs one function, while that function waits for IO, it pauses it and runs another. When the first function completes IO, it is resumed. Thus two or more functions can co-operatively run together. This the main goal of an event loop.

在任何平台上，当我们想要异步执行某些操作时，它通常涉及事件循环。事件循环是一个循环，可以注册要执行的任务，执行它们，延迟甚至取消它们，并处理与这些操作相关的不同事件。通常，我们为事件循环安排多个异步函数。 循环运行一个函数，而该函数等待IO，它暂停它并运行另一个。 当第一个函数完成IO时，它将恢复。 因此，两个或更多个功能可以协同地一起运行。 这是事件循环的主要目标。

The event loop can also pass resource intensive functions to a thread pool for processing. The internals of the event loop is quite complex and we don’t need to worry much about it right away. We just need to remember that the event loop is the mechanism through which we can schedule our async functions and get them executed.

事件循环还可以将资源密集型函数传递给线程池进行处理。 事件循环的内部非常复杂，我们不需要立即担心它。 我们只需要记住，事件循环是我们可以通过它调度异步函数并执行它们的机制.

### Futures / Tasks
If you are into Javascript too, you probably know about Promise. In Python we have similar concepts – Future/Task. A Future is an object that is supposed to have a result in the future. A Task is a subclass of Future that wraps a coroutine. When the coroutine finishes, the result of the Task is realized.

如果你也是Javascript，你可能知道Promise。 在Python中，我们有类似的概念 - Future / Task。 “Future"是一个应该在未来产生结果的对象。 Task是包装协程的Future的子类。 当协程完成时，task的结果就实现了。

### Coroutines
It’s a way of pausing a function and returning a series of values periodically. A coroutine can pause the execution of the function by using the yield yield from or await (python 3.5+) keywords in an expression. The function is paused until the yield statement actually gets a value.

这是一种暂停函数并定期返回一系列值的方法。 协程可以通过使用表达式中的yield yield或awaithon 3.5+）关键字来暂停函数的执行。 该函数暂停，直到yield语句实际获得一个值。

### Fitting Event Loop and Future/Task Together
It’s simple. We need an event loop and we need to register our future/task objects with the event loop. The loop will schedule and run them. We can add callbacks to our future/task objects so that we can be notified when a future has it’s results.

这很简单。 我们需要一个事件循环，我们需要使用事件循环注册我们的future / task对象。 循环将调度并运行它们。 我们可以为我们的future / task对象添加回调，以便在将来有结果时通知我们。

Very often we choose to use coroutines for our work. We wrap a coroutine in Future and get a Task object. When a coroutine yields, it is paused. When it has a value, it is resumed. When it returns, the Task has completed and gets a value. Any associated callback is run. If the coroutine raises an exception, the Task fails and not resolved.

我们经常选择使用coroutines来完成我们的工作。 我们在Future中包装一个coroutine并获取一个Task对象。 当coroutine yield时，它会暂停。当它有一个值时，它会恢复。 返回时，Task已完成并获取值。 运行任何关联的回调。 如果协同程序引发异常，则任务失败并且未解决。

下面是一些例子：
```
import asyncio
 
@asyncio.coroutine
def slow_operation():
    # yield from suspends execution until there's some result from asyncio.sleep
    yield from asyncio.sleep(1)
 
    # our task is done, here's the result
    return 'Future is done!'
 
 
def got_result(future):
    print(future.result())
 
 
# Our main event loop
loop = asyncio.get_event_loop()
 
# We create a task from a coroutine returned by slow_operation()  从slow_operation返回的协程创建一个任务
task = loop.create_task(slow_operation())
 
# Please notify us when the task is complete
task.add_done_callback(got_result) # adds a callback to our task
 
# The loop will close when the task has resolved
loop.run_until_complete(task) # runs the event loop until the task is realized. As soon as it has value, the loop terminates.
```
The run_until_complete function is a nice way to manage the loop. Of course we could do this:
```
import asyncio
 
 
async def slow_operation():
    await asyncio.sleep(1)
    return 'Future is done!'
 
 
def got_result(future):
    print(future.result())
 
    # We have result, so let's stop
    loop.stop()
 
 
loop = asyncio.get_event_loop()
task = loop.create_task(slow_operation())
task.add_done_callback(got_result)
 
# We run forever
loop.run_forever()
```
Here we make the loop run forever and from our callback, we explicitly shut it down when the future has resolved.
在这里，我们使循环永远运行，并且从我们的回调中，当future已经解决时，我们明确地将其关闭。
