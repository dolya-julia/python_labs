from django import forms
from .models import Route


class RouteForm(forms.ModelForm):

    class Meta:
        model = Route
        fields = '__all__'


class PassengerForm(forms.ModelForm):

    class Meta:
        model = Route
        fields = '__all__'