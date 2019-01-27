from flask import Flask
import requests
import json

app = Flask(__name__)

api_key = "AIzaSyABlH--kuE8mhX_wdycHH8L1bDuP7nsgOs"
placesURL = "https://maps.googleapis.com/maps/api/place/details/json?"

@app.route("/test")
def home():
    a = {"string": "Server is up!"}
    return json.dumps(a)

@app.route("/gTest")
def getx():
    a = {"string": "Server is up!"}
    parameters = {'fields': 'rating,geometry', 'key':api_key, 'placeid':"ChIJN1t_tDeuEmsRUsoyG83frY4"}
    r = requests.get(url=placesURL, params=parameters)
    data = r.json()
    return json.dumps(data)