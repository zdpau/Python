# Awaitables

我们说如果一个对象可以在await表达式中使用，那么它就是一个awaitable对象。许多asyncio API旨在接受awaitable。

**There are three main types of awaitable objects: coroutines, Tasks, and Futures.**

## coroutine
Python coroutines are awaitables and therefore can be awaited from other coroutines:
```
import asyncio

async def nested():
    return 42

async def main():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    nested()

    # Let's do it differently now and await it:
    print(await nested())  # will print "42".

asyncio.run(main())

output:
__main__:2: RuntimeWarning: coroutine 'nested' was never awaited
43
```
**Important**: In this documentation the term “coroutine” can be used for two closely related concepts:
>* a coroutine function: an async def function;
>* a coroutine object: an object returned by calling a coroutine function.

## Tasks
Tasks are used to schedule coroutines concurrently. 任务用于同时调度协同程序。

When a coroutine is wrapped into a Task with functions like asyncio.create_task() the coroutine is automatically scheduled to run soon:使用asyncio.create_task（）等函数将协程包装到Task中时，协程会自动安排为很快运行：
```
import asyncio

async def nested():
    return 42

async def main():
    # Schedule nested() to run soon concurrently with "main()".安排nested（）与“main（）”同时运行
    task = asyncio.create_task(nested())

    # "task" can now be used to cancel "nested()", or can simply be awaited to wait until it is complete:
    # “task”现在可以用来取消“nested()”，或者只是等待它等到它完成:
    await task

asyncio.run(main())

output:什么也没有
```
## Futures
A Future is a special low-level awaitable object that represents an eventual result of an asynchronous operation.(Future是一个特殊的low-level awaitable对象，它表示异步操作的最终结果。)

When a Future object is awaited it means that the coroutine will wait until the Future is resolved in some other place.(当等待Future对象时，它意味着协程将等到Future在其他地方解析。)

Future objects in asyncio are needed to allow callback-based code to be used with async/await.（需要asyncio中的Future对象来允许基于回调的代码与async / await一起使用。）

Normally there is no need to create Future objects at the application level code.（通常，不需要在应用程序级代码中创建Future对象。）

Future objects, sometimes exposed by libraries and some asyncio APIs, can be awaited:
```
async def main():
    await function_that_returns_a_future_object()

    # this is also valid:
    await asyncio.gather(
        function_that_returns_a_future_object(),
        some_python_coroutine()
    )
```
A good example of a low-level function that returns a Future object is loop.run_in_executor().
