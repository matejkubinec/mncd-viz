import numpy as np

np.float_ = np.float64
np.Inf = np.inf

from applicationinsights.flask.ext import AppInsights
from flask import Flask, request, Response, send_from_directory, jsonify
from flask_swagger import swagger
from controllers.single_layer_controller import single_layer
from controllers.multi_layer_controller import multi_layer
from controllers.common_charts_controller import common_charts
import logging
import json
import os

app = Flask(__name__)
APPINSIGHTS_KEY = os.environ.get("APPINSIGHTS_INSTRUMENTATIONKEY")
app.config["APPINSIGHTS_INSTRUMENTATIONKEY"] = APPINSIGHTS_KEY
app.register_blueprint(single_layer)
app.register_blueprint(multi_layer)
app.register_blueprint(common_charts)

appinsights = AppInsights(app)

streamHandler = logging.StreamHandler()
app.logger.addHandler(streamHandler)


@app.after_request
def after_request(response):
    appinsights.flush()
    return response


@app.route("/spec")
def spec():
    return jsonify(swagger(app, from_file_keyword="swagger_from_file"))


@app.route("/")
def home():
    return send_from_directory("static", "index.html")


@app.route("/<path:path>")
def docs(path):
    return send_from_directory("static", path)


if __name__ == "__main__":
    logging.basicConfig(filename='error.log', level=logging.DEBUG)
    app.run(host='0.0.0.0')
