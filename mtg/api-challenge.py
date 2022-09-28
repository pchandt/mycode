#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
import datetime
import reverse_geocoder as rg
    
URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()

    longitude =resp["iss_position"]["longitude"]

    latitude = resp["iss_position"]["latitude"]

    timestamp = resp["timestamp"]
    timestamp = datetime.datetime.fromtimestamp(timestamp)

    locator_resp = rg.search(latitude, longitude)

    city = locator_resp[0]["cc"]

    print(f"CURRENT LOCATION OF THE ISS:\nTimestamp: {timestamp}\nLon = {longitude}\nLat = {latitude}\nCity/Country : {city}, {country}")

if __name__ == "__main__":
    main()
