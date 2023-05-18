from http.server import SimpleHTTPRequestHandler, BaseHTTPRequestHandler, HTTPServer
from http import HTTPStatus
from socketserver import TCPServer
    

TCPServer.server_close = lambda _: print('Closing the server...')

class Handler(BaseHTTPRequestHandler):
    socket = ('localhost', 8002)
    def main(self):

        command = self.command
        path = self.path

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
        
        self.wfile.flush()

    def check_request(self):
        if not self.check_requestline():
            return False
        
        if not self.parse_request():
            return False
        
        return True

    def check_requestline(self):
        if len(self.raw_requestline) > 65536:
            self.requestline = ''
            self.request_version = ''
            self.command = ''
            self.send_error(HTTPStatus.REQUEST_URI_TOO_LONG)
            return False
        if not self.raw_requestline:
            self.close_connection = True
            return False
        
        return True

    def handle_one_request(self):
        try:
            self.raw_requestline = self.rfile.readline(65537)
            if not self.check_request():
                return
            
            self.main()
        except TimeoutError as e:
            #a read or a write timed out.  Discard this connection
            self.log_error("Request timed out: %r", e)
            self.close_connection = True
            return


with TCPServer(Handler.socket, Handler) as httpd:
    print("Servidor iniciado na porta", Handler.socket[1])
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
        # print('\nShutting down...')
        # print("Server stopped.")





# if __name__ == "__main__":
#     server = HTTPServer(Handler.socket, Handler)
#     print(f"Server started http://{socket[0]}:{socket[1]}")

#     try:
#         server.serve_forever()
#     except KeyboardInterrupt:
#         pass

#     server.server_close()
#     print("Server stopped.")