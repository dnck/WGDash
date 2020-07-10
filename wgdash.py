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
import common

from dotenv import load_dotenv
from flask import Flask, request
from flask_cors import CORS  # This is the magic

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
app = Flask(__name__)
CORS(app)

@app.route("/news/", methods=["GET"])
def get_news():
    """route_endpoint

    >> The service accepts data from a GPS tracker device.
    >> In the beginning of a track, the service requests a route to be created...
    """
    app.logger.debug("News feeds requested.")
    db = common.load_yaml_as_dict("./database.yaml")
    
    ALL_READER_RESULTS = []
    reader = rss_man.RssReader()
        reader.parse_feed()
        ALL_READER_RESULTS += reader.result_set
    return json.dumps(ALL_READER_RESULTS), 200

@app.route("/weather/", methods=["GET"])
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

@app.route("/parse-source/", methods=["POST"])
def parse_new_source():
    source = request.get_json()
    summary_field_key = source.get("summary_key")
    title_field_key = source.get("title_key")
    url_field_key = source.get("url_key")
    more_keys = source.get("keys")


@app.route('/add-source/', methods=['GET', 'POST']) #allow both GET and POST requests
def form_example():
    if request.method == 'POST':
        # we will do our parsing
        source_url = request.form.get('source_url')
        source_reader = rss_man.RssReader()
        feed = source_reader.get_feed(source_url)
        result_set = []
        for entry in feed["entries"]:
            result_set.append(entry)
        return json.dumps(result_set), 200

    return '''<form method="POST">
                  New source url: <input type="text" name="source_url"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
