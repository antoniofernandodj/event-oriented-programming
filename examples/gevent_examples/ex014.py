import gevent.monkey
gevent.monkey.patch_all()

from http.server import SimpleHTTPRequestHandler
from socketserver import ThreadingTCPServer

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello, world!')

if __name__ == '__main__':
    server_address = ('0.0.0.0', 8000)
    httpd = ThreadingTCPServer(server_address, Handler)
    httpd.serve_forever()