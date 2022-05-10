import requests
import json


def get_wildfire():
    url = f"https://eonet.gsfc.nasa.gov/api/v3/events/geojson"
    response = requests.get(url).json()
    data = response.get("features")
    wildfire_data = []
    for datum in data:
        wildfire = datum.get("properties").get("categories")[0].get("id")
        if wildfire == "wildfires":
            wildfire_dict = {
                "title": datum.get("properties").get("title"),
                "date": datum.get("properties").get("date"),
                "link": datum.get("properties").get("link"),
                "coordinates": datum.get("geometry").get("coordinates"),
                "type": datum.get("geometry").get("type"),
            }
            wildfire_data.append(wildfire_dict)
    wildfire_json = {"type": "FeatureCollection", "features": wildfire_data}
    return wildfire_json
