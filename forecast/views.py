import requests
from django.http import JsonResponse
from django.shortcuts import render
from .forms import CityForm
from .models import UserSearchHistory, CitySearchCount
from .config import load_config

api_key: str = load_config().api_w.token


def get_data(city):
    response = requests.get(
        f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=4&aqi=no&alerts=no'
    )
    if response.status_code == 200:
        data = response.json()
        city = data['location']['name']
        current_temp = data['current']['temp_c']
        country = data['location']['country']
        feelslike = data['current']['feelslike_c']
        uv = data['current']['uv']
        humidity = data['current']['humidity']
        forecast_days = [
            [i['date'], i['day']['avgtemp_c'], i['day']['maxtemp_c'], i['day']['mintemp_c']]
            for i in data['forecast']['forecastday']
        ]
        return {
            'city': city,
            'country': country,
            'weather_data': forecast_days,
            'current_temp': current_temp,
            'feelslike': feelslike,
            'uv': uv,
            'humidity': humidity
        }
    return False


def weather_view(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key

    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            context = get_data(city)

            if context:
                request.session['last_city'] = city

                user_history, created = UserSearchHistory.objects.get_or_create(session_key=session_key, last_city=city)
                if not created:
                    user_history.count += 1
                    user_history.save()

                city_count, created = CitySearchCount.objects.get_or_create(city=city)
                if not created:
                    city_count.count += 1
                city_count.save()

                return render(request, 'forecast/index.html', context)
            else:
                return render(request, 'forecast/wrong_city.html', {'error': 'City not found'})
        else:
            return render(request, 'forecast/index.html', {'error': 'Invalid form submission'})
    else:
        last_city = request.session.get('last_city', 'London')
        form = CityForm()
        context = get_data(last_city)

        if context:
            return render(request, 'forecast/index.html', context)
        else:
            return render(request, 'forecast/wrong_city.html', {'error': 'City not found'})


def city_search_count_view(request):
    city_counts = CitySearchCount.objects.all().values('city', 'count')
    return JsonResponse(list(city_counts), safe=False)
