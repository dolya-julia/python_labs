from django.contrib import admin
from .models import BusStation
from .models import Route
from .models import Passenger
# from .models import PassRoutes


class PostBusStation(admin.ModelAdmin):
    list_display = ['station_name']


class PostRoute(admin.ModelAdmin):
    list_display = ['departure', 'arrival', 'departure_time', 'arrival_time', 'price']
    list_filter = ('price', 'arrival_time', 'departure','arrival')
    search_fields = ['departure__station_name', 'arrival__station_name']


class PostPassenger(admin.ModelAdmin):
    list_display = ['name', 'date_of_birth', 'passport']
    list_filter = ('date_of_birth',)

# class PostPassRoutes(admin.ModelAdmin):
#     list_display = ['pass_id', 'routes_id']


admin.site.register(BusStation, PostBusStation)
admin.site.register(Route, PostRoute)
admin.site.register(Passenger, PostPassenger)
# admin.site.register(PassRoutes, PostPassRoutes)
