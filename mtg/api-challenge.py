#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
import datetime
    
URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()

    longitude =resp["iss_position"]["longitude"]

    latitude = resp["iss_position"]["latitude"]

    timestamp = resp["timestamp"]
    timestamp = datetime.datetime.fromtimestamp(timestamp)

    print(f"CURRENT LOCATION OF THE ISS:\nTimestamp: {timestamp}\nLon = {longitude}\nLat = {latitude}")

if __name__ == "__main__":
    main()
