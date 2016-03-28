import asyncio
import aiohttp
from aiohttp import web
import json

WEBSITES = ['http://www.lpsz.org/', 'http://www.lpsz.org/bus/', 'http://www.lpsz.org/']

async def handle(request):
    # Fire up 3 requests in parallel
    coroutines = [aiohttp.request('get', website) for website in WEBSITES]

    # Wait for those requests to complete
    results = await asyncio.gather(*coroutines, return_exceptions=True)

    # Analyze results
    response_data = {
        website: not isinstance(result, Exception) and result.status == 200
        for website, result in zip(WEBSITES, results)
    }

    # Build JSON response
    body = json.dumps(response_data).encode('utf-8')
    return web.Response(body=body, content_type="application/json")

loop = asyncio.get_event_loop()
app = web.Application(loop=loop)
app.router.add_route('GET', '/', handle)

server = loop.create_server(app.make_handler(), '127.0.0.1', 8000)
print("Server started at http://127.0.0.1:8000")
loop.run_until_complete(server)
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass