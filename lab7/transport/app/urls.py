from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('route/create/', views.RouteCreate.as_view(template_name="app/change_data.html"),
         name='route_create'),
    path('route/<int:pk>/', views.route_detail, name='route_detail'),
    path('route/<int:pk>/update/', views.RouteUpdate.as_view(template_name="app/change_data.html"),
         name='route_update'),
    path('route/<int:pk>/delete/', views.RouteDelete.as_view(template_name="app/confirm_delete.html"),
         name='route_delete'),
    path('passenger/create/', views.PassengerCreate.as_view(template_name="app/change_data.html"),
         name='passenger_create'),
    path('passenger/<int:pk>/', views.PassengerDetail.as_view(template_name="app/passenger_detail.html"),
         name='passenger_detail'),
    path('passenger/<int:pk>/update/', views.PassengerUpdate.as_view(template_name="app/change_data.html"),
         name='passenger_update'),
    path('passenger/<int:pk>/delete/', views.PassengerDelete.as_view(template_name="app/confirm_delete.html"),
         name='passenger_delete'),
]

