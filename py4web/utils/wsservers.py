import logging
from bottle import ServerAdapter

import socketio # pip install python-socketio

#
# If you don't want to use websocket or socketio you can delete-rename this file
#
#
# How I tested the servers from anyservers_list 
# 1 downloaded py4web applications from https://github.com/ali96343/facep4w  
#   ( it's near 8000 files: html+svg+css+png+jpg, 176 py-files, 7000 js-files )
# 2 run py4web with each server 
# 3 tested the applications list with https://github.com/linkchecker/linkchecker
#   with 10 threads active
# 4 access to the apps databases (sqlite) was not tested.
# 5 that's all
# 
# aiohttp  - test duration: 1064 seconds
# tornado  - test duration: 1065 seconds
# gevent   - test duration: 1126 seconds
# treading - test duration: 1135 seconds
#

#
# Today it is possible to use two protocols (socket.io and websockets) to build a chat server.
#
# For the websockets handler native server handlers are used. 
# For the socketio handlers, we use the nice library by Miguel Grinberg - python-socketio.
#
#
# To test the two installed protocols, please,   use two test applications: _socketio and _ws.
#
# The import libraries are done in the app-index.html files.
# in _socketio-index.html "<script src="https://cdn.socket.io/3.1.1/socket.io.min.js"></script>"
# in _ws-index.html " ws = new WebSocket('ws://127.0.0.1:8000/'); "
#
# Also at this link https://github.com/ali96343/py4web-chat , there is a more realistic chat server and the file anyservers.py
#

#  you can run server from wsservers_list with command
# ./py4web.py  run -s  wsgirefAioSioWsServer  apps
# ./py4web.py  run -s  tornadoSioWsServer  apps
# ./py4web.py  run -s  geventSioWsServer  apps
# ./py4web.py  run -s  wsgirefSioServer  apps

wsservers_list = ['wsgirefAioSioWsServer', 'tornadoSioWsServer', 'geventSioWsServer', 'wsgirefSioServer', ]

def wsgirefAioSioWsServer():
    import logging.handlers
    from aiohttp import web
    from aiohttp_wsgi import WSGIHandler  # pip install aiohttp_wsgi

    # https://pypi.org/project/aiohttp/
    async def handle(request):
        name = request.match_info.get('name', "Anonymous")
        text = "Hello, " + name
        return web.Response(text=text)
    
    async def wshandle(request):
        ws = web.WebSocketResponse()
        await ws.prepare(request)
    
        async for msg in ws:
            if msg.type == web.WSMsgType.text:
                await ws.send_str(f"Echo from ws.aiohttp: {msg.data}")
            elif msg.type == web.WSMsgType.binary:
                await ws.send_bytes(msg.data)
            elif msg.type == web.WSMsgType.close:
                break
    
        return ws


    sio_debug = False
    sio = socketio.AsyncServer(async_mode='aiohttp')

    @sio.event
    async def connect(sid, environ):
        sio_debug and print('connect ', sid)

    @sio.event
    async def disconnect(sid):
         sio_debug and print('disconnect ', sid)

    @sio.on('to_py4web')
    async def echo(sid, data):
         sio_debug and  print('from client: ', data)
         await sio.emit("py4web_echo", data)

    class AioSioWsServer(ServerAdapter):
        def run(self, app):
            if not self.quiet:
                log = logging.getLogger('loggingAioHttp')
                log.setLevel(logging.INFO)
                log.addHandler(logging.StreamHandler())
            wsgi_handler = WSGIHandler(app)
            app = web.Application()
            sio.attach(app)
            app.router.add_routes( [ web.get('/', wshandle), ])
            app.router.add_route("*", "/{path_info:.*}", wsgi_handler)
            web.run_app(app, host=self.host,  port=self.port)
    return AioSioWsServer


def wsgirefSioServer():
    # https://python-socketio.readthedocs.io/en/latest

    # ws does not work with this wsgirefSioServer 
    #  ./py4web.py run -s wsgirefSioServer   apps

    from wsgiref.simple_server import WSGIRequestHandler, WSGIServer
    from wsgiref.simple_server import make_server
    from socketserver import ThreadingMixIn
    import socket
    import sys
    from concurrent.futures import ThreadPoolExecutor  # pip install futures

    sio_debug = False
    sio = socketio.Server(async_mode='threading')

    @sio.event
    async def connect(sid, environ):
        sio_debug and print('connect ', sid)

    @sio.event
    async def disconnect(sid):
         sio_debug and print('disconnect ', sid)

    @sio.on('to_py4web')
    async def echo(sid, data):
         sio_debug and  print('from client: ', data)
         await sio.emit("py4web_echo", data)

    class WSGIRefPySoketIOServer(ServerAdapter):
        def run(self, app):

            class PoolMixIn(ThreadingMixIn):
                def process_request(self, request, client_address):
                    self.pool.submit(self.process_request_thread, request, client_address)

            class ThreadingWSGIServer(PoolMixIn, WSGIServer):
                daemon_threads = True
                pool = ThreadPoolExecutor(max_workers=40)

            class Server:
                def __init__(self, server_address = ('127.0.0.1', 8000), handler_cls = None):
                    self.sio=sio
                    self.wsgi_app = None
                    self.listen, self.port = server_address
                    self.handler_cls = handler_cls
                def set_app(self, app):
                    self.wsgi_app = socketio.WSGIApp(self.sio, app) 
                def get_app(self):
                    return self.wsgi_app
                def serve_forever(self):
                    self.server = make_server(
                        self.listen, self.port, self.wsgi_app, ThreadingWSGIServer, self.handler_cls
                    )
                    self.server.serve_forever()

            class FixedHandler(WSGIRequestHandler):
                def address_string(self): # Prevent reverse DNS lookups please.
                    return self.client_address[0]
                def log_request(*args, **kw):
                    #self.quiet = True
                    if not self.quiet:
                        return WSGIRequestHandler.log_request(*args, **kw)

            handler_cls = self.options.get('handler_class', FixedHandler)
            server_cls  = Server

            if ':' in self.host: # Fix wsgiref for IPv6 addresses.
                if getattr(server_cls, 'address_family') == socket.AF_INET:
                    class server_cls(server_cls):
                        address_family = socket.AF_INET6

            srv = make_server(self.host, self.port, app, server_cls, handler_cls)
            srv.serve_forever()
    return WSGIRefPySoketIOServer

