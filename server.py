from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import os
import json
import urllib.request

def stock_price(request):
    url = "http://hq.sinajs.cn/list=sh000001"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
    message = the_page
    return Response(message)

def hello_world(request):
    name = "Ryan"
    if name == None or len(name) == 0:
        name = "world"
    message = "Hello, " + name + "!\n"
    return Response(message)

if __name__ == '__main__':
    port = int(os.environ.get("PORT"))
    with Configurator() as config:
        config.add_route('stock', '/')
        config.add_route('hello', '/hello')
        config.add_view(stock_price, route_name='stock')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', port, app)
    server.serve_forever()
