from django.contrib import admin
from .models import BusStation
from .models import Route
from .models import Passenger


class PostBusStation(admin.ModelAdmin):
    list_display = ['station_name']
    search_fields = ['station_name']


class PostRoute(admin.ModelAdmin):
    list_display = ['departure', 'arrival', 'departure_time', 'arrival_time', 'price']
    list_filter = ('price', 'departure_time', 'departure', 'arrival')
    search_fields = ['departure__station_name', 'arrival__station_name']
    filter_horizontal = ('passengers',)


class PostPassenger(admin.ModelAdmin):
    list_display = ['name', 'date_of_birth', 'passport']
    search_fields = ['name', 'passport']


admin.site.register(BusStation, PostBusStation)
admin.site.register(Route, PostRoute)
admin.site.register(Passenger, PostPassenger)

