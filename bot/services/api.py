import requests

API_KEY = '1224e7d3db47b619825107c01b3d588f'

def get_city_lon_lat(city):
    lat, lon = None, None
    url_lon_lat = f'https://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY}'
    response = requests.get(url_lon_lat)
    if response.status_code == 200:
        data = response.json()
        lat = data[0]['lat']
        lon = data[0]['lon']
    return lat, lon


def get_weather_city(lat, lon):
    weather_dict_data = {}
    weather_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}'
    response = requests.get(weather_url)
    if response.status_code == 200:
        weather_data = response.json()
        weather = weather_data['weather'][0]['main']
        humidity = weather_data['main']['humidity']
        temp = weather_data['main']['temp']
        temp_max = weather_data['main']['temp_max']
        temp_min = weather_data['main']['temp_min']
        weather_dict_data.update({
            'weather': weather,
            'humidity': humidity,
            'temp': round(temp - 273),
            'temp_max': round(temp_max - 273),
            'temp_min': round(temp_min - 273)
        })
    return weather_dict_data
