import asyncio  
import aiohttp

def fetch_page(url, idx):  
    response = yield from aiohttp.request('GET', url)

    if response.status == 200:
        print("data fetched successfully for: %d" % idx)
    else:
        print("data fetch failed for: %d" % idx)
        print(response.content, response.status)

def main():  
    url = 'https://www.infohostal.com'

    urls = [url] * 100

    coros = []
    for idx, url in enumerate(urls):
        coros.append(asyncio.Task(fetch_page(url, idx)))

    yield from asyncio.gather(*coros)

if __name__ == '__main__':  
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
