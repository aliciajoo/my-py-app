import requests
import json

endpoint = "http://api.openweathermap.org/data/2.5/weather"
payload = {"q": "London,UK", "units":"metric", "appid":"e7c675268ab91c7bdaaaec6f087e13b2"}
response = requests.get(endpoint, params=payload)
data = response.json()

print response.url
print response.status_code
print response.headers["content-type"]

print response.text


temperature = data["main"]["temp"]
name = data["name"]
weather = data["weather"][0]["main"]
print u"It's {}C in {}, and the sky is {}".format(temperature, name, weather)
