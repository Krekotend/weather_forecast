from django.contrib import admin
from .models import UserSearchHistory, CitySearchCount

class UserSearchHistoryAdmin(admin.ModelAdmin):
    list_display = ('session_key', 'last_city', 'count')
    search_fields = ('session_key', 'last_city')
    list_filter = ('last_city',)

class CitySearchCountAdmin(admin.ModelAdmin):
    list_display = ('city', 'count')
    search_fields = ('city',)
    list_filter = ('city',)

admin.site.register(UserSearchHistory, UserSearchHistoryAdmin)
admin.site.register(CitySearchCount, CitySearchCountAdmin)

