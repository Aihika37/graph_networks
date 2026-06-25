import random
import requests
API_KEY = "uceoIQrX8kzLUL0PzUXMJocmVB3tyiFh"

def get_traffic(lat, lon):
    url = (
        "https://api.tomtom.com/traffic/services/4/"
        "flowSegmentData/absolute/10/json"
        f"?key={API_KEY}"
        f"&point={lat},{lon}"
    )#making the request for data
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data["flowSegmentData"]

class TrafficEngine:
        @staticmethod
        def traffic_multiplier(flow_data):
            current = flow_data["currentSpeed"]
            free = flow_data["freeFlowSpeed"]
            if current <= 0:
                return 10.0
            ratio = free / current # if current free less than
            # free means road taking more time than usual..traffic factor>1
            return max(1.0, ratio)
