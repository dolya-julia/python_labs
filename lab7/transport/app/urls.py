from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('route/create/', views.RouteCreate.as_view(template_name="app/route_update.html"),
         name='route_create'),
    path('route/<int:pk>/', views.route_detail, name='route_detail'),
    # path('route/<int:pk>', views.RouteDetailView.as_view(template_name="app/route_detail.html"), name='route_detail'),
    path('route/<int:pk>/update/', views.RouteUpdate.as_view(template_name="app/route_update.html"),
         name='route_update'),
]

