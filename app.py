from flask import Flask, Response, request

app = Flask(__name__)

@app.route('/')
def hello():
    str = "Hello, world!"
    return Response(str, mimetype="text/html")


if __name__ == "__main__":
    app.run()
