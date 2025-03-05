import requests
import json
from datetime import datetime

# Function to fetch prayer times using latitude and longitude
def get_prayer_times_by_coords(lat, lon, method=2):
    url = "http://api.aladhan.com/v1/timings"
    params = {
        'latitude': lat,
        'longitude': lon,
        'method': method
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    if data['code'] == 200:
        return data['data']['timings']
    else:
        return None

# Input: Latitude and Longitude (You can look these up on Google Maps)
latitude = float(input("Enter the latitude: "))
longitude = float(input("Enter the longitude: "))

# Fetch prayer times
prayer_times = get_prayer_times_by_coords(latitude, longitude)

# If valid data is returned, print prayer times
if prayer_times:
    print(f"Prayer times for coordinates ({latitude}, {longitude}) on {datetime.now().strftime('%Y-%m-%d')}:")
    for prayer, time in prayer_times.items():
        print(f"{prayer}: {time}")
else:
    print("Failed to fetch prayer times. Please check your inputs.")
