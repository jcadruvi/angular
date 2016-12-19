from gevent.pywsgi import WSGIServer

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    ws = WSGIServer(('0.0.0.0', 5001), app)
    ws.serve_forever()
