# -*- coding: utf-8 -*-
"""Flask app for offering data to consumption.

Example:

        $ cd .. && docker-compose up

"""
import datetime
import json
import logging
import os
import sys

import rss_man
import weather_man

from dotenv import load_dotenv
from flask import Flask, request


SCRIPT_DIRNAME, SCRIPT_FILENAME = os.path.split(os.path.abspath(__file__))

logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
)

def get_secrets():
    load_dotenv(".env")
    weather_key = os.getenv("WEATHER_KEY")
    return {"weather_key": weather_key}

# >> The application is a small service.
APP = Flask(__name__)

@APP.route("/news/", methods=["GET"])
def get_news():
    """route_endpoint

    >> The service accepts data from a GPS tracker device.
    >> In the beginning of a track, the service requests a route to be created...
    """
    APP.logger.debug("News feeds requested.")
    ALL_READER_RESULTS = []
    for reader in [
        rss_man.WashingtonPostParser(),
        rss_man.NYTRssParser(),
    ]:
        reader.parse_feed()
        ALL_READER_RESULTS += reader.result_set
    return json.dumps(ALL_READER_RESULTS), 200

@APP.route("/weather/", methods=["GET"])
def get_weather():
    key = get_secrets().get("weather_key")
    wm = weather_man.WeatherMan(key)
    return wm.get_weather(), 200

"""
POST add new source
 -> present full rss json
 -> select fields
 -> POST fields for new source
update new source <-
"""

@APP.route("/add-source/", methods=["POST"])
def add_source():
    source = request.get_json()
    url = source.get("url")
    if not url:
        return {"Missing Data": "need 'url' field in data"}, 400
    source_reader = rss_man.RssReader()
    feed = source_reader.get_feed(url)
    result_set = []
    for entry in feed["entries"]:
        result_set.append(entry)
    return json.dumps(result_set), 200

@APP.route("/parse-source/", methods=["POST"])
def parse_new_source():
    source = request.get_json()
    summary_field_key = source.get("summary_key")
    title_field_key = source.get("title_key")
    url_field_key = source.get("url_key")
    more_keys = source.get("keys")







if __name__ == "__main__":
    APP.run(host="0.0.0.0", debug=True)
