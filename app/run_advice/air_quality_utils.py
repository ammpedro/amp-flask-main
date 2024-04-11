"""Utility function for reporting air quality"""
import os
import requests

OMW_APP_ID = os.getenv("OPEN_WEATHER_APP_ID")
OWM_AIR_POLLUTION_URL = f"https://api.openweathermap.org/data/2.5/air_pollution?appid={OMW_APP_ID}"

AIR_QUALITY_INDEX_MAP = {
    "1": ("Good", "Go run!"),
    "2": ("Fair", "Go run!"),
    "3": ("Moderate", "You could run!"),
    "4": ("Poor", "You shouldn't run!"),
    "5": ("Very Poor", "You shouldn't run!")
}


def get_air_pollution_data(location):
    """
    Takes a location {lat:"latitude", lon:"longitude"} and retrieves the current air pollution data
    """
    latitude = location.get("lat")
    longitude = location.get("lon")
    resp = requests.get(
        url=f"{OWM_AIR_POLLUTION_URL}&lat={latitude}&lon={longitude}",
        timeout=10
    )

    if resp.ok:
        data = resp.json()
        data_list = data.get("list")[0]
        aqi = str(data_list.get("main").get("aqi"))
        aq_components = data_list.get("components")
        aq_result = AIR_QUALITY_INDEX_MAP.get(aqi)

        return {
                   "status": "ok",
                   "message": f"Air quality is {aq_result[0]} right now; {aq_result[1]}",
                   "data": aq_components
               }, 200

    return {
               "status": "failed",
               "url": resp.request.url,
               "data": resp.json()
           }, resp.status_code
