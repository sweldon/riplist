from django.conf.urls import url
from browse import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^searchLocation/', views.searchLocation, name='searchLocation'),


]