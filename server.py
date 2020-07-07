# -*- coding: utf-8 -*-
"""Flask app for offering data to consumption.

Example:

        $ cd .. && docker-compose up

"""
import datetime
import json
import logging
import sys

from flask import Flask, request


logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
)

# >> The application is a small service.
APP = Flask(__name__)

@APP.route("/news/", methods=["GET"])
def get_news():
    """route_endpoint

    >> The service accepts data from a GPS tracker device.
    >> In the beginning of a track, the service requests a route to be created...
    """
    APP.logger.debug("News feeds requested.")
    news = {"Hello": "World!"}
    return json.dumps(news), 200

if __name__ == "__main__":
    APP.run(host="0.0.0.0", debug=True)
