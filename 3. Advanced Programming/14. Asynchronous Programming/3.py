import asyncio

async def fetch_data():
    print("start fetching")
    await asyncio.sleep(2)
    print("done fetching")
    return [1, 2, 3, 4, 5, 6]

async def run_algorithm():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.5)

async def main():
    data = await asyncio.gather(fetch_data())
    await run_algorithm()
    print(await data)


asyncio.run(main())