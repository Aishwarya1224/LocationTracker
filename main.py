import phonenumbers
from test import number
import folium

from phonenumbers import geocoder
Key="0acbae22f58c4942a959a7e30a8c4192"
ch_num=phonenumbers.parse(number,"CH")
youLoc=geocoder.description_for_number(ch_num,"en")
print(youLoc)

from phonenumbers import carrier
service_num= phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_num, "en"))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(Key)
Query= str(youLoc)
results=geocoder.geocode(Query)
print(results)

lat=results[0]["geometry"]["lat"]
lng=results[0]["geometry"]["lng"]
print(lat,lng)

myMap= folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=youLoc).add_to(myMap)
myMap.save("myLocation.html")
