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
from flask_cors import CORS

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

app = Flask(__name__)
CORS(app)

@app.route("/show-news-sources/",  methods=["GET"]):
def show_sources():
    db = common.load_yaml_as_dict("./database.yaml")
    return json.dumps(db.get("newssources")), 200

@app.route("/news/", methods=["GET"])
def get_news():
    app.logger.debug("News feeds requested.")
    all_reader_results = []
    reader = rss_man.RssReader()
    db = common.load_yaml_as_dict("./database.yaml")
    sources = db.get("newssources").get("rss_urls")
    for url in sources:
        all_reader_results += reader.parse_feed(url)
    return json.dumps(all_reader_results), 200

@app.route("/weather/", methods=["GET"])
def get_weather():
    key = get_secrets().get("weather_key")
    wm = weather_man.WeatherMan(key)
    return wm.get_weather(), 200

@app.route('/add-source/', methods=['GET', 'POST'])
def add_source():
    if request.method == 'POST':
        source_url = request.form.get('source_url')
        db = common.load_yaml_as_dict("./database.yaml")
        sources = db.get("newssources").get("rss_urls"))
        try:
            assert(sources not in source_url)
        except AssertionError as err:
            return json.dumps({"Error": "That url is already in our sources."}), 400
        sources += source_url
        common.save_to_yaml(db)
        return json.dumps({"Success": "Source added."}), 200
    return '''<form method="POST">
                  New rss url: <input type="text" name="source_url"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
