import gevent
from gevent.pywsgi import WSGIServer

def app(environ, start_response):

    status = '200 OK'
    headers = {'Content-type': 'text/html'}
    response_body = b'Hello, world!'

    start_response(status, headers.items())
    return [response_body]

# Create a WSGIServer and run the server
server = WSGIServer(('0.0.0.0', 8000), app)
server.serve_forever()