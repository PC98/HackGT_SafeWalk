"""import urllib2
result = urllib2.urlopen('https://maps.googleapis.com/maps/api/directions/json?origin=Brooklyn&destination=Queens&mode=transit&key=AIzaSyCIb177AKBFz11BDI_RIG4eXZPw3rJESqY').read()
print(result)"""
import urllib, json
import re
obj = file("A.json", "w")
obj2 = file("B.json", "w")
url = "https://maps.googleapis.com/maps/api/directions/json?origin=33.773687,-84.391022&destination=33.774791,-84.396436&mode=walking&alternatives=true&key=AIzaSyCIb177AKBFz11BDI_RIG4eXZPw3rJESqY"
response = urllib.urlopen(url)
data = json.load(response)
obj2.write(str(data).replace("u'", "\n'"))
obj2.close
routes = []

#print(data["routes"])
for i in data["routes"]:
    processed =str(i).replace("u'", "'")
    arrayprocessed = processed.split("overview_polyline': ")


arrayprocessed.pop(0)
a = []

m = re.search("'lat': (\d+)","'lat': 33.7738867, 'lng': -84.39102040000002 }, 'steps': [")
if m:
    print m.groups()[0]
for i in routes:
    for
    a[i].append([])
obj.write(arrayprocessed[0])
#obj.write(str(data).replace("u'", "'"))
obj.close
