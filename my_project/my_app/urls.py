from django.urls import path, include

from . import views

urlpatterns = [path("", views.chart, name="chart"),
               path("dht11/", views.dht11, name="dht11"),
               path("api/get_data/", views.get_data, name="get_data")
               ]
