from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch
from forecast.models import UserSearchHistory, CitySearchCount
from forecast.forms import CityForm

class WeatherViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.weather_url = reverse('weather_view')
        self.city_search_counts_url = reverse('city_search_counts')
        self.valid_city = 'London'
        self.invalid_city = 'InvalidCity'

    @patch('forecast.views.get_data')
    def test_weather_view_get(self, mock_get_data):
        # Mock the response of get_data function
        mock_get_data.return_value = {
            'city': 'London',
            'country': 'United Kingdom',
            'weather_data': [['2024-07-19', 25, 30, 20], ['2024-07-20', 26, 31, 21], ['2024-07-21', 27, 32, 22], ['2024-07-22', 28, 33, 23]],
            'current_temp': 25,
            'feelslike': 27,
            'uv': 5,
            'humidity': 60
        }
        response = self.client.get(self.weather_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forecast/index.html')
        self.assertContains(response, 'London')
        self.assertContains(response, 'United Kingdom')

    @patch('forecast.views.get_data')
    def test_weather_view_post_valid_city(self, mock_get_data):
        mock_get_data.return_value = {
            'city': 'London',
            'country': 'United Kingdom',
            'weather_data': [['2024-07-19', 25, 30, 20], ['2024-07-20', 26, 31, 21], ['2024-07-21', 27, 32, 22], ['2024-07-22', 28, 33, 23]],
            'current_temp': 25,
            'feelslike': 27,
            'uv': 5,
            'humidity': 60
        }
        response = self.client.post(self.weather_url, {'city': self.valid_city})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forecast/index.html')
        self.assertContains(response, 'London')
        self.assertContains(response, 'United Kingdom')


    def test_city_search_count_view(self):
        CitySearchCount.objects.create(city='London', count=5)
        response = self.client.get(self.city_search_counts_url)
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, [{'city': 'London', 'count': 5}])

class CityFormTests(TestCase):
    def test_city_form_valid(self):
        form = CityForm(data={'city': 'London'})
        self.assertTrue(form.is_valid())

    def test_city_form_invalid(self):
        form = CityForm(data={'city': ''})
        self.assertFalse(form.is_valid())
