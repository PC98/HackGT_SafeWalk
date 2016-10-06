"""import urllib2
result = urllib2.urlopen('https://maps.googleapis.com/maps/api/directions/json?origin=Brooklyn&destination=Queens&mode=transit&key=AIzaSyCIb177AKBFz11BDI_RIG4eXZPw3rJESqY').read()
print(result)"""
import urllib, json
import re
def parse():
    full = file("ParsedJSONoutput.csv","w")
    url = "https://maps.googleapis.com/maps/api/directions/json?origin=33.779136,-84.406643&destination=33.771038,-84.391408&mode=walking&alternatives=true&key=AIzaSyCIb177AKBFz11BDI_RIG4eXZPw3rJESqY"
    response = urllib.urlopen(url)
    data = json.load(response)
    routes = []
    processed =str(data).replace("u'", "'")
    arrayprocessed = processed.split("overview_polyline': ")
    a = []
    for i in range(len(arrayprocessed)):
        lat = re.findall("'lat': (-?\d+\.\d+)",arrayprocessed[i])
        lng = re.findall("'lng': (-?\d+\.\d+)",arrayprocessed[i])
        if lat:
            a.append(lat)
        if lng:
            a.append(lng)
    for i in range(len(a)):
        if i%2 == 0:
            full.write("Latitude:\n")
        else:
            full.write("Longitude:\n")
        for y in range(len(a[i])):
            full.write("%s\n" % a[i][y])
    full.close()
parse()
