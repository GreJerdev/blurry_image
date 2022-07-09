from flask import Flask
from configuration.routes import init_routes


app = Flask(__name__)

init_routes(app)


if __name__ == '__main__':
    app.run(port=8080,host="0.0.0.0")