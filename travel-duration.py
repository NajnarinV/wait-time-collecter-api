
import requests
import json

response = requests.get("https://api.mapbox.com/directions-matrix/v1/mapbox/driving-traffic/-123.1193,49.2497;-123.124500,49.262211;-123.127930,49.281435;-123.146935,49.16873;-123.068991,49.320956;-123.095800,49.258308;-123.245415,49.264181;-123.129116,49.277396;-123.083663,49.312363?sources=0&destinations=1;2;3;4;5;6;7;8&access_token=pk.eyJ1IjoibmFqbmFyaW52IiwiYSI6ImNrYmtqN2t4czB4bmgzNXRkNzZrcGViNnoifQ.u2mxN3bQc4dYWBsonzzc6A")

matrix = response.json()

travel_time = matrix["durations"]

print(travel_time)