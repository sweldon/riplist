from django.conf.urls import url
from rip import views

urlpatterns = [

    url(r'^$', views.rip, name='rip'),
    url(r'^searchLocation/', views.searchLocation, name='searchLocation'),


]