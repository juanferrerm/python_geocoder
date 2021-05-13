import requests
import codecs
import pandas as pd

df =    pd.read_csv(r"DATA_WITH_ADDRESSES - two columns: id & address.txt", sep = ",", header = None)
df =    df.rename(columns= {0: "id", 1: "address"})
address = df['address'].tolist()
lat = []
lon = []
for direccion in address:
    address2 = ""
    for i, char in enumerate(direccion):
        if char == " ":
            address2 += "+"
        else:
            address2 += char
    apikey='API KEY FROM GOOGLE'
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + address2 + '&key=' + apikey
    response = requests.get(url)
    resp_json_payload = response.json()

    if resp_json_payload['status']=="OK":
        a = resp_json_payload['results'][0]['geometry']['location']
        lat.append(a["lat"])
        lon.append(a["lng"])
    else:
        lat.append(999)
        lon.append(999)

df['lat'] = lat
df['lon'] = lon
df
out= "OUTPUT.dta"
df.to_stata(out)
