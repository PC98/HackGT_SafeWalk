import googlemaps
import re

set_of_coordinates = []

def parse():

    API_KEY = "AIzaSyAQc3FQc8Crqjk_e6lY2WHz3zacGWpsdNA"
    origin = "33.776860,-84.392070"
    destination = "33.773875,-84.394581"

    gmaps = googlemaps.Client(key=API_KEY)
    directions_result = gmaps.directions(origin, destination, mode="walking", alternatives=True)
    
    for routes in directions_result:
        route = str(routes['legs'][0]['steps'])
        lat = list(map(float, re.findall("'lat': (-?\d+\.\d+)", route)))
        long = list(map(float, re.findall("'lng': (-?\d+\.\d+)", route)))
        set_of_coordinates.append(list(set(zip(lat, long))))

