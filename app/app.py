"""A flask app"""
from flask_cors import CORS
import flask
import routes


def add_cors(app: flask.Flask):
    CORS(
        app,
        supports_credentials=True,
        resources={
            r"*": {"origins": "*"},
        },
    )


def create_app(env: str) -> flask.Flask:
    app = flask.Flask(__name__)
    app.env = env

    app.register_blueprint(routes.bp)
    add_cors(app)

    return app
