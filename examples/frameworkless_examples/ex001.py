from socket import (
    AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR, socket
)

class MyHTTPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = None

    def start(self):
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)
        print(f'Servidor rodando em http://{self.host}:{self.port}')

        while True:
            client_socket, client_address = self.server_socket.accept()
            self.handle_request(client_socket)

    def handle_request(self, client_socket: socket):
        request_data = client_socket.recv(1024).decode('utf-8')

        if request_data:
            print('request_data:', request_data)
            method = request_data.split(' ')[0]
            print(f'Método HTTP: {method}')

        response = 'HTTP/1.1 200 OK\nContent-Type: text/plain\n\nMétodo HTTP: ' + method
        client_socket.sendall(response.encode('utf-8'))
        client_socket.close()

def main():
    host = 'localhost'
    port = 8000
    server = MyHTTPServer(host, port)
    server.start()

if __name__ == '__main__':
    main()