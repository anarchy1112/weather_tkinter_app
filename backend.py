import datetime

import requests
import json





base_url='https://api.openweathermap.org/data/2.5'
lat=45.2396
lon=19.8227

api_key='bc465a524e6f688aea578403df822ba2'

def current_weather(i):
    pass

def hourly_forecast(i):
    pass

def daily_forecast(i):
    pass




current_weather_endpoint='/weather?lat=' + str(lat) + '&lon=' + str(lon) + '&appid=' + api_key + '&units=metric'

current_weather_url=base_url+current_weather_endpoint

request=requests.get(current_weather_url)
result=request.json()

# print(json.dumps(result, sort_keys=True, indent=4))
sunrise =result['sys']['sunrise']
sunset =result['sys']['sunset']

print('Vreme u '+ result['name'])
print('Temperatura je ' +str(result['main']['temp']) + ' stepeni celzijusa')
print('Vreme je ' + result['weather'][0]['description'])
print('Izlazak sunca u '+ datetime.datetime.utcfromtimestamp(sunrise).strftime('%d.%m.%Y. %H:%M:%S'))
print('Zalazak sunca u '+ datetime.datetime.utcfromtimestamp(sunset).strftime('%d.%m.%Y. %H:%M:%S'))

forecast_endpoint='/forecast?lat=' + str(lat) + '&lon=' + str(lon) + '&appid=' + api_key + '&units=metric'

forecast_url = base_url + forecast_endpoint

request = requests.get(forecast_url)
result=request.json()

# print(json.dumps(result, sort_keys=True, indent=4))

for i in range(9):
    ts=result['list'][i]['dt']
    time= datetime.datetime.utcfromtimestamp(ts).strftime('%d.%m.%Y. %H:%M:%S')
    print(result['city']['name'] + ' weather at '+ time)
    print('Temperature will be ' +str(result['list'][i]['main']['temp']) + ' degrees celsius.')
    print('Weather will be '+ result['list'][i]['weather'][0]['description'])
    print()