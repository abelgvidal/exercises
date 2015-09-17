from tornado import gen
from tornado.httpclient import AsyncHTTPClient
from tornado.httpclient import HTTPClient
import tornado.ioloop
import tornado.web
import time

"""
example of async http request with tornado

output:
Async requests time: 0.5929031372070312
Sync requests time: 1.1293201446533203
Total time: 1.7222421169281006
"""


class MainHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        respuesta = ""
        
        start = time.time()
        urls_sync = ["http://www.yahoo.es", "http://www.yahoo.com", "http://www.themotion.com", "http://www.themotion.com"]
        urls_async = ["http://www.yahoo.es", "http://www.yahoo.com", "http://www.themotion.com", "http://www.themotion.com"]        
        
        async_start = time.time()

        http_client = AsyncHTTPClient()
        response_dict = yield dict(response1=http_client.fetch(urls_async.pop()),
                                   response2=http_client.fetch(urls_async.pop()),
                                   response3=http_client.fetch(urls_async.pop()),
                                   response4=http_client.fetch(urls_async.pop()))
        async_stop = time.time()

        respuesta += "<br>Async requests time: " + str(async_stop-async_start)


        sync_start = time.time()

        for url in urls_sync:
            sc = HTTPClient()                    
            response = sc.fetch(url)
            print(response.code)

        sync_stop = time.time()
            
        respuesta += "<br>Sync requests time: " + str(sync_stop-sync_start)        


        
        respuesta += "<br>Total time: " + str(time.time()-start)
        
        self.write(respuesta)
    
if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
    

