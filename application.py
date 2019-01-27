from flask import Flask
import requests
import json
import time

app = Flask(__name__)

api_key = "AIzaSyABlH--kuE8mhX_wdycHH8L1bDuP7nsgOs"
placesURL = "https://maps.googleapis.com/maps/api/place/details/json?"
nearbyURL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"

radius = 10000
types = ["night_club","stadium","casino,bar","bowling_alley"]
finFields = ['name', 'rating', 'user_ratings_total', 'place_id', 'vicinity', 'geometry']

center_lat = 49.251450
center_lon = -123.160820

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

@app.route("/updateGData")
def updateGDat():
    allFinalData = {}
    for typex in types:
        finalData = {}
        parameters = {'key':api_key, 'radius': radius, 'location':str(center_lat)+','+str(center_lon), 'type':typex}
        r = requests.get(url=nearbyURL, params=parameters)
        data = r.json()
        i = 0
        finalData["place"+str(i)] = data['results']
        time.sleep(2)
        while 'next_page_token' in data:
            i = i+1
            parameters = {'key':api_key, 'radius': radius, 'pagetoken':data['next_page_token']}
            r = requests.get(url=nearbyURL, params=parameters)
            data = r.json()
            finalData["place"+str(i)] = data['results']
            time.sleep(2)
        allFinalData[typex] = finalData
    print(json.dumps(allFinalData))
    return cleanData(allFinalData)

def cleanData(data):
    finX = []
    for typex in data:
        subData = data[typex]
        print(typex)
        for page in subData:
            arr = subData[page]
            for place in arr:
                #print(json.dumps(place))
                if 'rating' in place:
                    tempDat = {}
                    tempDat['rating'] = place['rating']
                    tempDat['num_ratings'] = place['user_ratings_total']
                    tempDat['name'] = place['name']
                    tempDat['goog_id'] = place['place_id']
                    tempDat['address'] = place['vicinity']
                    geometry = place['geometry']
                    tempDat['geo_location'] = geometry['location']
                    finX.append(tempDat)
    return json.dumps(finX)
    

