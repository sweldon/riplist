from django.conf.urls import url
from browse import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^search_listings', views.search_listings, name='search_listings'),


]