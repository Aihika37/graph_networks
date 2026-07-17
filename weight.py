import random

class WeightEngine:
    def weather_multiplier(self,weather):
        multiplier = 1.0
        rain = 0
        #finding precipitation data from weather data
        if "rain" in weather:
            rain = weather["rain"].get("1h",0)
        visibility = weather.get("visibility",10000)#finding visibility
        wind = weather["wind"]["speed"]#getting wind speed
        if rain > 5:#if rain more,time taken will be more,hence multiplier increase
            multiplier += 0.3
        if visibility < 2000:#if visibility less,time taken will be more,hence multiplier increase
            multiplier += 0.2
        if wind > 15:#if wind speed,time taken will be more,hence multiplier increase
            multiplier += 0.1
        return multiplier
