import asyncio
import aiofiles
import aiohttp
import logging
import re
import sys
import os

import lxml.html

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

HEADERS = {
    '''USER-AGENT': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
       Chrome/40.0.2214.85 Safari/537.36'''
}
MAX_PICS = 10
SUBREDDIT = "earthporn"


class WorkerPool:
    def __init__(self, loop, coro, worker_count, options):
        self.loop = loop or asyncio.get_event_loop()
        self.result = None
        self.queue = asyncio.Queue(loop=self.loop)
        self.coro = coro
        self.worker_count = worker_count
        self.options = options

    async def run(self):
        workers = [asyncio.Task(self.coro(self.loop, self.queue, self.options))
                   for _ in range(self.worker_count)]
        await self.queue.join()
        for worker in workers:
            worker.cancel()


async def _fetch(loop, queue, options):
    while True:
        try:
            url, utype = await queue.get()
            logger.debug('url: %s, url type: %s', url, utype)
            async with aiohttp.ClientSession(loop=loop, headers=HEADERS) as session:
                async with session.get(url) as resp:
                    if utype == 'seed':
                        text = await resp.text()
                        for link in _parse_links(text):
                            queue.put_nowait((link, 'post'))
                    elif utype == 'post':
                        text = await resp.text()
                        queue.put_nowait((_get_image_link(text), 'img'))
                    else:
                        outdir = os.path.join('/tmp', SUBREDDIT, options['mods'].replace('/', '_'))
                        await _get_image(resp, outdir)
            logger.debug('about to finish task, queue size: %s', queue.qsize())
            queue.task_done()
        except asyncio.CancelledError:
            break
        except:
            logger.exception('error')
            raise




def main(mods=''):
    try:
        outdir = os.path.join('/tmp', SUBREDDIT, mods.replace('/', '_'))
        os.makedirs(outdir)
    except:
        logger.warn("oops couldn't create folder")

    try:
        loop = asyncio.get_event_loop()
        worker_pool = WorkerPool(loop, _fetch, 5, options={'sr': SUBREDDIT, 'mods': mods})
        seed_url = 'http://imgur.com/r/{}{}'.format(SUBREDDIT, mods)
        worker_pool.queue.put_nowait((seed_url, 'seed'))

        loop.run_until_complete(worker_pool.run())
    except KeyboardInterrupt:
        sys.stderr.flush()
    except:
        logger.exception('error with loop')
    finally:
        loop.close()


if __name__ == '__main__':
    main(mods='/top/year')

