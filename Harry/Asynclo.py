import asyncio
import time

async def f1():
    time.sleep(1)
    await asyncio.sleep(1)
    print('func 1')

async def f2():
    time.sleep(2)
    await asyncio.sleep(1)
    print('func 2')

async def f3():
    time.sleep(3)
    await asyncio.sleep(1)
    print('func 3')

# async def main():
#     await f1() #running in sequence 
#     await f2()
#     await f3()

# asyncio.run(main())


# async def main1():
#     task = asyncio.create_task(f1()) #to make it a task, so it will run when it can, regardless of order
#     await f2()
#     await f3()

# asyncio.run(main1())

async def main2():
    tasks = await asyncio.gather( #to run all functions at once
        f1(),
        f2(),
        f3()
        )
    print(tasks)

asyncio.run(main2())
