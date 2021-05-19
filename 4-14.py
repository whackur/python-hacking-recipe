import asyncio


async def main():
    await asyncio.sleep(0)
    return 42


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
try:
    print(loop.run_until_complete(main()))
finally:
    asyncio.set_event_loop(None)
    loop.close()
