import asyncio

async def print_something():
    await asyncio.sleep(1)
    print("SOMETHING")
    return "finished"

async def main():
    print("MAIN")

    task = asyncio.create_task(print_something())

    print("main again")
    result = await task
    print(result)


asyncio.run(main())
