import asyncio
import time

start_time = time.time()


async def main():
    print("hello")
    task1 = asyncio.create_task(thing())
    task2 = asyncio.create_task(thing2())
    # value = await task2
    # print(value)


async def thing():
    print("from thing")
    print("task1 complete")
    await asyncio.sleep(2)


async def thing2():
    print("from thing2")
    print("task2 complete")


if __name__ == "__main__":
    asyncio.run(main())
    print("after")
    print("--- %s seconds ---" % (time.time() - start_time))
