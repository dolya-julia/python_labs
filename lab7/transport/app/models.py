from django.db import models


class BusStation(models.Model):
    station_name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.station_name)


class Passenger(models.Model):
    name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    passport = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.name} {self.passport}'


class Route(models.Model):
    departure = models.ForeignKey(BusStation, related_name='routes_as_departure', on_delete = models.CASCADE)
    arrival = models.ForeignKey(BusStation, related_name='routes_as_arrival', on_delete = models.CASCADE)
    departure_time = models.DateTimeField()
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.FloatField()
    passengers = models.ManyToManyField(Passenger)

    def __str__(self):
        return f'{self.departure} {self.arrival}'


