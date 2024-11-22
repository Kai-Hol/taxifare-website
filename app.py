import streamlit as st
import requests
import streamlit as st
from geopy.geocoders import Nominatim

def get_coordinates(address):
    geolocator = Nominatim(user_agent="my_geocoder")
    location = geolocator.geocode(address)
    if location is None:
        return None, None
    return location.latitude, location.longitude
date_input = st.date_input("Enter the date")
time_input = st.time_input("Enter the time")
pickup_address = st.text_input("Enter pickup address")
dropoff_address = st.text_input("Enter dropoff address")
passenger_count = int(st.slider("Enter the number of passengers", min_value=1, max_value=10))

if pickup_address:
  pickup_lat, pickup_long = get_coordinates(pickup_address)
  if pickup_lat and pickup_long:
      pass
  else:
      st.write("Pickup address not found.")

if dropoff_address:
  dropoff_lat, dropoff_long = get_coordinates(dropoff_address)
  if dropoff_lat and dropoff_long:
      pass
  else:
      st.write("Dropoff address not found.")

api_params = {
    "pickup_datetime": str(date_input) + ' ' +str(time_input),
    "pickup_longitude": pickup_long,
    "pickup_latitude": pickup_lat,
    "dropoff_longitude": dropoff_long,
    "dropoff_latitude": dropoff_lat,
    "passenger_count": passenger_count
}

endpoint = 'https://taxifare.lewagon.ai/predict'
request = requests.get(endpoint, api_params)

response = request.json()
fare = round(response["fare"], 2)
#st.write("Response:", request.json())
st.write(f"Estimated Fare: ${fare}")
