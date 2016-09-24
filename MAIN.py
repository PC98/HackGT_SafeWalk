"""import urllib2
result = urllib2.urlopen('https://maps.googleapis.com/maps/api/directions/json?origin=Brooklyn&destination=Queens&mode=transit&key=AIzaSyCIb177AKBFz11BDI_RIG4eXZPw3rJESqY').read()
print(result)"""
import urllib, json
obj = file("A.json", "w")
url = "https://maps.googleapis.com/maps/api/directions/json?origin=33.773687,-84.391022&destination=33.774791,-84.396436&mode=walking&alternatives=true&key=AIzaSyCIb177AKBFz11BDI_RIG4eXZPw3rJESqY"
response = urllib.urlopen(url)
data = json.load(response)
#obj.write(str(data).replace("u'", "\n'"))
obj.write(str(data).replace("u'", "\n"))
obj.close