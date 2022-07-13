import http.client
import json
from dotenv import load_dotenv
import os
import streamlit as st
from geopy.geocoders import Nominatim

#Loading .env file
def configure():
    load_dotenv()


#Bringing data from met API
def getweather(lat, long):
    configure()
    conn = http.client.HTTPSConnection("api-metoffice.apiconnect.ibmcloud.com")

    headers = {
        'X-IBM-Client-Id': os.getenv('api_key'), #Replace os.getenv('api_key') with your API Key. Or use a .env file containing the creds
        'X-IBM-Client-Secret': os.getenv('api_secret'), #Replace os.getenv('api_secret') with your API Secret
        'accept': "application/json"
        }

    conn.request("GET", f"/v0/forecasts/point/three-hourly?excludeParameterMetadata=true&includeLocationName=true&latitude={lat}&longitude={long}", headers=headers)

    res = conn.getresponse()
    data = res.read()
    js = json.loads(data) #Return data as JSON

    #return(data.decode("utf-8")) Uncomment this for original data return
    return js

st.title("Weather Dashboard")

geolocator = Nominatim(user_agent="Streamlit")
    
placechoice = st.text_input("Enter Location", key="keytext")

mylocation = geolocator.geocode(placechoice) # Using Nominatim to get lat/long coords from Location

choice1 = st.number_input('Latitude', min_value = -85, max_value = 85, key="keylat")
choice2 = st.number_input('Longitude', min_value = -180, max_value = 179, key="keylong")

if placechoice:
    choice1 = mylocation.latitude
    choice2 = mylocation.longitude

data = getweather(choice1, choice2)
location = data["features"][0]["properties"]["location"]["name"]
timeSeries0 = data["features"][0]["properties"]["timeSeries"][0]
alltimeseries = data["features"][0]["properties"]["timeSeries"]

col1,col2,col3 = st.columns(3)
with col2:
    st.title(location)
    st.caption(f"Lat: {choice1}, Long: {choice2}")
st.header(f"48 Hour Forecast")
col1, col2, col3, col4 = st.columns(4)

def get48hrforecast():
    temp1, temp2, temp3 = timeSeries0["feelsLikeTemp"], timeSeries0["windSpeed10m"], timeSeries0["probOfRain"]
    col1.metric(timeSeries0["time"][:10], timeSeries0["time"][11:-1])
    col2.metric("Temperature", f'{temp1} °C')
    col3.metric("Windspeed", f'{temp2} mph')
    col4.metric("Rain Probability", f'{temp3}%')
    
    for v in alltimeseries[1:16]:
        tm, t, w, r = v["time"], v["feelsLikeTemp"], v["windSpeed10m"], v["probOfRain"]
        col1.metric(tm[:10], tm[11:-1], "3", delta_color="off")
        col2.metric("Temperature", f'{t} °C', round(t - temp1, 2))
        col3.metric("Windspeed", f'{w} mph', round(w - temp2, 2))
        col4.metric("Rain Probability", f'{r}%', round(r - temp3, 2))
        temp1, temp2, temp3 = t, w, r
        
get48hrforecast()