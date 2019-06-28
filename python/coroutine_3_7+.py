import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(10, "Hello")
    await say_after(20, "world")
    # 30s cost
    print(f"finished at {time.strftime('%X')}")
asyncio.run(main())


async def main2():
    task1 = asyncio.create_task(say_after(10, "hello"))
    task2 = asyncio.create_task(say_after(20, "world"))

    print(f"started at {time.strftime('%X')}")

    await task1
    await task2
    # 20s cost, concurrently

    print(f"started at {time.strftime('%X')}")
asyncio.run(main2())
