import logging
from bottle import ServerAdapter

__all__ = ['geventWebSocketServer', 'wsgirefThreadingServer', 'geventPySocketIOServer', 'wsgirefPySoketIOServer', 'tornadoSocketIOServer' ]

def geventWebSocketServer():
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    from geventwebsocket.logging import create_logger

    class GeventWebSocketServer(ServerAdapter):
        def run(self, handler):
            server = pywsgi.WSGIServer((self.host, self.port), handler, handler_class=WebSocketHandler, **self.options)

            if not self.quiet:
                server.logger = create_logger('geventwebsocket.logging')
                server.logger.setLevel(logging.INFO)
                server.logger.addHandler(logging.StreamHandler())

            server.serve_forever()
    return GeventWebSocketServer

def wsgirefThreadingServer():
    #https://www.electricmonk.nl/log/2016/02/15/multithreaded-dev-web-server-for-the-python-bottle-web-framework/

    from wsgiref.simple_server import WSGIRequestHandler, WSGIServer
    from wsgiref.simple_server import make_server
    from socketserver import ThreadingMixIn
    import socket
    from concurrent.futures import ThreadPoolExecutor  # pip install futures

    class WSGIRefThreadingServer(ServerAdapter):
        def run(self, app):

            class PoolMixIn(ThreadingMixIn):
                def process_request(self, request, client_address):
                    self.pool.submit(self.process_request_thread, request, client_address)

            class ThreadingWSGIServer(PoolMixIn, WSGIServer):
                daemon_threads = True
                pool = ThreadPoolExecutor(max_workers=40)

            class Server:
                def __init__(self, server_address = ('127.0.0.1', 8000), handler_cls = None):
                    self.wsgi_app = None
                    self.listen, self.port = server_address
                    self.handler_cls = handler_cls
                def set_app(self, app):
                    self.wsgi_app = app
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
    return WSGIRefThreadingServer


def wsgirefPySoketIOServer():
    # https://www.electricmonk.nl/log/2016/02/15/multithreaded-dev-web-server-for-the-python-bottle-web-framework/
    # https://python-socketio.readthedocs.io/en/latest/server.html#standard-threads

    # websocket does not work with this wsgirefPySoketIOServer 
    #  ./py4web.py run -s wsgirefPySoketIOServer   apps

    from wsgiref.simple_server import WSGIRequestHandler, WSGIServer
    from wsgiref.simple_server import make_server
    from socketserver import ThreadingMixIn
    import socket
    import sys
    from concurrent.futures import ThreadPoolExecutor  # pip install futures

    try:
        import socketio
    except BaseException:
        sys.exit('pls, install python-socketio')


    sio_debug = False
    sio = socketio.Server(async_mode='threading')

    @sio.event
    def connect(sid, environ):
        sio_debug and print('connect ', sid)

    @sio.event
    def disconnect(sid):
         sio_debug and print('disconnect ', sid)

    @sio.on('to_py4web')
    def echo(sid, data):
         sio_debug and  print('from client: ', data)
         sio.emit("py4web_echo", data)

    @sio.event
    def my_message(sid, data):
        sio_debug and  print('Send message ', data)
        sio.send(data)

    @sio.on('message')
    def message(sid, data):
          sio_debug and print('message ', data)


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

def geventPySocketIOServer():
    # https://stackoverflow.com/questions/54703656/python-socketio-how-to-emit-message-from-server-to-client
    # websocket work with this geventPySocketIOServer 
    # ./py4web.py --usegevent  run -s geventPySocketIOServer   apps

    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    from geventwebsocket.logging import create_logger
    import sys

    try:
        import socketio
    except BaseException:
        sys.exit('pls, install python-socketio')


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

    @sio.event
    def my_message(sid, data):
        sio_debug and  print('Send message ', data)
        sio.send(data)

    @sio.on('message')
    def message(sid, data):
          sio_debug and print('message ', data)


    @sio.on("my_new_message")
    def handle_message(sid, data):
         sio_debug and print("from client my_new_message:", data)
 
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


def tornadoSocketIOServer():

    # py4web.py run -s tornadoSocketIOServer apps
    
    '''
websockets + tornado about

# https://stackoverflow.com/questions/62044284/tornado-websocket-server-and-websocket-client-concurrently-in-one-loop-with-asyn
# https://www.includehelp.com/python/how-to-implement-a-websocket-server-using-tornado.aspx
# https://docs.aiohttp.org/en/stable/client_quickstart.html#websockets

    '''
    
    import tornado.websocket as ws
    import time

    ws_debug = False 
    
    class web_socket_handler(ws.WebSocketHandler):
        '''
        This class handles the websocket channel
        '''
        @classmethod
        def route_urls(cls):
            return (r'/',cls, {})
        
        def simple_init(self):
            self.last = time.time()
            self.stop = False
        
        def open(self):
            '''
                client opens a connection
            '''
            self.simple_init()
            ws_debug and print("ws: New client connected")
            self.write_message("You are connected")
            
        def on_message(self, message):
            '''
                Message received on the handler
            '''
            ws_debug and print("ws: received message {}".format(message))
            self.write_message("You said: {}".format(message))
            self.last = time.time()
        
        def on_close(self):
            '''
                Channel is closed
            '''
            ws_debug and print("ws: connection is closed")
            self.stop= True
            #self.loop.stop()
        
        def check_origin(self, origin):
            return True

    # socketio    pip install python-socketio
    
    import socketio
    sio_debug = True
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

    class TornadoSocketIOServer(ServerAdapter):

        def run(self, handler): # pragma: no cover
            import tornado.wsgi, tornado.httpserver,  tornado.web,  tornado.ioloop
            import tornado.websocket
            container = tornado.wsgi.WSGIContainer(handler)
            app= tornado.web.Application([
                    web_socket_handler.route_urls(),
                    (r"/socket.io/", socketio.get_tornado_handler(sio) ),
                    (r".*", tornado.web.FallbackHandler, dict(fallback=container) ),
                 ])
            server = tornado.httpserver.HTTPServer(app)
            server.listen(port=self.port,address=self.host)

            tornado.ioloop.IOLoop.instance().start()

    return TornadoSocketIOServer