def geventSioWsServer():
    # _websocket work with this geventSioWsServer 
    # ./py4web.py --usegevent  run -s geventSioWsServer   apps

    # tested with
    # pip install gevent==20.9.0
    # pip install greenlet==0.4.17
    # pip install gevent-websocket

    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    from geventwebsocket.logging import create_logger
    import sys

    sio_debug = False
    sio = socketio.Server( async_mode='gevent'  )

    @sio.event
    def connect(sid, environ):
        sio_debug and print('connect ', sid)

    @sio.event
    def disconnect(sid):
         sio_debug and print('disconnect ', sid)

    @sio.on('to_py4web')
    async def echo(sid, data):
         sio_debug and  print('from client: ', data)
         await sio.emit("py4web_echo", data)

    class GeventPySocketIOServer(ServerAdapter):
        def run(self, handler):

            handler = socketio.WSGIApp(sio, handler)
            server = pywsgi.WSGIServer((self.host, self.port), handler, handler_class=WebSocketHandler, **self.options)
            #self.quiet = True
            if not self.quiet:
                server.logger = create_logger('geventsocketio.logging')
                server.logger.setLevel(logging.INFO)
                server.logger.addHandler(logging.StreamHandler())

            server.serve_forever()
    return GeventPySocketIOServer


def tornadoSioWsServer():

    # py4web.py run -s tornadoSioWsServer apps
    
    import tornado.websocket
    import time, urllib
    from tornado.httputil import url_concat
    import tornado.httpclient

    ws_debug = True 
    
    class web_socket_handler(tornado.websocket.WebSocketHandler):
        # This class handles the websocket channel
        @classmethod
        def route_urls(cls):
            return (r'/',cls, {})
        
        def simple_init(self):
            self.last = time.time()
            self.stop = False
        
        def open(self):
            #    client opens a connection
            self.simple_init()
            ws_debug and print(f"tornado ws: {time.time() - self.last:.1f}: New client connected")
            self.write_message(f"tornado ws: {time.time() - self.last:.1f}: You are connected")
            
        def on_message(self, message):
            #    Message received on the handler
            ws_debug and print(f"Echo from tornado ws: {time.time() - self.last:.1f}: received message {message}")
            self.write_message(f"ECho from tornado ws: {time.time() - self.last:.1f}: You said - {message}")
            self.last = time.time()
        
        def on_close(self):
            #    Channel is closed
            ws_debug and print(f"tornado ws: {time.time() - self.last:.1f}: connection is closed")
            self.stop= True
        
        def check_origin(self, origin):
            return True

    def handle_request( response):
        pass
    
    import socketio
    sio_debug = False
    sio = socketio.AsyncServer(async_mode='tornado')

    @sio.event
    async def connect(sid, environ):
        sio_debug and print('sio: connect ', sid)

    @sio.event
    async def disconnect(sid):
         sio_debug and print('sio: disconnect ', sid)

    @sio.on('to_py4web')
    async def echo(sid, data):
         sio_debug and  print('sio: from client: ', data)
         await sio.emit("py4web_echo", data)


         #http_client = tornado.httpclient.AsyncHTTPClient()
         #params = {"a": 1, "b": 2}
         #request = url_concat("http://localhost:8000/_socketio/echo", params)
         #request = url_concat("http://localhost:8000/_socketio/echo/xx/yy/zz")

         #http_client.fetch(request, handle_request)


    class TornadoSioWsServer(ServerAdapter):

        def run(self, handler): # pragma: no cover
            if not self.quiet:
                log = logging.getLogger('tornadoSioWs')
                log.setLevel(logging.INFO)
                log.addHandler(logging.StreamHandler())

            import tornado.wsgi, tornado.httpserver,  tornado.web,  tornado.ioloop
            container = tornado.wsgi.WSGIContainer(handler)
            app= tornado.web.Application([
                    web_socket_handler.route_urls(),
                    (r"/socket.io/", socketio.get_tornado_handler(sio) ),
                    (r".*", tornado.web.FallbackHandler, dict(fallback=container) ),
                 ])
            server = tornado.httpserver.HTTPServer(app)
            server.listen(port=self.port,address=self.host)

            tornado.ioloop.IOLoop.instance().start()

    return TornadoSioWsServer

