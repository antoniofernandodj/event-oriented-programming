from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    pass

    # def do_request(self):
    #     self.send_response(200)
    #     self.send_header('Content-type', 'text/plain')
    #     self.end_headers()
    #     self.wfile.write(bytes(f'Método HTTP: {self.command}', 'utf-8'))

    # def do_GET(self):
    #     self.do_request()

    # def do_POST(self):
    #     self.do_request()

class MyServer(HTTPServer):
    def __init__(self, host, port):
        server_address = (host, port)
        super().__init__(server_address, MyHandler)

def main():
    host = 'localhost'
    port = 8000
    server = MyServer(host, port)
    print(f'Servidor rodando em http://{host}:{port}')
    server.serve_forever()

if __name__ == '__main__':
    main()