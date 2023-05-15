import gevent.monkey
gevent.monkey.patch_all()

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

if __name__ == '__main__':
    from gevent.pywsgi import WSGIServer
    server = WSGIServer(('0.0.0.0', 8000), app)
    server.serve_forever()