from urllib.request import urlopen
import http.client
import json
import pandas as pd
import plotly.express as px
import streamlit as st

with urlopen('https://services1.arcgis.com/ESMARspQHYMw9BZ9/arcgis/rest/services/Counties_December_2021_EN_BFC/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson') as response:
    counties = json.load(response)
    
#Grabs temp from met API:
def getweather(lat, long):
    conn = http.client.HTTPSConnection("api-metoffice.apiconnect.ibmcloud.com")

    headers = {
        'X-IBM-Client-Id': st.secrets['api_key'], #Replace secret before github push
        'X-IBM-Client-Secret': st.secrets['api_secret'], #Replace secret before github push
        'accept': "application/json"
        }

    conn.request("GET", f"/v0/forecasts/point/three-hourly?excludeParameterMetadata=true&includeLocationName=true&latitude={lat}&longitude={long}", headers=headers)

    res = conn.getresponse()
    data = res.read()
    js = json.loads(data)

    return js["features"][0]["properties"]["timeSeries"][0]['feelsLikeTemp']

lats = [52.34966, 54.63638, 53.07858, 50.72558, 50.93805, 51.80982, 51.81971, 51.04474, 51.80879, 51.19295, 53.86216, 52.68779, 53.11102, 52.67123, 54.09371, 53.1285, 51.77155, 51.07182, 52.9093, 52.25385, 51.26803, 52.17977, 50.95134, 52.21287]
longs= [-0.23506, -2.90213, -1.6021, -3.65698, 0.334559, 0.54106, -2.15235, -1.24735, -0.27699, 0.72137, -2.46091, -1.3779, -0.23884, 0.964714, -1.55032, -1.00656, -1.29146, -3.29595, -2.02756, 1.04919, -0.33911, -1.56874, -0.45933, -2.20935]
ids = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
nom = 0
temps = []
for i in range(len(lats)):
    temps.append(getweather(lats[nom], longs[nom]))
    nom += 1

df = pd.DataFrame({"Temp" : temps, "ID" : ids})

fig = px.choropleth_mapbox(df, geojson=counties, locations='ID', color='Temp',
                           color_continuous_scale="Viridis",
                           range_color=(10, 25),
                           mapbox_style="carto-positron",
                           zoom=5, center = {"lat": 53.3498, "lon": -6.2661},
                           opacity=0.5,
                           labels={'Temp':'Temperature (deg C)'}
                          )

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()