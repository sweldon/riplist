from django.conf.urls import url
from list import views

urlpatterns = [

    url(r'^$', views.create_listing, name='create_listing'),
    url(r'^submit', views.submit_listing, name='submit_listing'),

]