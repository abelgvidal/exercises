import asyncio

async def hello():
    await asyncio.sleep(1)
    print('hello')


async def test():
    print('here')
    await hello()
    await asyncio.sleep(0.5)
    print('there')
    

loop = asyncio.get_event_loop()
loop.run_until_complete(test())

"""
here
hello
there
"""


import asyncio

async def hello():
    await asyncio.sleep(1)
    print('hello')


async def test():
    print('here')
    asyncio.ensure_future(hello())
    await asyncio.sleep(0.5)
    print('there')
    await asyncio.sleep(2)
    

loop = asyncio.get_event_loop()
loop.run_until_complete(test())

""" 
here
there
hello
"""
