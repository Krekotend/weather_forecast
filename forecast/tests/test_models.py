from django.test import TestCase
from forecast.models import UserSearchHistory, CitySearchCount

class UserSearchHistoryModelTests(TestCase):
    def setUp(self):
        self.session_key = 'testsessionkey'
        self.last_city = 'London'
        self.user_search_history = UserSearchHistory.objects.create(
            session_key=self.session_key, last_city=self.last_city
        )

    def test_user_search_history_creation(self):
        self.assertEqual(self.user_search_history.session_key, self.session_key)
        self.assertEqual(self.user_search_history.last_city, self.last_city)
        self.assertEqual(self.user_search_history.count, 1)

    def test_user_search_history_increment(self):
        self.user_search_history.count += 1
        self.user_search_history.save()
        self.assertEqual(self.user_search_history.count, 2)

class CitySearchCountModelTests(TestCase):
    def setUp(self):
        self.city = 'London'
        self.city_search_count = CitySearchCount.objects.create(city=self.city)

    def test_city_search_count_creation(self):
        self.assertEqual(self.city_search_count.city, self.city)
        self.assertEqual(self.city_search_count.count, 1)

    def test_city_search_count_increment(self):
        self.city_search_count.count += 1
        self.city_search_count.save()
        self.assertEqual(self.city_search_count.count, 2)
