import asyncio


async def factorial(name, num):
    f = 1
    for i in range(2, num + 1):
        print(f"Task {name}: Compute factorial({i})...")
        f *= i
    print(f"Task {name}: factorial({num}) = {f}")


async def main():
    await asyncio.gather(
        factorial("Task A", 5),
        factorial("Task B", 3),
        factorial("Task C", 10),
    )

asyncio.run(main())
