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
