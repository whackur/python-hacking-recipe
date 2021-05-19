import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    task1 = asyncio.create_task(say_after(1, "hello"))
    task2 = asyncio.create_task(say_after(2, "world"))
    await task1
    await task2


if __name__ == "__main__":
    print(f"started at {time.strftime('%X')}")
    asyncio.run(main())
    print(f"finished at {time.strftime('%X')}")
