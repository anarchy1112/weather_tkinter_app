import datetime

import requests
import json

base_url='https://api.openweathermap.org/data/2.5'
lat=45.2396
lon=19.8227

api_key='bc465a524e6f688aea578403df822ba2'

current_weather_endpoint='/weather?lat=' + str(lat) + '&lon=' + str(lon) + '&appid=' + api_key + '&units=metric'
current_weather_url=base_url+current_weather_endpoint

forecast_endpoint='/forecast?lat=' + str(lat) + '&lon=' + str(lon) + '&appid=' + api_key + '&units=metric'
forecast_url = base_url + forecast_endpoint

request_current = requests.get(current_weather_url)
result_current = request_current.json()

request_forecast = requests.get(forecast_url)
result_forecast = request_forecast.json()

def current_weather():
    sunrise = result_current['sys']['sunrise']
    sunset = result_current['sys']['sunset']
    result=[]
    result.append(f"{result_current['name']}")
    result.append(f"Temp {result_current['main']['temp']} degrees Celsius")
    result.append(f"Weather is {result_current['weather'][0]['description']}")
    result.append(f"Sunrise at {datetime.datetime.utcfromtimestamp(sunrise).strftime('%d.%m.%Y. %H:%M:%S')}")
    result.append(f"Sunset at {datetime.datetime.utcfromtimestamp(sunset).strftime('%d.%m.%Y. %H:%M:%S')}")
    return result


def hourly_forecast(i):

    ts = result_forecast['list'][i]['dt']
    time = datetime.datetime.utcfromtimestamp(ts).strftime('%d.%m.%Y. %H:%M:%S')
    result1=[]
    result1.append(f"{result_forecast['city']['name']}")
    result1.append(f"Weather at {time}")
    result1.append(f"Temp will be {result_forecast['list'][i]['main']['temp']} degrees celsius.")
    result1.append(f"Weather will be {result_forecast['list'][i]['weather'][0]['description']}")
    return result1


def daily_forecast(i):
    request = requests.get(forecast_url)
    result = request.json()
    ts = result['list'][i]['dt']
    time = datetime.datetime.utcfromtimestamp(ts).strftime('%d.%m.%Y. %H:%M:%S')
    result2 = []
    result2.append(f"{result_forecast['city']['name']}")
    result2.append(f"Weather at {time}")
    result2.append(f"Temp will be {result_forecast['list'][i]['main']['temp']} degrees celsius.")
    result2.append(f"Weather will be {result_forecast['list'][i]['weather'][0]['description']}")
    return result2
