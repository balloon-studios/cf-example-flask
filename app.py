import os
import pprint
from flask import Flask, Response, request
import logging

app = Flask(__name__)

logging.basicConfig(level='DEBUG')
log = logging.getLogger()

@app.route('/')
def hello():
    info = { "Request": request.environ, "Environment": os.environ.__dict__['data'] }
    str = pprint.pformat(info,width=10)
    return Response(str, mimetype="text/plain")


if __name__ == "__main__":
    app.run()
