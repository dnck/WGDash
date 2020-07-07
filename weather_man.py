import requests


class WeatherMan():
    def __init__(self, key):
        self.city = "Berlin"
        self.country = "Germany"
        self.zip = "12047"
        self.baseurl = "http://api.weatherstack.com/current"
        self.key = key

    def get_weather(self):
        params = {
          "access_key": self.key,
          "query": self.city
        }
        api_result = requests.get(self.baseurl, params)
        api_response = api_result.json()
        return api_response
