from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .forms import RouteForm
from django.urls import reverse_lazy

from .models import Route, Passenger


def index(request):
    routes = Route.objects.all()
    passengers = Passenger.objects.all()
    return render(request, 'app/index.html', {'routes': routes, 'passengers': passengers})


def route_detail(request, pk):
    route = get_object_or_404(Route, pk=pk)
    return render(request, 'app/route_detail.html', {'route': route})


class RouteUpdate(UpdateView):
    model = Route
    fields = '__all__'
    template_name = 'app/route_update.html'
    success_url = reverse_lazy('index')


class RouteCreate(CreateView):
    model = Route
    fields = ('departure', 'arrival', 'departure_time', 'arrival_time', 'price')
    template_name = 'app/route_update.html'
    success_url = reverse_lazy('index')


class RouteDelete(DeleteView):
    model = Route
    success_url = "/"


class PassengerDetail(DetailView):
    model = Passenger
    fields = '__all__'


class PassengerCreate(CreateView):
    model = Passenger
    fields = '__all__'