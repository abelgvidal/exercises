import asyncio

async def slow_operation(future):
    await asyncio.sleep(2)
    print("-----> slow operation")
    future.set_result('Future is done!')

loop = asyncio.get_event_loop()
future = asyncio.Future()
asyncio.ensure_future(slow_operation(future))
print("i ensured the future")
loop.run_until_complete(future)
print("task is completed")
print(future.result())
loop.close()


"""
i ensured the future
-----> slow operation
task is completed
Future is done!
"""