from django.db import models


class BusStation(models.Model):
    station_name = models.CharField(max_length=30, verbose_name="Станция")

    def __str__(self):
        return str(self.station_name)


class Passenger(models.Model):
    name = models.CharField(max_length=30, verbose_name="Имя")
    date_of_birth = models.DateField(verbose_name="Дата рождения")
    passport = models.CharField(max_length=10, verbose_name="Паспорт")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")

    def __str__(self):
        return f'{self.name} {self.passport}'


class Route(models.Model):
    departure = models.ForeignKey(BusStation, related_name='routes_as_departure', on_delete = models.CASCADE, verbose_name="Отправление")
    arrival = models.ForeignKey(BusStation, related_name='routes_as_arrival', on_delete = models.CASCADE, verbose_name="Прибытие")
    departure_time = models.DateTimeField(verbose_name="Время отправления")
    arrival_time = models.DateTimeField(verbose_name="Время прибытия")
    price = models.FloatField(verbose_name="Цена")
    passengers = models.ManyToManyField(Passenger, verbose_name="Пассажиры")

    def __str__(self):
        return f'{self.departure} {self.arrival}'


