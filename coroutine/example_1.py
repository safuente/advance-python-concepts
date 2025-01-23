"""A coroutine is a special type of Python generator which returns the control
back to the event loop on encountering the await keyword. It uses only one thread"""
import asyncio


async def my_coroutine():
    print("Starting my coroutine")
    await asyncio.sleep(2)
    print("Coroutine finished")

# Execute coroutine with run
asyncio.run(my_coroutine())
