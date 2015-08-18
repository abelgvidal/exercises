import asyncio

@asyncio.coroutine
def greet_every_two_seconds():  
    while True:
        print('Hello World')
        yield from asyncio.sleep(2)
        print('After back from sleep')

loop = asyncio.get_event_loop()  
loop.run_until_complete(greet_every_two_seconds())  
