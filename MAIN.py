"""import urllib2
result = urllib2.urlopen('https://maps.googleapis.com/maps/api/directions/json?origin=Brooklyn&destination=Queens&mode=transit&key=AIzaSyCIb177AKBFz11BDI_RIG4eXZPw3rJESqY').read()
print(result)"""
import urllib, json
import re
obj = file("A.json", "w")
obj2 = file("B.json", "w")
full = file("full.json","w")
url = "https://maps.googleapis.com/maps/api/directions/json?origin=33.773687,-84.391022&destination=38.928933,-77.020103&mode=walking&alternatives=true&key=AIzaSyCIb177AKBFz11BDI_RIG4eXZPw3rJESqY"

response = urllib.urlopen(url)
data = json.load(response)
obj2.write(str(data).replace("u'", "\n'"))
obj2.close
routes = []
processed =str(data).replace("u'", "'")
arrayprocessed = processed.split("overview_polyline': ")
obj3 = file("C.txt","w")
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
        full.write("Latitude:")
    else:
        full.write("Longitude:")
    for y in range(len(a[i])):

        full.write("\n"+a[i][y])
obj.write(arrayprocessed[0])
obj.write(str(data).replace("u'", "'"))
obj.close
obj3.close
