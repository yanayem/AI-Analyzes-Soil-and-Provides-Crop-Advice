from django.shortcuts import render
from django.http import JsonResponse
import requests
import datetime
import random

OPENWEATHER_API_KEY = '963804a07802e5371e2a2bd19f6a7afb'
UNSPLASH_ACCESS_KEY = '1p8c8r_JXHlH5-CStbJgX5JNheF7_7YanrgSftDbZX8'

def weather_dashboard(request):
    # City from GET or default
    city = request.GET.get('city', 'Dhaka')

    # URLs
    weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric'
    forecast_url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={OPENWEATHER_API_KEY}&units=metric'
    unsplash_url = f'https://api.unsplash.com/photos/random?query={city}&orientation=landscape&client_id={UNSPLASH_ACCESS_KEY}'

    # Default values
    temp = humidity = rain = wind = pressure = feels_like = 0
    description = 'clear sky'
    icon = '01d'
    image_url = '/static/media/Untitled.png'
    exception_occurred = False

    # Fetch image
    try:
        data_img = requests.get(unsplash_url).json()
        image_url = data_img.get('urls', {}).get('regular', image_url)
    except:
        pass

    # Fetch current weather
    try:
        data = requests.get(weather_url).json()
        if data.get('cod') == 200:
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            pressure = data['main']['pressure']
            feels_like = data['main']['feels_like']
            wind = data['wind']['speed']
            description = data['weather'][0]['description']
            icon = data['weather'][0]['icon']
            rain = data.get('rain', {}).get('1h', 0)
        else:
            exception_occurred = True
    except:
        exception_occurred = True

    # Fetch hourly forecast for graph
    labels = []
    temp_data = []
    humidity_data = []
    try:
        forecast_data = requests.get(forecast_url).json()
        if forecast_data.get('cod') == "200":
            for i in range(0, 24, 3):
                dt_txt = forecast_data['list'][i]['dt_txt']
                labels.append(dt_txt.split()[1][:5])
                temp_data.append(forecast_data['list'][i]['main']['temp'])
                humidity_data.append(forecast_data['list'][i]['main']['humidity'])
    except:
        pass

    day = datetime.date.today()
    rain_drops = [random.randint(0, 100) for _ in range(50)]

    context = {
        'city': city,
        'temp': temp,
        'humidity': humidity,
        'rain': rain,
        'wind': wind,
        'pressure': pressure,
        'feels_like': feels_like,
        'description': description,
        'icon': icon,
        'day': day,
        'image_url': image_url,
        'exception_occurred': exception_occurred,
        'rain_drops': rain_drops,
        'labels': labels,
        'temp_data': temp_data,
        'humidity_data': humidity_data,
    }

    # ✅ Fixed AJAX detection for Django 4+
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse(context)

    return render(request, 'weather.html', context)
